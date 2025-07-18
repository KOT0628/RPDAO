import time
import logging

import schedule

from features.price import send_price_image
from utils.logger import clear_log_file
from utils.translate import clear_log_file_translate

# === НАСТРОЙКА РАСПИСАНИЯ ===
# == Отправка цены BTC 1 раз в 4 часа ==
schedule.every(4).hours.do(send_price_image)

# == Очистка logs.txt раз в 3 дня ==
schedule.every(3).days.do(clear_log_file)

# == Очистка translate.txt раз в 3 дня ==
schedule.every(3).days.do(clear_log_file_translate)

# === ЗАПУСК ПЛАНИРОВЩИКА ==
def run_scheduler():
    logging.info("[SCHEDULER] Планировщик запущен.")
    while True:
        schedule.run_pending()
        time.sleep(1)

__all__ = ["run_scheduler"]
