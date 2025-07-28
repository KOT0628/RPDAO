import os
import logging

import discord
import requests

from discord.ext import commands

from config.settings import (
    GUILD_ID,
    BTC_CHANNEL_ID,
    BACKGROUND_PATH,
    FONT_PATH,
)
from utils.image import create_price_image
import utils.helpers as helpers

# === ПОЛУЧЕНИЕ ЦЕНЫ BTC ===

...

# === ОБНОВЛЕНИЕ НАЗВАНИЯ КАНАЛА BTC ===

...

# === СЛЭШ-КОМАНДА /price ===

...

__all__ = [
    "register_price_command",
    "update_btc_channel_name",
]
