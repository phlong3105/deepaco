# DeepACO: A Robust Deep Learning-based Automatic Checkout System

This repository contains our team's (SKKU Automation Lab) source code for 
building solutions for the 2022 AI City Challenge Track 4 
(Multi-Class Product Counting & Recognition for Automated Retail Checkout). 

![Example 02](docs/testA_2.gif)

## Installation

We recommend using Ubuntu 20.04, Python 3.9+ and PyTorch (version >= v1.11.0) with `conda` environment .
We also use PyCharm as the main IDE. 

The `aic22_track4` can be installed in the local python environment using the below commands:

```shell
mkdir -p one
mkdir -p one/datasets
cd one

# Install `aic22_track4` package
git clone https://github.com/phlong3105/aic22_track4
cd aic22_track4/install
chmod +x install.sh
conda init bash
./install.sh  # Install package using `sudo`. When prompt to input the 
              # dataset directory path, you should enter: <some-path>/one/datasets

cd ..
pip install --upgrade -e .  # This will clone and install `onevision` package

# (Optional) Install `onevision` package
cd ..
git clone https://github.com/phlong3105/onevision
cd onevision
pip install --upgrade -e .
```

## Inference

Download [pretrained models](https://o365skku-my.sharepoint.com/:u:/g/personal/phlong_o365_skku_edu/EX7Rn_xKsAlEgEW6RDCOTBABB90GAUA76-vFVr0Mwme9_w?e=96gV5b) and copy them to `aic22_track4/src/aic/pretrained/scaled_yolov4`

Download and copy testing videos to `aic22_track4/data/aic22retail/test_b`
```text
one
  |__ datasets (this folder contains the actual raw data)
  |__ aic22_track4
        |__ data
        |     |__ aic22retail
        |           |__ test_a
        |           |     |__ testA_1.mp4
        |           |     |__ testA_2.mp4
        |           |     |__ ..
        |           |__ test_b
        |                 |__ testB_1.mp4
        |                 |__ testB_2.mp4
        |                 |__ ..
        |__ src
              |__ aic
                    |__ pretrained
                    |     |__ scaled_yolov4
                    |__ ...
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

Download the training data [zip file](https://o365skku-my.sharepoint.com/:u:/g/personal/phlong_o365_skku_edu/EXmFKp_8KKNFv9VC1POLr5cBE6RXIw39HqvIg5ajBXsq7g?e=M0BSLo) and extract it inside `one/datasets/aicity`:
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

# The new trained weights will be located at: 
aic22_track4/src/aic/pretrained/scaled_yolov4/exp0_yolov4-p5_aic22retail117_448/weights/best.pt

# After training is done, copy the best weight and rename it to: 
aic22_track4/src/aic/pretrained/scaled_yolov4/yolov4-p5_aic22retail117_448.pt
```


## Citation

If you find our work useful, please cite the following:

```text
@inreview{Pham2022,  
    author={Long Hoang Pham and Duong Nguyen-Ngoc Tran and Huy-Hung Nguyen and 
            Tai Huu-Phuong Tran and Hyung-Joon Jeon and Hyung-Min Jeon and Jae Wook Jeon},  
    title={DeepACO: A Robust Deep Learning-based Automatic Checkout System},  
    booktitle={CVPR Workshop},
    year={2022}  
}
```

## Contact

If you have any questions, feel free to contact Long Pham ([phlong@skku.edu](phlong@skku.edu))
