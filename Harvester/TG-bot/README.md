# 🔴 Red Planet Telegram Bot

Этот бот автоматически:
- отправляет изображение с текущей ценой Bitcoin в Telegram-чат Red Planet DAO каждые 4 часа,
- обрабатывает команды `/price`, `/rpdao_trivia`, `/roll`, `/reroll`, `/score`, `/gm`, `/gn`, `/start_roll` / `/stop_roll`, `/reroll_on`/ `/reroll_off`, `/rpdao_trivia_off`
- пересылает все сообщения и изображения из Telegram в Discord, с автоматическим переводом на английский язык.

---

## 📦 Функционал и возможности

- 🕓 Автоматическая публикация изображения с ценой $BTC каждые 4 часа
- 💬 Пересылка всех сообщений и изображений из Telegram в Discord (с переводом на английский)
- 📸 Генерация изображений:
  - `/price` — $BTC цена
  - `/gm` — доброе утро (случайная фраза, случайный фон)
  - `/gn` — спокойной ночи (случайная фраза, случайный фон)
- 🎮 Мини-игры и интерактив:
  - `/reroll` — игра "Камень, ножницы, бумага"
  - `/roll` — случайное число от 0 до 100
- 🧠 Викторина:
  - `/rpdao_trivia` — викторина с автоматическими подсказками
- 🏆 Лидерборд:
  - `/score` — просмотр таблицы лидеров (с навигацией по страницам)
- 🛡️ Защита:
  - от старых сообщений (не реагирует на устаревшие)
  - от двойного запуска через `bot.lock`
- 📝 Логирование:
  - в файл `logs.txt` (очистка каждые 3 дня)

---

## 🛠 Требования

- Python 3.8+
- Telegram Bot Token
- Telegram Chat ID (например, `-1001234567890`)
- Discord Webhook URL (для пересылки в Discord)
- Изображения:
  - `background.jpg` — для BTC цены
  - `morning.jpg` — для команды `/gm`
  - `night.jpg` — для команды `/gn`
- Шрифт: `SpicyRice-Regular.ttf`
- Вопросы для Trivia: `trivia_questions.txt`
- Таблица лидеров: `scores.json` (создаётся автоматически)

---

## 🔧 Установка

1. Установи зависимости:

```bash
pip install -r requirements.txt
```

Содержимое `requirements.txt`:
```
pyTelegramBotAPI==4.15.4
python-dotenv==1.0.1
Pillow==10.4.0
psutil==5.9.8
schedule==1.2.1
requests==2.31.0
discord-webhook==1.1.0

deepl==1.15.0
deep-translator==1.11.4
langdetect==1.0.9
```

2. Создай `.env` файл со следующими переменными:

```env
TELEGRAM_TOKEN=your_telegram_bot_token
CHAT_ID=-100xxxxxxxxxx
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
DISCORD_AVATAR_URL=your_avatar_url
DEEPL_API_KEY=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx:fx
```

3. Вспомогательные файлы:

 - `background.jpg`          # для /price
 - `morning1-6.jpg`          # для /gm
 - `night1-6.jpg`            # для /gn
 - `SpicyRice-Regular.ttf`   # шрифт
 - `trivia_questions.txt`    # вопросы для викторины

---

## 🚀 Запуск

```bash
python main.py
```

Бот начнёт работу и будет:
- каждые 4 часа публиковать изображение с ценой $BTC,
- реагировать на обработку команд `/price`, `/rpdao_trivia_off`, `/score`, `/gm`, `/gn`, `/start_roll` / `/stop_roll`, `/reroll_on`/ `/reroll_off`,
- автоматически пересылать все сообщений и фото в Discord с переводом на английский,
- мини-игры: раунды `/roll`, турниры `/reroll` и викторину `/rpdao_trivia`.

---

## 🗂 Структура проекта

```
RPDAO-TG-bot/
│
├── __init__.py
├── main.py                            # Главная точка входа (run_bot)
│
├── config/                            # Конфигурации
│   ├── __init__.py
│   └── settings.py                    # Загрузка переменных окружения
│
├── utils/                             # Вспомогательные функции
│   ├── __init__.py
│   ├── logger.py                      # Настройка логирования
│   ├── scheduler.py                   # Планировщик schedule
│   ├── image.py                       # Генерация изображений
│   ├── helpers.py                     # Экранирование, удаление сообщений и др.
│   ├── check_admin.py                 # Проверка прав администратора
│   ├── scoreboard.py                  # Формирование Leaderboard
│   └── translate.py                   # Универсальный переводчик
│
├── features/                          # Основной функционал
│   ├── game/                          # Игры в чате Red Planet DAO
│   │   ├── __init__.py 
│   │   ├── game_state.py              # Модуль состояния режима Reroll
│   │   ├── trivia.py                  # Логика викторины
│   │   ├── roll.py                    # Логика Roll
│   │   └── reroll.py                  # Логика Reroll
│   ├── __init__.py
│   ├── price.py                       # Команда /price и изображение BTC
│   ├── gm_gn.py                       # Команды /gm и /gn
│   ├── score.py                       # Логика Leaderboard
│   └── discord_bridge.py              # Пересылка сообщений и фото в Discord
│
├── assets/
│   ├── backgrounds/
│   │   ├── morning/                   # Фоны для /gm
│   │   ├── night/                     # Фоны для /gn
│   │   └── background.jpg             # Фон для /price
│   └── fonts/
│       └── SpicyRice-Regular.ttf      # Шрифт
│
├── data/
│   ├── scores.json                    # Таблица очков
│   ├── trivia_questions.txt           # Вопросы для викторины
│   ├── translate.txt                  # Файл логов переводчика
│   └── logs.txt                       # Файл логов
│
└── requirements.txt                   # Список зависимостей

```

---

## 🧹 Завершение работы

При завершении скрипта автоматически удаляется `bot.lock`, чтобы бот мог быть перезапущен без конфликтов.

---

## ⚠️ Примечания

- Если бот не отвечает — проверь лог `logs.txt`.
- Убедись, что переменные окружения заданы корректно.
- Если бот запускается в группе, добавь его как администратора с правами на удаление и отправку сообщений и медиа.

---

## 👤 Автор

Создан с ❤️ [Red Planet DAO](https://linktr.ee/rpdao)  
Автор: [KOT0628](https://github.com/KOT0628)

---

## 📝 Лицензия

RPDAO
