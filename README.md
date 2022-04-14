# AIC: A library for AI City Challenge

This repository, `aic`, contains the source code for building solutions for 
AI City Challenge.

## Installation

We recommend to use Python 3.9+ and PyTorch (version >= v1.11.0) with `conda` environment.
The `aic22_track4` can be installed in the local python environment using the below commands:

```shell
mkdir -p one
mkdir -p one/datasets
cd one

# Install `aic22_track4` package (main solution)
git clone git@github.com:phlong3105/aic22_track4
cd aic22_track4/install
sh ./install_env_linux.sh    # Create conda environment
sudo ./install_env_linux.sh  # Install package using `sudo`
pip install -e .
```

Download pretrained models and copy them to `aic22_track4/src/aic/pretrained/scaled_yolov4`:
[https://drive.google.com/drive/folders/1xKCGTWnGmZBu5treyh_2i8ppWVhiOoFq?usp=sharing](https://drive.google.com/drive/folders/1xKCGTWnGmZBu5treyh_2i8ppWVhiOoFq?usp=sharing)

## Inference

Download and copy testing videos to `aic22_track4/data/aic22retail/test_b`:
```text
one
  |__ datasets (this folder contains the actual raw data)
  |__ aic22_track4
        |__ data
              |__ aic22retail
                    |__ test_a
                    |     |__ testA_1.mp4
                    |     |__ testA_2.mp4
                    |     |__ ..
                    |__ test_b
                          |__ testB_1.mp4
                          |__ testB_2.mp4
                          |__ ..
```

Run inference code:
```shell
conda activate one  # By default, our conda environment is named `one`
cd aic22_track4/scripts

# Run synchronous processing pipeline
python aic22_retail_checkout_all.py --subset "test_b" --configs "configs_yolov4p5_448" --save_results True

# Run asynchronous processing pipeline
python aic22_retail_checkout_all_async.py --subset "test_b" --configs "configs_yolov4p5_448" --save_results True
```

## Training

Download and copy training data to `one/datasets`:
```text
one
  |__ datasets (this folder contains the actual raw data)
  |     |__ aicity
  |__ aic22_track4
```
