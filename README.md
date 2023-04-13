[![](https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-gradient.svg)]()

# Sky Diffusion

This codebase contains an implementation of a deep diffusion model to predict the next frames of a sky camera, and thereby forecast PV power.
It is an extension of the [Cloud Diffusion](https://github.com/tcapelle/cloud_diffusion) repository. The crucial difference from original repository is the type of data the models have been trained on: In the original version the diffusion model predicts satelite images of cloud formations, whereas here the diffusion models are used to predict sky images from the [SKIPP'D](https://github.com/yuhao-nie/Stanford-solar-forecasting-dataset#1) dataset, which also includes power measurements of a PV system next to the sky camera.

## Main Idea and Intuition 💡

Diffusion models, as seen in DALL-E 2 or Stable Diffusion, have recently gained a lot of attention for their impressive image generation capabilities. These models are trained to generate high-quality images by gradually denoising images into a meaningful image. For a more detailed explanation see this [video]()

In this project, we leverage diffusion models to generate sky images, with the goal of improving very-short term solar forecasting (horizons of a couple of minutes). However, rather than conditioning the generation of a sky image on text, we condition it on the past few frames. This allows us to leverage the information contained in the previous frames to generate more accurate predictions of how the sky will look in the future. By then using a second neural network to transpose this image to a single power value, we arrive at PV power forecasts.

## Setup

1. Clone this repository and run ...

## Usage



## Training a Simple Diffusion Model



## Running Inference


## License

This code is released under the [MIT License](LICENSE).
