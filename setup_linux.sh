#!/bin/bash

# Install: 
# chmod +x install_env_linux.sh
# ./install_env_linux.sh

script_path=$(readlink -f "$0")
oneinstall_dir=$(dirname "$script_path")
env_yml_path="${oneinstall_dir}/environment.yml"
echo $env_yml_path

# Add conda-forge channel
conda config --append channels conda-forge

# Update 'base' env
echo "Update base environment:"
conda update --a --y
pip install --upgrade pip 
apt-get install libvips -y

# Create `one` env
echo "Create 'one' environment:"
conda env create -f "${env_yml_path}"
conda activate one
conda update --a --y
pip install --upgrade pip
conda clean --a --y

# Install 'cuda'
echo "Install 'cuda':"
install_cuda_script="${oneinstall_dir}/install_cuda.sh"
"$install_cuda_script"

# Install `mish-cuda`
echo "Install 'mish-cuda':"
install_mish_cuda_script="${oneinstall_dir}/install_cuda.sh"
"$install_mish_cuda_script"
