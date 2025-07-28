import re
import logging

import requests

from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from utils.helpers import escape_markdown
from utils.message_map import save_mapping, get_telegram_reply_id

# === ПЕРЕСЫЛКА СООБЩЕНИЙ В TELEGRAM ===
# == Пересылка текстового сообщения ==

...

# == Пересылка фото с подписью ==

...

# === ОБРАБОТКА СООБЩЕНИЙ ДЛЯ ПЕРЕСЫЛКИ В TELEGRAM ===

...

__all__ = ["register_tg_bridge_command"]
