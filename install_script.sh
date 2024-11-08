#!/bin/bash
git clone https://github.com/Floda28/Solana_farm.git && \
apt update && \
apt-get install python3.12 -y && \
apt install python3-pip -y && \
cd Solana_farm && \
pip3 install -r requirements.txt && \
screen -S Sonic_auto_transaction
