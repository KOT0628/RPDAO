import os
import logging

import requests

from requests.exceptions import ReadTimeout

from config.settings import CHAT_ID, BTC_IMAGE_OUTPUT
from utils.helpers import delete_command_after, safe_delete_message
from utils.image import create_price_image

# === ВНЕШНИЕ УСТАНОВКИ ===
# == Глобальные переменные ==
bot = None

# == Установка бота ==
def set_bot(b):
    global bot
    bot = b

# === ПОЛУЧЕНИЕ ЦЕНЫ BTC ===
def get_btc_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            logging.error(f"Ошибка ответа CoinGecko: {response.status_code}")
            return 0.0
        data = response.json()
        price = data.get("bitcoin", {}).get("usd")
        if price is None:
            logging.warning("Цена BTC не найдена в ответе CoinGecko")
            return 0.0
        return round(price, 2)
    except Exception as e:
        logging.error(f"Ошибка при получении цены BTC: {e}")
        return 0.0

# === ОТПРАВКА ИЗОБРАЖЕНИЯ ===

...

# === ОБРАБОТЧИК КОМАНДЫ /price ===

...

__all__ = [
    "send_price_image",
    "use_price",
    "set_bot"
]
