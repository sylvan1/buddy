#!/usr/bin/env bash

sudo timedatectl set-timezone Europe/Warsaw
sudo locale-gen pl_PL.UTF-8
sudo apt-get update


sudo apt-get -y install git
sudo apt-get -y install  python3 python3-dev python3-psycopg2 python3-setuptools libjpeg-dev libtiff5-dev zlib1g-dev
sudo curl https://bootstrap.pypa.io/get-pip.py  | sudo python3

cd /home/vagrant/workspace/buddy
sudo pip3 install -r requirements/dev.txt
sudo -u vagrant python3 manage.py migrate
