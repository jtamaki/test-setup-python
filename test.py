import numpy as nu

print("hello world!")


# install docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -a -G docker {user}
sudo service docker restart

# install nvidia-docker
curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list |   sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list
sudo apt-get update
sudo apt-get install nvidia-container-runtime
sudo systemctl restart docker

# install nvidia driver
sudo apt update -y
sudo apt install -y ubuntu-drivers-common
ubuntu-drivers devices
sudo apt install -y --no-install-recommends nvidia-driver-535
