# 🔴 Red Planet Telegram Bot

Этот бот автоматически:
- отправляет изображение с текущей ценой Bitcoin в Telegram-чат Red Planet DAO каждые 4 часа,
- обрабатывает команды `/price`, `/rpdao_trivia`, `/roll`, `/reroll`, `/score`, `/gm`, `/gn`, `/start_roll` / `/stop_roll`, `/reroll_on`/ `/reroll_off`, `/rpdao_trivia_off`
- пересылает все сообщения и изображения из Telegram в Discord.

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

1. Клонируй репозиторий или скачай скрипт:

```bash
git clone https://github.com/KOT0628/RPDAO-TG-bot.git
cd rpdao-btc-bot
```

2. Установи зависимости:

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

3. Создай `.env` файл со следующими переменными:

```env
TELEGRAM_TOKEN=your_telegram_bot_token
CHAT_ID=-100xxxxxxxxxx
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
DISCORD_AVATAR_URL=your_avatar_url
DEEPL_API_KEY=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx:fx
```

4. Помести в корень проекта файлы:

 - `background.jpg`          # для /price
 - `morning.jpg`             # для /gm
 - `night.jpg`               # для /gn
 - `SpicyRice-Regular.ttf`   # шрифт
 - `trivia_questions.txt`    # вопросы для викторины

---

## 🚀 Запуск

```bash
python btc_bot.py
```

Бот начнёт работу и будет:
- каждые 4 часа публиковать изображение с ценой $BTC,
- реагировать на обработку команд `/price`, `/rpdao_trivia_off`, `/score`, `/gm`, `/gn`, `/start_roll` / `/stop_roll`, `/reroll_on`/ `/reroll_off`,
- автоматически пересылать все сообщений и фото в Discord с переводом на английский,
- мини-игры: раунды `/roll`, турниры `/reroll` и викторину `/rpdao_trivia`.

---

## 🗂 Структура проекта

```
project/
├── background.jpg            # Фон для BTC
├── morning.jpg               # Фон для доброго утра
├── night.jpg                 # Фон для спокойной ночи
├── SpicyRice-Regular.ttf     # Шрифт
├── btc_bot.py                # Основной код бота
├── translate.py              # Модуль перевода на английский
├── .env                      # Переменные окружения
├── logs.txt                  # Логи
├── scores.json               # Таблица лидеров (автоматически)
├── trivia_questions.txt      # Вопросы для викторины
└── requirements.txt          # Зависимости
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
