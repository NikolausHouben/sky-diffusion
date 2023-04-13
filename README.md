[![](https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-gradient.svg)]()

# Sky Diffusion

This codebase contains an implementation of a deep diffusion model to predict the next frames of a sky camera, and thereby forecast PV power.
It is an extension of the [Cloud Diffusion](https://github.com/tcapelle/cloud_diffusion) repository. The crucial difference from original repository is the type of data the models have been trained on: In the original version the diffusion model predicts satelite images of cloud formations, whereas here the diffusion models are used to predict sky images from the [SKIPP'D](https://github.com/yuhao-nie/Stanford-solar-forecasting-dataset#1) dataset, which also includes power measurements of a PV system next to the sky camera.

## Main Idea 💡

Diffusion models, as seen in DALL-E 2 or Stable Diffusion, have attracted great attention for their image generation capabilities. In these apps, users can *condition* their image generation on text. Sky cameras have been an effective solution to improve very-short term solar forecasting (horizons of a couple of minutes). Of course, with enough training data, a diffusion model could also be trained to generate sky images. However, it would be little use to generate these images based on text. Rather, we would like to know how the clouds will behave in the future, given their movements of the past. In other words, we would like to *condition* the generation of a sky image on the past few frames.

## Setup

1. Clone this repository and run ...

## Usage



## Training a Simple Diffusion Model



## Running Inference


## License

This code is released under the [MIT License](LICENSE).
