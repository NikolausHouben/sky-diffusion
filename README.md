[![](https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-gradient.svg)]()

# Sky Diffusion

This codebase contains an implementation of a deep diffusion model to predict the next frames of a sky camera, and thereby forecast PV power.
It is an extension of the [Cloud Diffusion](https://github.com/tcapelle/cloud_diffusion) repository. The crucial difference from original repository is the type of data the models have been trained on: In the original version the diffusion model predicts satelite images of cloud formations, whereas here the diffusion models are used to predict sky images from the [SKIPP'D](https://github.com/yuhao-nie/Stanford-solar-forecasting-dataset#1) dataset, which also includes power measurements of a PV system next to the sky camera.

## Main Idea 💡

Diffusion models, as seen in DALL-E 2 or Stable Diffusion, have attracted great attention for their image generation capabilities. In these apps, users can *condition* their image generation on text. Sky cameras have been an effective solution to improve very-short term solar forecasting (horizons of a couple of minutes). Of course, with enough training data, a diffusion model could also be trained to generate sky images. However, it would be little use to generate these images based on text. Rather, we would like to know how the clouds will behave in the future, given their movements of the past. In other words, we would like to *condition* the generation of a sky image on the past few frames.

## Setup

1. Clone this repository and run ...
2. Set up your WandB account by signing up at [wandb.ai](https://wandb.ai/site).
3. Set up your WandB API key by running `wandb login` and following the prompts.

## Usage

To train the model, run `python train.py`. You can play with the parameters on top of the file to change the model architecture, training parameters, etc.

You can also override the configuration parameters by passing them as command-line arguments, e.g.

```bash
> python train.py --epochs=10 --batch_size=32
```

## Training a Simple Diffusion Model

This training is based on a Transformer based Unet (UViT), you can train the default model by running:

```bash
> python train_uvit.py
```

## Running Inference
If you are only interested on using the trained models, you can run inference by running:

```bash
> python inference.py  --future_frames 10 --num_random_experiments 2
```

This will generate 10 future frames for 2 random experiments.

## License

This code is released under the [MIT License](LICENSE).
