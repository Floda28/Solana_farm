#!/bin/bash

git clone https://github.com/Floda28/Solana_farm.git && \
apt-get update && \
apt-get install software-properties-common -y && \
add-apt-repository ppa:deadsnakes/ppa -y && \
apt-get update && \
apt-get install python3.12 -y && \
apt-get install python3-pip -y && \
cd Solana_farm && \
pip3 install -r requirements.txt
