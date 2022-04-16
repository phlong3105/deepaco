# AIC: A library for AI City Challenge

This repository, `aic22_track4`, contains the source code for building solutions 
for the 2022 AI City Challenge Track 4 (Multi-Class Product Counting & 
Recognition for Automated Retail Checkout).

![Example 01](docs/testA_1.gif)
![Example 01](docs/testA_2.gif)

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
sh ./setup_linux.sh    # Create conda environment
sudo ./setup_linux.sh  
# Install package using `sudo`. When prompt to input the dataset directory 
# path, you should enter: <some-path>/one/datasets

pip install -e .
```

Download [pretrained models](https://drive.google.com/drive/folders/1xKCGTWnGmZBu5treyh_2i8ppWVhiOoFq?usp=sharing) and copy them to `aic22_track4/src/aic/pretrained/scaled_yolov4`:

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

Download the training data [zip file](https://drive.google.com/file/d/1fCp6iFTKTD8yPb_HF8unvqCumJcJ9uoZ/view?usp=sharing) and extract it inside `one/datasets/aicity`:
```text
one
  |__ datasets (this folder contains the actual raw data)
  |     |__ aicity
  |           |__ aic22retail
  |__ aic22_track4
```

Run training script:
```shell
conda activate one  # By default, our conda environment is named `one`
cd aic22_track4/scripts

# Run training script
python aic22_train_scaled_yolov4.py --run "train" --cfg "yolov4-p5_aic22retail117_448"
```

## Citation

If you find our work useful, please cite the following:

```text
@inproceedings{Pham2022,  
    author={Long Hoang Pham, Duong Nguyen-Ngoc Tran, Huy-Hung Nguyen, 
            Tai Huu-Phuong Tran, Hyung-Joon Jeon, Hyung-Min Jeon, and Jae Wook Jeon},  
    title={DeepACO: A Robust Deep Learning-based Automatic Checkout System},  
    booktitle={CVPR Workshop},
    year={2022}  
}
```
