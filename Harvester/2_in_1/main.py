# === СТАНДАРТНЫЕ БИБЛИОТЕКИ ===
import os
import re
import sys
import json
import time
import signal
import logging
import threading
import datetime

from threading import Thread

# === СТОРОННИЕ БИБЛИОТЕКИ ===
import requests
import schedule

# === ЛОКАЛЬНЫЕ ИМПОРТЫ ===
from config.settings import LOCK_FILE
from utils import logger
from utils.scheduler import run_scheduler

# === ОТКЛЮЧЕНИЕ ЛОГОВ discord.py ===
for logger_name in ["discord", "discord.client", "discord.gateway", "discord.http"]:
    log = logging.getLogger(logger_name)
    log.setLevel(logging.WARNING)                      # Показывать только важное
    log.propagate = False

# === ИМПОРТ БОТОВ ===
from dc_bot import run_discord_bot
from tg_bot import run_telegram_bot

# === ГЛОБАЛЬНОЕ СОБЫТИЕ ДЛЯ ОСТАНОВКИ ===
stop_event = threading.Event()

# === ОБРАБОТЧИК Ctrl+C ===
def handle_sigint(sig, frame):
    answer = input(
        "\n[MAIN] Вы уверены, что хотите остановить бота? [Y/n]: "
    ).strip().lower()
    if answer in ["y", "yes", ""]:
        print("[MAIN] Завершение по Ctrl + C")
        logging.info("[MAIN] Пользователь подтвердил завершение.")
        stop_event.set()
    else:
        print("[MAIN] Продолжаем работу.")

signal.signal(signal.SIGINT, handle_sigint)

# === ОБЁРТКИ ДЛЯ ПОТОКОВ ===
def discord_worker():
    try:
        logging.info("[MAIN] Запуск потока Discord-бота...")
        run_discord_bot()
    except Exception as e:
        logging.error(f"[MAIN] Поток Discord завершился с ошибкой: {e}")
        stop_event.set()

def telegram_worker():
    try:
        logging.info("[MAIN] Запуск потока Telegram-бота...")
        run_telegram_bot()
    except Exception as e:
        logging.error(f"[MAIN] Telegram бот упал: {e}", exc_info=True)
        stop_event.set()

# === ГЛАВНЫЙ ЗАПУСК ===
def main():
    logging.info("[MAIN] Запуск объединённого бота...")

    # Запускаем расписание
    schedule_thread = threading.Thread(target=run_scheduler, daemon=True)

    # Запускаем ботов
    discord_thread = threading.Thread(target=discord_worker)
    telegram_thread = threading.Thread(target=telegram_worker)

    schedule_thread.start()
    discord_thread.start()
    telegram_thread.start()

    try:
        while not stop_event.is_set():
            time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
    finally:
        logging.info("[MAIN] Бот завершает работу...")
        discord_thread.join(timeout=5)
        telegram_thread.join(timeout=5)

        # Удаление LOCK-файла
        if os.path.exists(LOCK_FILE):
            os.remove(LOCK_FILE)
            logging.info("[TG] Lock-файл удалён. Telegram бот завершил работу.")
        
        logging.info("[MAIN] Бот завершил работу корректно.")

if __name__ == "__main__":
    main()
