#!/bin/bash
mkdir -p Sonic && cd Sonic || { echo "Не удалось создать или зайти в папку Sonic"; exit 1; }
git clone https://github.com/Floda28/Solana_farm.git . || { echo "Не удалось клонировать репозиторий"; exit 1; }
apt update
apt-get install python3.12 -y || { echo "Не удалось установить Python 3.12"; exit 1; }
apt install python3-pip -y || { echo "Не удалось установить pip"; exit 1; }
pip3 install -r requirements.txt || { echo "Не удалось установить зависимости"; exit 1; }
screen -S Sonic_auto_transaction || { echo "Не удалось создать screen сессию"; exit 1; }