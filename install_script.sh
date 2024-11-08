#!/bin/bash
mkdir -p Sonic && cd Sonic
git clone https://github.com/Floda28/Solana_farm.git
apt update
apt-get install python3.12 -y
apt install python3-pip -y 
pip3 install -r requirements.txt
screen -S Sonic_auto_transaction 
