from pathlib import Path
from types import SimpleNamespace

import wandb
import torch
from torch.utils.data import DataLoader
from torch.optim import AdamW
from torch.optim.lr_scheduler import OneCycleLR


from cloud_diffusion.dataset import download_dataset, CloudDataset
from cloud_diffusion.utils import (
    MiniTrainer, init_ddpm, 
    ddim_sampler, set_seed, parse_args)
from cloud_diffusion.ddpm import collate_ddpm, get_unet_params, UNet2D


PROJECT_NAME = "ddpm_clouds"
DATASET_ARTIFACT = 'capecape/gtc/np_dataset:v0'

config = SimpleNamespace(    
    epochs=50, # number of epochs
    model_name="unet_small", # model name to save [unet_small, unet_big]
    strategy="ddpm", # strategy to use ddpm
    noise_steps=1000, # number of noise steps on the diffusion process
    sampler_steps=333, # number of sampler steps on the diffusion process
    seed=42, # random seed
    batch_size=128, # batch size
    img_size=64, # image size
    device="cuda", # device
    num_workers=8, # number of workers for dataloader
    num_frames=4, # number of frames to use as input
    lr=5e-4, # learning rate
    validation_days=3, # number of days to use for validation
    log_every_epoch=5, # log every n epochs to wandb
    n_preds=8, # number of predictions to make
    )

def train_func(config):
    config.model_params = get_unet_params(config.model_name, config.num_frames)

    set_seed(config.seed)
    device = torch.device(config.device)

    # downlaod the dataset from the wandb.Artifact
    files = download_dataset(DATASET_ARTIFACT, PROJECT_NAME)
    train_ds = CloudDataset(files=files[:-config.validation_days],  
                            num_frames=config.num_frames, img_size=config.img_size)
    valid_ds = CloudDataset(files=files[-config.validation_days:], 
                            num_frames=config.num_frames, img_size=config.img_size).shuffle()

    collate_fn = collate_ddpm

    # DDPM dataloaders
    train_dataloader = DataLoader(train_ds, config.batch_size, shuffle=True, 
                                collate_fn=collate_fn,  num_workers=config.num_workers)
    valid_dataloader = DataLoader(valid_ds, config.batch_size, shuffle=False, 
                                collate_fn=collate_fn,  num_workers=config.num_workers)

    # model setup
    model = UNet2D(**config.model_params).to(device)
    init_ddpm(model)

    ## optim params
    config.total_train_steps = config.epochs * len(train_dataloader)
    optimizer = AdamW(model.parameters(), lr=config.lr, eps=1e-5)
    scheduler = OneCycleLR(optimizer, max_lr=config.lr, total_steps=config.total_train_steps)

    # sampler
    sampler = ddim_sampler(steps=config.sampler_steps)

    # Metrics
    loss_func = torch.nn.MSELoss()

    trainer = MiniTrainer(train_dataloader, valid_dataloader, model, optimizer, scheduler, 
                          sampler, device, loss_func)
    wandb.config.update(config)
    trainer.fit(config)
    

if __name__=="__main__":
    parse_args(config)
    with wandb.init(project=PROJECT_NAME, config=config, tags=["ddpm", config.model_name]):
        train_func(config)