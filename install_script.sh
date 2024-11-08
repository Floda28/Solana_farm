#!/bin/bash
mkdir Sonic && cd Sonic
git clone https://github.com/Floda28/Solana_farm.git .
sudo apt update && sudo apt install -y python3 python3-pip
pip3 install -r requirements.txt
screen -S Sonic_auto_transaction
