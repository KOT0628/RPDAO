import time
import logging

import schedule

from utils.logger import clear_log_file

# === НАСТРОЙКА РАСПИСАНИЯ ===
# == Очистка logs.txt раз в 3 дня ==
schedule.every(3).days.do(clear_log_file)

# === ЗАПУСК ПЛАНИРОВЩИКА ==
def run_scheduler():
    logging.info("[SCHEDULER] Планировщик запущен.")
    while True:
        schedule.run_pending()
        time.sleep(1)

__all__ = ["run_scheduler"]
