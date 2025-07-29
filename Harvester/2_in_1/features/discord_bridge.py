import os
import logging
import tempfile

import requests

from requests.exceptions import ReadTimeout

from discord_webhook import DiscordWebhook

from config.settings import CHAT_ID, DISCORD_WEBHOOK_URL, DISCORD_AVATAR_URL
from utils.helpers import escape_md, is_recent
from utils.translate import translate_smart

# === ВНЕШНИЕ УСТАНОВКИ ===
# == Установка бота ==
def set_bot(b):
    global bot
    bot = b

# === МОСТ TELEGRAM -> DISCORD ===
# == Пересылка текста в Discord ==

...

# == Пересылка фото с подписью ==

...

# == Обработка текста ==

...

# == Обработка фото ==

...

__all__ = [
    "set_bot",
    "send_to_discord",
    "send_photo_to_discord",
    "send_text",
    "send_photo"
]
