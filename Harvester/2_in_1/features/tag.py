import os
import json
import time
import logging

from config.settings import CHAT_ID
from utils.helpers import delete_command_after, require_bot_active

USERNAMES_FILE = "data/game/active_users.json"

# === Установка бота ===
def set_bot(b):
    global bot
    bot = b

# === Загрузка списка никнеймов ===
def load_usernames(path=USERNAMES_FILE):
    ...

# === Обработчик команды /tag ===
def tag(bot):
    ...

# === Объединим функции set_bot, tag ===
def tag_handlers(bot):
    set_bot(bot)
    tag(bot)

__all__ = ["tag_handlers"]
