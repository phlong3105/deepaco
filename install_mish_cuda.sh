#!/bin/bash

script_path=$(readlink -f "$0")
oneinstall_dir=$(dirname "$script_path")

# Install `mish-cuda`
echo "Install 'mish-cuda':"
mish_cuda_dir="${oneinstall_dir}/mish-cuda"
cd "$mish_cuda_dir" || exit
apt install gcc-10 -y
apt install g++-10 -y
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 10
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-10 10
python setup.py build install
