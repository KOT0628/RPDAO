# === СТАНДАРТНЫЕ БИБЛИОТЕКИ ===
import os
import sys
import time
import logging
import threading

# === СТОРОННИЕ БИБЛИОТЕКИ ===
import psutil
import telebot

# == Telegram библиотеки ==
from telebot import TeleBot

# === ЛОКАЛЬНЫЕ ИМПОРТЫ ===
from config.settings import LOCK_FILE, TOKEN
from utils import logger
from utils.scheduler import run_scheduler
from utils import scoreboard

from features import discord_bridge, gm_gn, price, score
from features import game
from features.game import trivia

# === ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ===
# == Блокировка повторного запуска ==
def is_process_running(pid: int) -> bool:
    return psutil.pid_exists(pid)

# == Пишем текущий PID в файл ==
def write_lock_file():
    with open(LOCK_FILE, "w") as f:
        f.write(str(os.getpid()))

# = Проверяем LOCK файл =
def check_existing_instance():
    if os.path.exists(LOCK_FILE):
        with open(LOCK_FILE, "r") as f:
            try:
                pid = int(f.read())
                if is_process_running(pid):
                    logging.error(f"Бот уже запущен с PID {pid}. Выход.")
                    sys.exit(1)
                else:
                    logging.warning(
                        "Найден старый lock-файл от неактивного процесса. "
                        "Продолжаем."
                    )
            except ValueError:
                logging.warning("Поврежденный lock-файл. Продолжаем.")

# === ЗАПУСК ===
def run_bot():
    # Проверка и блокировка
    check_existing_instance()
    write_lock_file()

    # Загрузка очков
    scores = scoreboard.load_scores()

    # Инициализация бота    
    bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

    # Установка бота в модули
    game.set_bot(bot)
    game.set_save_scores(scoreboard.save_scores)
    score.register_handlers(bot)
    discord_bridge.set_bot(bot)
    discord_bridge.send_photo(bot)
    gm_gn.set_bot(bot)
    price.set_bot(bot)

    # Регистрация обработчиков
    game.register_game_handlers(bot)
    trivia.load_trivia_questions()
    gm_gn.register_handlers(bot)
    price.use_price(bot)

    # Планировщик в отдельном потоке
    threading.Thread(target=run_scheduler, daemon=True).start()

    logging.info("Бот запущен.")

    # Основной цикл polling
    while True:
        try:
            bot.remove_webhook()
            logging.info("Стартуем polling...")
            bot.polling(none_stop=True, timeout=60, long_polling_timeout=60)
        except Exception as e:
            logging.error(f"[POLLING ERROR] {e}")
            time.sleep(15)
        finally:
            if os.path.exists(LOCK_FILE):
                os.remove(LOCK_FILE)
                logging.info("Lock-файл удалён. Бот завершил работу.")


if __name__ == "__main__":
    run_bot()
