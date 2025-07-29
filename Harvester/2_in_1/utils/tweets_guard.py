import os
import time
import logging

TWITTER_TIMESTAMP_FILE = "data/twitter/last_twitter_check.txt"
TWITTER_BLOCK_FILE = "data/twitter/twitter_block.txt"
TWITTER_DISABLED_FILE = "data/twitter/twitter_disabled.txt"

# === ПРОВЕРКА ИНТЕРВАЛА МЕЖДУ ЗАПРОСАМИ ===

...

    # Проверка временной блокировки (например, при TooManyRequests)

    ...

    # Проверка интервала последней проверки

    ...

# == Сохраняем успешную проверку ==

...

# === БЛОКИРОВКА ПРИ ПРЕВЫШЕНИИ ЛИМИТА ===

...

# === ПРОПУСК ЗАПРОСА, ЕСЛИ НЕ ТРЕБУЕТСЯ ===

...

# === ЗАГРУЗКА СОСТОЯНИЯ БЛОКИРОВКИ TWITTER ===

...

__all__ = [
    "allow_check",
    "mark_checked",
    "block_due_to_limit",
    "should_skip_fetch",
]
