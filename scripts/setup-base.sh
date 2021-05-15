#! /bin/bash

sudo apt update && sudo apt upgrade

# Docker
sudo apt-get remove docker docker-engine docker.io containerd runc

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# Nginx
sudo apt install nginx

# Iptables
sudo apt-get install iptables

# virtualvenv
sudo python3 -m pip install --upgrade pip
pip3 install virtualenv

# Git
sudo apt install git

# Tree
sudo apt-get install tree

# Vim
sudo apt-get install vim
