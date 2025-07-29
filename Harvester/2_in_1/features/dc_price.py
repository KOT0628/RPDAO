import os
import aiohttp
import logging

import discord
import requests

from discord.ext import commands

from config.settings import (
    GUILD_ID,
    BTC_CHANNEL_ID,
    COMMAND_CHANNEL_ID,
    BACKGROUND_PATH,
    FONT_PATH,
)
from utils.image import create_price_image
import utils.dc_helpers as helpers

# === ПОЛУЧЕНИЕ ЦЕНЫ BTC ===
async def get_btc_price():
    # == Основной источник: CoinGecko ==
    coingecko_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(coingecko_url, timeout=10) as response:
                if response.status != 200:
                    raise Exception(f"Код ответа: {response.status}")
                data = await response.json()
                if "bitcoin" in data and "usd" in data["bitcoin"]:
                    return round(data["bitcoin"]["usd"], 2)
                else:
                    logging.warning(
                        f"[DC_PRICE] CoinGecko вернул неожиданный ответ: {data}"
                    )
    except Exception as e:
        logging.warning(f"[DC_PRICE] Ошибка CoinGecko: {e}")

    # == Резервный источник: MEXC ==
    mexc_url = "https://api.mexc.com/api/v3/ticker/price?symbol=BTCUSDT"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(mexc_url, timeout=10) as response:
                if response.status != 200:
                    raise Exception(f"Код ответа: {response.status}")
                data = await response.json()
                if "price" in data:
                    return round(float(data["price"]), 2)
                else:
                    logging.warning(
                        f"[DC_PRICE] MEXC вернул неожиданный ответ: {data}"
                    )
    except Exception as e:
        logging.error(f"[DC_PRICE] Ошибка MEXC: {e}")

    # В случае полной неудачи
    return None

# === ОБНОВЛЕНИЕ НАЗВАНИЯ КАНАЛА BTC ===

...

# === СЛЭШ-КОМАНДА /price ===

...

__all__ = [
    "register_price_command",
    "update_btc_channel_name",
]
