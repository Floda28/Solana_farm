import json
from solana.rpc.api import Client
from solders.keypair import Keypair  # type: ignore
from solders.pubkey import Pubkey as PublicKey  # type: ignore
from solders.system_program import TransferParams, transfer
from solana.transaction import Transaction
from dotenv import load_dotenv
import base58
import random
import time
import os

# Загрузка переменных окружения
load_dotenv()

# Загрузка параметров клиента из конфигурационного файла
with open(os.path.join(os.path.dirname(__file__), "RPC.json"), "r") as config_file:
    config = json.load(config_file)
    rpc_url = config["rpc_url"]

# Настройка клиента для Sonic Devnet
client = Client(rpc_url)

# Ввод приватного ключа из файла
with open("priv_key.txt", "r") as priv_key_file:
    private_key_input = priv_key_file.read().strip()
private_key_bytes = base58.b58decode(private_key_input)
keypair = Keypair.from_bytes(private_key_bytes)

# Получение адреса получателя из приватного ключа
receiver_address = keypair.pubkey()
print(f"Адрес получателя: {receiver_address}")

def check_balance(pubkey):
    balance_resp = client.get_balance(pubkey).value
    return balance_resp  # Используем атрибут 'value' вместо индексирования

def send_transaction():
    try:
        balance_resp = client.get_balance(keypair.pubkey()).value
        balance = balance_resp  # Доступ к значению через атрибут 'value'
        if balance == 0:
            raise Exception("Недостаточно средств на счету.")

        amount_sol = random.uniform(0.01, 0.1)
        amount_lamports = int(amount_sol * 1_000_000_000)  # 1 SOL = 1 миллиард лампортов

        if amount_lamports > balance:
            raise Exception("Недостаточно средств для выполнения транзакции.")

        # Получение недавнего blockhash
        latest_blockhash_resp = client.get_latest_blockhash().value.blockhash
        latest_blockhash = latest_blockhash_resp

        # Создание транзакции
        transaction = Transaction()
        transaction.add(transfer(
            TransferParams(
                from_pubkey=keypair.pubkey(),
                to_pubkey=receiver_address,
                lamports=amount_lamports
            )
        ))
        transaction.recent_blockhash = latest_blockhash
        transaction.fee_payer = keypair.pubkey()
        transaction.sign(keypair)  # Передаем объект Keypair, а не список

        # Отправка транзакции
        response = client.send_raw_transaction(transaction.serialize())
        print(f"Отправлено {amount_sol} SOL. Ответ сервера: {response}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Основной цикл
try:
    while True:
        for _ in range(100):
            send_transaction()
            time.sleep(random.randint(5, 15))
        print("Цикл завершен. Пауза на 24 часа.")
        time.sleep(24 * 60 * 60)  # Пауза на 24 часа
except KeyboardInterrupt:
    print("Бот остановлен.")
