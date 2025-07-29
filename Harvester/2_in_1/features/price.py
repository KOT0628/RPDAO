import os
import logging

import requests

from requests.exceptions import ReadTimeout

from config.settings import CHAT_ID, BTC_IMAGE_OUTPUT
from utils.helpers import (
    delete_command_after,
    safe_delete_message,
    require_bot_active,
)
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
    # == Основной источник: CoinGecko ==
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = data.get("bitcoin", {}).get("usd")
        if price is not None:
            return round(price, 2)
        logging.warning("[TG_PRICE] CoinGecko вернул пустой ответ")
    except Exception as e:
        logging.error(f"[TG_PRICE] Ошибка при запросе CoinGecko: {e}")

    # == Резервный источник: MEXC ==
    try:
        url = "https://api.mexc.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = float(data.get("price"))
        return round(price, 2)
    except Exception as e:
        logging.error(f"[TG_PRICE] Ошибка при запросе MEXC: {e}")

    # В случае полной неудачи
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
