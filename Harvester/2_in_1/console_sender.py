import os
import asyncio

from asyncio import CancelledError
from pathlib import Path

from dotenv import load_dotenv

from telegram import Bot
from telegram.error import BadRequest

from config.settings import TOKEN, CHAT_ID

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

# === ОТМЕНА ОТПРАВКИ СООБЩЕИЯ ===

...

# === ОТПРАВКА СООБЩЕИЯ ===

...

# === ВЫБОР ФАЙЛА ИЗ ПАПКИ ===

...

# === КОНСОЛЬНЫЙ ВВОД ===

...

            # == Выбор последних файлов ==

            ...

            # == Ввод пути вручную, если не выбрали ==

            ...

                # поддержка drag-n-drop с кавычками

                ...

            # == Reply ID ==

            ...

            # == Закрепление ==

            ...

                # = Отправка с медиа =

                ...

                # = Отправка без медиа =

                ...

                # = Закрепить =

                ...

...

if __name__ == "__main__":
    try:
        asyncio.run(console_input())
    except KeyboardInterrupt:
        print("\n[!] Программа остановлена пользователем (Ctrl+C).")
