## 📚 Оглавление

* [🔴 Red Planet Harvester Bot](#-red-planet-harvester-bot)
* [📦 Функционал и возможности](#-функционал-и-возможности)

  * [🟣 Telegram](#-telegram)
  * [🔵 Discord](#-discord)
  * [🔴 Общие функции](#-общие-функции)
  
* [📚 Поддерживаемые команды](#-поддерживаемые-команды)

  * [🟣 Telegram](#-telegram-1)
  * [🔵 Discord](#-discord-1)
  
* [🛠 Требования](#-требования)
* [🔧 Установка](#-установка)

  * [🗂 Структура проекта](#-1-структура-проекта)
  * [🌐 Установка виртуального окружения для Windows](#-2-установка-виртуального-окружения-для-windows)
  * [📥 Установка зависимостей](#-3-установка-зависимостей)
  * [🔐 Создание .env](#-4-создай-env-файл-со-следующими-переменными)
  * [📂 Вспомогательные файлы](#-5-вспомогательные-файлы)
  
* [🛠️ Используемые технологии](#️-используемые-технологии)
* [📷 Скриншоты](#-скриншоты)
* [🚀 Запуск](#-запуск)
* [🧹 Завершение работы](#-завершение-работы)
* [⚠️ Примечания](#️-примечания)
* [👤 Автор](#-автор)
* [📝 Лицензия](#-лицензия)

---

# 🔴 Red Planet Harvester Bot (Разработка прекращена)

> ***Red Planet Harvester*** - *это многофункциональный, универсальный бот для сообщества Red Planet DAO, объединяющий возможности Telegram и Discord в одном скрипте.*

Этот бот автоматически:

- отправляет сгенерированное изображение с текущей ценой Bitcoin в [Telegram](https://t.me/rpdao) и [Discord](https://discord.gg/g4b8RsbnNd) **"Red Planet DAO"** каждые 4 часа;
- обрабатывает слэш-команды: `/price`, `/roll`, `/reroll`, `/gm`, `/gn`, `/rpdao_game` `/crimson_board`, `/link`;
- пересылает все сообщения и изображения **из Telegram в Discord**, с автоматическим переводом на английский язык;
- пересылает все сообщения и изображения **из Discord в Telegram**;
- поддерживает ретрансляцию твитов **с Twitter в Discord**.

---

## 📦 Функционал и возможности

### 🟣 **Telegram:**

- 🕓 Автоматическая публикация изображения с ценой $BTC каждые 4 часа
- 💬 Пересылка всех сообщений и изображений из Telegram в Discord (с переводом на английский)
- 🎮 Игровая зона:
  - 🎲 мини-игра `ROLL` - случайное число от 0 до 100, используя `/roll`
  - 🎰 мини-игра `"Камень, ножницы, бумага"`, используя `/reroll`
  - 🧠 викторина `TRIVIA` с автоматическими подсказками и двумя режимами игры:
    - **Рандомный режим** - вопрос приходит через 30-90 минут после предыдущего правильного ответа.  
	- **Фиксированный режим** - строгий 60-секундный интервал между раундами.
  - 🏆 просмотр таблицы лидеров (с навигацией по страницам):
    - 📤 в общем чате
	- 📬 в личных сообщениях
- 🏆 Лидерборд Crimson Envoys:
  - `/crimson_board` — просмотр таблицы лидеров Алых Посланников (с навигацией по страницам):
    - 📤 в общем чате
	- 📬 в личных сообщениях
- 🔗 Ссылки на социальные сети Red Planet DAO:
  - `/link` - просмотр оффициальных ссылок Red Planet DAO:
    - 📤 в общем чате
	- 📬 в личных сообщениях
- 🛡️ Защита:
  - от старых сообщений (не реагирует на устаревшие)
  - от двойного запуска через `bot.lock`
- 📝 Логирование переводчика:
  - в файл `translate.txt` (автоматическая очистка каждые 3 дня)

- 📤 CLI-бот для Telegram:
  - 💬 многострочный ввод
  - 📷 фото и 📹 видео
  - 📁 выбор последних файлов
  - 📌 закрепление
  - 🧾 ответ на сообщение
  - 📦 drag-and-drop

### 🔵 **Discord:**

- 📈 Автообновление цены Bitcoin через API CoinGecko:
  - отображение её в названии голосового канала
  - 🟢🔴 эмоджи и стрелки в зависимости от изменения цены
- 🎲 Команда `/roll` - случайное число от 0 до 100
- 🎰 Команда `/reroll` - мини-игра "Камень, ножницы, бумага"
- 🐦 Ретрансляция оригинальных твитов из аккаунта Twitter в канал Discord:
  - 🔗 кнопки для перехода к твиту и ретвита
  - ❤️ автоматические реакции на твит
- 🔄 Пересылка сообщений и фото из Discord в Telegram
- 📬 Отправка уведомлений в Telegram о новых "Тикетах"
- 🛡️ Защита:
  - 🐦 Twitter API - многоуровневая защита от превышения лимитов:
    - ⏱️ **Ограничение частоты** - учёт времени последней удачной проверки твитов;
    - 🔁 **Автоматическая блокировка** при получении ошибки `429 Too Many Requests`;
    - 📅 **Обнаружение месячного лимита** (`Usage cap exceeded`) и отключение ретрансляции до N числа;
    - 📁 **Сохранение состояния блокировки** в файл - даже при перезапуске бот не будет использовать API до окончания периода блокировки;
	- ✅ **Восстановление доступа** после окончания временной или месячной блокировки - автоматически.

### 🔴 **Общие функции:**

- 📸 Генерация изображений:
  - `/price` - $BTC цена
  - `/gm` - доброе утро (случайная фраза, случайный фон)
  - `/gn` - спокойной ночи (случайная фраза, случайный фон)
- 📝 Логирование:
  - в один файл `logs.txt` - с ротацией по времени (1 день) и автоматическим удалением старых файлов (старше 7 дней)

---

## 👁 Поддерживаемые команды

### 🟣 **Telegram:**

| Команда             | Назначение                                        |
| ------------------- | ------------------------------------------------- |
| `/price`            | Отправляет картинку с текущей ценой BTC           |
| `/roll`             | Выдаёт случайное число от 0 до 100                |
| `/reroll`           | Камень, ножницы или бумага (эмодзи)               |
| `/gm`               | Отправляет картинку с "Добрым утром"              |
| `/gn`               | Отправляет картинку с "Доброй ночи"               |
| `/rpdao_game`       | Открывает меню "Игровой зоны"                     |
| `/crimson_board`    | Открывает таблицу лидеров Crimson Envoy           |
| `/link`             | Отправляет ссылки на социальные сети              |
| `/start_roll`       | Запускает режим турнира "ROLL"                    |
| `/stop_roll`        | Останавливает режим турнира "ROLL"                |
| `/reroll_on`        | Запускает мини-игру "Камень, ножницы, бумага"     |
| `/reroll_off`       | Останавливает мини-игру "Камень, ножницы, бумага" |
| `/rpdao_trivia`     | Запускает викторину "TRIVIA"                      |
| `/rpdao_trivia_off` | Останавливает викторину "TRIVIA"                  |
| `/score`            | Открывает таблицу лидеров "Игровой зоны"          |
| `/stop`             | Отключение использования слэш-команд              |
| `/start`            | Включение использования слэш-команд               |

### 🔵 **Discord:**

| Команда   | Назначение                              |
| --------- | --------------------------------------- |
| `/price`  | Отправляет картинку с текущей ценой BTC |
| `/roll`   | Выдаёт случайное число от 0 до 100      |
| `/reroll` | Камень, ножницы или бумага (эмодзи)     |

---

## 🛠 Требования

- Python 3.8+
- Telegram Bot Token
- Discord Bot Token
- Twitter API Token
- DeepL API Token
- GoogeCloud Translate API Token

---

## 🔧 Установка

### 🗂 **1. Структура проекта**

```
RPDAO-Harvester_v2.0/
│
├── __init__.py
├── main.py                            # Главная точка входа
├── tg_bot.py                          # Запуск Telegram бота
├── dc_bot.py                          # Запуск Discord бота
│
├── console_sender.py                  # CLI-бот для Telegram
│
├── config/                            # Конфигурации
│   ├── __init__.py
│   └── settings.py                    # Загрузка переменных окружения
│
├── utils/                             # Вспомогательные функции
│   ├── __init__.py
│   ├── check_admin.py                 # Проверка прав администратора
│   ├── dc_helpers.py                  # Экранирование, сохранение последнего твита и др.
│   ├── helpers.py                     # Экранирование, удаление сообщений и др.
│   ├── image.py                       # Генерация изображений
│   ├── logger.py                      # Настройка логирования
│   ├── message_map.py                 # Маппинг сообщений Discord - Telegram
│   ├── scheduler.py                   # Планировщик schedule
│   ├── scoreboard.py                  # Формирование Leaderboard
│   ├── telegram_notify.py             # Отправка оповещения о новом "тикете" в Telegram
│   ├── translate.py                   # Универсальный переводчик
│   └── tweets_guard.py                # Контроль частоты обращений к Twitter API
│
├── features/                          # Основной функционал
│   ├── game/                          # Игры в чате Red Planet DAO
│   │   ├── __init__.py 
│   │   ├── dc_reroll.py               # Discord команда /reroll
│   │   ├── dc_roll.py                 # Discord команда /reroll
│   │   ├── game_menu.py               # Модуль игрового меню
│   │   ├── game_state.py              # Модуль состояния режима Reroll
│   │   ├── handlers.py                # Общий фасад для Roll, Reroll и TRIVIA
│   │   ├── reroll.py                  # Логика Reroll
│   │   ├── roll.py                    # Логика Roll
│   │   └── trivia.py                  # Логика викторины
│   ├── __init__.py
│   ├── crimson_board.py               # Логика Crimson Envoy Leaderboard
│   ├── dc_price.py                    # Discord команда /price
│   ├── discord_bridge.py              # Пересылка сообщений и фото в Discord
│   ├── gm_gn.py                       # Telegram команды /gm и /gn
│   ├── link.py                        # Команда /link
│   ├── price.py                       # Telegram команда /price
│   ├── score.py                       # Логика Game Leaderboard
│   ├── stop_start.py                  # Отключение/включение использования слэш-команд
│   ├── telegram_bridge.py             # Пересылка сообщений и фото в Telegram
│   ├── ticket_notify.py               # Обработка создания нового канала с "тикетом"
│   └── tweets.py                      # Ретрансляция твитов с Twitter в Discord
│
├── assets/
│   ├── backgrounds/
│   │   ├── morning/                   # Фоны для /gm
│   │   │   ├── 1.jpg
│   │   │   ├── 2.jpg
│   │   │   ├── 3.jpg
│   │   ├── night/                     # Фоны для /gn
│   │   │   ├── 1.jpg
│   │   │   ├── 2.jpg
│   │   │   ├── 3.jpg
│   │   └── background.jpg             # Фон для /price
│   ├── fonts/
│   │   └── SpicyRice-Regular.ttf      # Шрифт
│   ├── game_zone.jpg                  # Фон для основного меню "Игровой зоны"
│   ├── leaderboard.jpg                # Фон подменю "Игровой зоны"
│   ├── link.png                       # Фон для меню ссылок на соц.сети
│   ├── reroll.jpg                     # Фон подменю "Игровой зоны"
│   ├── roll.jpg                       # Фон подменю "Игровой зоны"
│   └── trivia.txt                     # Фон подменю "Игровой зоны"
│
├── data/
│   ├── discord/
│   │   ├── last_price.txt             # Последняя цена $BTC
│   │   └── message_map.json           # Файл маппинга сообщений
│   ├── game/
│   │   └── trivia_questions.txt       # Вопросы для викторины
│   ├── img_output/
│   │   ├── btc_price_output.jpg       # Сгенерированное изображение с ценой $BTC
│   │   ├── gm_output.jpg              # Сгенерированное изображение "Доброе утро"
│   │   └── gn_output.jpg              # Сгенерированное изображение "Доброй ночи"
│   ├── leadeboard/
│   │   ├── crimson_scores.json        # Таблица лидеров Crimson Envoy
│   │   └── scores.json                # Таблица лидеров "Игровой зоны"
│   ├── logs/
│   │   ├── logs.log                   # Файл логов
│   │   └── translate.log              # Файл логов переводчика
│   ├── secrets/
│   │   └── google_key.json            # GoogleCloud Translate API ключ
│   └── twitter/
│       ├── last_tweet.txt             # Последний ретранслируемый твит
│       ├── last_twitter_check.txt     # Содержит время последней успешной проверки Twitter
│       ├── twitter_block.txt          # Содержит время окончания временной блокировки API
│       └── twitter_disabled.txt       # Содержит информацию о состоянии блокировки API
│
└── requirements.txt                   # Список зависимостей
```
### 🌐 **2. Установка виртуального окружения для Windows**

- 2.1. 📁 Перейди в папку проекта

Открой терминал (например, PowerShell или CMD) и перейди туда, где лежит твой проект:

```powershell
cd путь\к\твоему\проекту
```

Например:

```powershell
cd "G:\My disc\Cosmos Ecosystem\RPDAO_Bot"
```

- 2.2. 🐍 Убедись, что установлен Python

Проверь:

```powershell
python --version
```

Если не установлен - [скачай и установи Python 3.10+ с python.org](https://www.python.org/downloads/windows/), не забудь поставить галочку **"Add Python to PATH"** при установке.

- 2.3. 🌱 Создай виртуальное окружение

```powershell
python -m venv venv
```

После этого появится папка `venv/` внутри проекта - в ней будет всё изолировано.

- 2.4. ▶️ Активируй окружение

```powershell
venv\Scripts\activate
```

После активации ты увидишь в начале строки терминала `(venv)` - это значит, окружение активно.

### 📥 **3. Установка зависимостей:**

```bash
pip install -r requirements.txt
```

Содержимое `requirements.txt`:
```
Pillow==10.4.0
psutil==5.9.8
python-dotenv==1.0.1
requests==2.31.0
schedule==1.2.1
word2number==1.1

python-telegram-bot>=20.0,<21.0

pyTelegramBotAPI==4.15.4
wcwidth>=0.2.6

discord.py==2.3.2
discord-webhook==1.1.0
PyNaCl>=1.5.0,<1.6.0

aiohttp>=3.9.0
async_lru>=2.0.4
oauthlib>=3.2.2
tweepy==4.16.0

deepl==1.15.0
deep-translator==1.11.4
google-cloud-translate>=3.0.2
langdetect==1.0.9
```

### 🔐 **4. Создай `.env` файл со следующими переменными:**

| Переменная                       | Описание                                      |
|----------------------------------|-----------------------------------------------|
| `TELEGRAM_TOKEN`                 | Telegram токен бота                           |
| `CHAT_ID`                        | ID Telegram чата                              |
| `DISCORD_TOKEN`                  | Discord токен бота                            |
| `GUILD_ID`                       | ID вашего Discord сервера                     |
| `COMMAND_CHANNEL_ID`             | ID канала для использования команд            |
| `GAME_CHANNEL_ID`                | ID канала для исползования игровых команд     |
| `DISCORD_CHANNEL_ID`             | ID канала для пересылки сообщений             |
| `BTC_CHANNEL_ID`                 | ID канала для отображения цены                |
| `TWITTER_CHANNEL_ID`             | ID канала для твитов                          |
| `TWITTER_BEARER`                 | Bearer Token для Twitter API                  |
| `TWITTER_USER_ID`                | ID профиля Twitter                            |
| `DISCORD_WEBHOOK_URL`            | Discord Webhook URL (для пересылки в Discord) |
| `DEEPL_API_KEY`                  | API ключ переводчика DeepL                    |
| `GOOGLE_APPLICATION_CREDENTIALS` | API ключ GoogleCloud переводчика              |
| `DISCORD_AVATAR_URL`             | URL аватарки для бота                         |

```env
# Telegram
TELEGRAM_TOKEN=your_telegram_token
CHAT_ID=-100xxxxxxxxxx

# Discord
DISCORD_TOKEN=your_discord_token
GUILD_ID=discord_guild_id
COMMAND_CHANNEL_ID=discord_use_command_channel_id
GAME_CHANNEL_ID=discord_use_game_command_channel_id
DISCORD_CHANNEL_ID=discord_bridge_channel_id
BTC_CHANNEL_ID=discord_btc_channel_id
TWITTER_CHANNEL_ID=discord_twitter_channel_id

# Twitter
TWITTER_BEARER=your_twitter_bearer_token
TWITTER_USER_ID=twitter_user_id

# Webhook (TG -> DC)
DISCORD_WEBHOOK_URL=discord_webhook_url

# Deepl (перевод)
DEEPL_API_KEY=deepl_api_key
GOOGLE_APPLICATION_CREDENTIALS=data/secrets/google_key.json

# Прочее
DISCORD_AVATAR_URL=your_avatar_url
```

### 📂 **5. Вспомогательные файлы:**

| Файл                     | Назначение                                                          |
| ------------------------ | ------------------------------------------------------------------- |
| `background.jpg`         | фон для изображения с ценой                                         |
| `morning1-6.jpg`         | фоны для изображения "Доброе утро"                                  |
| `night1-6.jpg`           | фоны для изображения "Доброё ночи"                                  |
| `game_zone.jpg`          | фон для основного меню "Игровой зоны"                               |
| `roll.jpg`               | фон для подменю `ROLL`                                              |
| `reroll.jpg`             | фон для подменю `REROLL`                                            |
| `trivia.jpg`             | фон для подменю `TRIVIA`                                            |
| `leaderboard.jpg`        | фон для подменю `LEADERBOARD`                                       |
| `SpicyRice-Regular.ttf`  | кастомный шрифт для текста                                          |
| `last_price.txt`         | кэш последней цены BTC (создаётся автоматически)                    |
| `last_tweet.txt`         | кэш последнего отправленного твита (создаётся автоматически)        |
| `last_twitter_check.txt` | время последней успешной проверки Twitter (создаётся автоматически) |
| `twitter_block.txt`      | время окончания временной блокировки API (создаётся автоматически)  |
| `logs.log`               | общий лог-файл бота (создаётся автоматически)                       |
| `translate.log`          | лог-файл переводчика (создаётся автоматически)                      |
| `trivia_questions.txt`   | вопросы для викторины `TRIVIA`                                      |
| `scores.json.`           | файл таблицы лидеров "Игровой зоны" (создаётся автоматически)       |
| `crimson_scores.json`    | файл таблицы лидеров "Crimson Envoy"                                |
| `message_map.json`       | файл маппинга сообщений (создаётся автоматически)                   |
| `.env`                   | конфигурация токенов и ID                                           |
| `google_key.json`        | API ключ GoogleCloud Translate                                      |
| `requirements.txt`       | список зависимостей Python                                          |

---

## 🛠️ Используемые технологии

- [os](https://docs.python.org/3/library/os.html) встроенный модуль Python для работы с операционной системой (файлы, переменные окружения, процессы)  
- [sys](https://docs.python.org/3/library/sys.html) встроенный модуль Python для доступа к системным параметрам и взаимодействия с интерпретатором  
- [re](https://docs.python.org/3/library/re.html) встроенный модуль Python для работы с регулярными выражениями  
- [time](https://docs.python.org/3/library/time.html) встроенный модуль Python для работы со временем и задержками  
- [uuid](https://docs.python.org/3/library/uuid.html) встроенный модуль Python для генерации уникальных идентификаторов (UUID)  
- [json](https://docs.python.org/3/library/json.html) встроенный модуль Python для кодирования и декодирования JSON-данных  
- [random](https://docs.python.org/3/library/random.html) встроенный модуль Python для генерации случайных чисел и выборок  
- [logging](https://docs.python.org/3/library/logging.html) встроенный модуль Python для ведения логов в приложениях  
- [threading](https://docs.python.org/3/library/threading.html) встроенный модуль Python для многопоточности  
- [tempfile](https://docs.python.org/3/library/tempfile.html) встроенный модуль Python для создания временных файлов и директорий  
- [datetime](https://docs.python.org/3/library/datetime.html) встроенный модуль Python для работы с датами и временем  
- [discord.py](https://discordpy.readthedocs.io/en/stable/) библиотека Python для взаимодействия с Discord API  
- [discord.ui](https://discordpy.readthedocs.io/en/stable/interactions/api.html#module-discord.ui) модуль для создания кнопок и интерактивных элементов в Discord  
- [discord.ext](https://discordpy.readthedocs.io/en/stable/ext/commands/index.html) расширение библиотеки `discord.py`, предоставляющее систему команд для создания Discord-ботов  
- [Tweepy](https://docs.tweepy.org/en/stable/) библиотека Python для работы с Twitter API  
- [aiohttp](https://pypi.org/project/aiohttp/) библиотека Python для выполнения асинхронных HTTP-запросов, основанная на asyncio. Используется для высокопроизводительного взаимодействия с API, включая работу с Twitter через Tweepy  
- [async_lru](https://pypi.org/project/async-lru/) асинхронная реализация LRU (Least Recently Used) кэширования для Python-функций. Позволяет кешировать результаты асинхронных вызовов, снижая нагрузку и ускоряя повторные запросы  
- [oauthlib](https://pypi.org/project/oauthlib/) библиотека Python, реализующая протоколы OAuth 1.0 и OAuth 2.0. Обеспечивает безопасную авторизацию и аутентификацию при работе с API, включая Twitter API через Tweepy  
- [aiohttp](https://docs.aiohttp.org/en/stable/) асинхронная библиотека Python для работы с HTTP  
- [asyncio](https://docs.python.org/3/library/asyncio.html) стандартный модуль Python для асинхронного программирования  
- [requests](https://pypi.org/project/requests/) библиотека Python для выполнения HTTP-запросов  
- [Pillow](https://pillow.readthedocs.io/en/stable/) библиотека для обработки изображений в Python  
- [psutil](https://psutil.readthedocs.io/en/latest/) библиотека Python для получения информации о системных ресурсах (CPU, память, диски, сеть) и управления процессами  
- [schedule](https://schedule.readthedocs.io/en/stable/) библиотека Python для простого планирования периодических задач с помощью понятного синтаксиса  
- [python-dotenv](https://saurabh-kumar.com/python-dotenv/) библиотека Python для загрузки переменных окружения из файла `.env` в переменные окружения системы  
- [python-telegram-bot](https://docs.python-telegram-bot.org/) библиотека Python для создания ботов Telegram с поддержкой асинхронности, удобных хендлеров и взаимодействия с Telegram Bot API  
- [pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/) простая библиотека Python для создания ботов Telegram с синхронным и удобным API на основе [telebot](https://github.com/eternnoir/pyTelegramBotAPI)  
- [telebot](https://pypi.org/project/pyTelegramBotAPI/) библиотека Python (часть `pyTelegramBotAPI`) для создания Telegram-ботов  
- [discord-webhook](https://pypi.org/project/discord-webhook/) простая библиотека Python для отправки сообщений через Discord Webhooks  
- [word2number](https://pypi.org/project/word2number/) библиотека Python для преобразования чисел, записанных словами (например, "two hundred"), в числовой формат (`200`)  
- [PyNaCl](https://pynacl.readthedocs.io/) Python-биндинг к библиотеке [NaCl](https://nacl.cr.yp.to/), реализующий современные криптографические функции (например, цифровые подписи, шифрование и т.д.)  
- [CoinGecko API](https://www.coingecko.com/en/api) бесплатный API для получения информации о криптовалютах  
- [DeepL API](https://www.deepl.com/docs-api) интерфейс программирования от DeepL для автоматического перевода текста с поддержкой высококачественных переводов  
- [deepl](https://pypi.org/project/deepl/) официальная библиотека Python для работы с DeepL API — одного из самых качественных сервисов машинного перевода текста  
- [Google Cloud Translation API](https://cloud.google.com/translate) API от Google для перевода текста. Поддерживает автоматическое определение языка, настройку терминологии и интеграцию в веб- и мобильные приложения
- [google-cloud-translate](https://cloud.google.com/python/docs/reference/translate/latest) официальная библиотека Python для использования Google Cloud Translation API для автоматического перевода текста  
- [deep-translator](https://deep-translator.readthedocs.io/en/latest/) универсальная библиотека Python для перевода текста с поддержкой нескольких сервисов, включая Google Translate, DeepL, Microsoft Translator и другие  
- [langdetect](https://pypi.org/project/langdetect/) библиотека Python для автоматического определения языка текста на основе алгоритмов Google Language Detection  

---

## 📷 Скриншоты

---

## 🚀 Запуск

```powershell
python main.py
```

### **Бот начнёт работу и будет:**

- каждые 10 минут обновлять название канала в **Discord** с текущей ценой $BTC  
- каждые 30 минут проверять наличие нового твита для ретрансляции в Discord  
- отслеживать создание новых "тикетов" и отправлять уведомление в Telegram  
- каждые 4 часа публиковать изображение с ценой $BTC в **Telegram**  
- реагировать на обработку слэш-команд:  
  - **Telegram** `/price`, `/gm`, `/gn`, `/rpdao_game`, `/crimson_board`, `/link`, `/start_roll` / `/roll` / `/stop_roll`, `/reroll_on` / `/reroll` / `/reroll_off`, `/rpdao_trivia` / `/rpdao_trivia_off`, `/score`, `/stop` / `/start`  
  - **Discord** `/price`, `/roll`, `/reroll`  
- автоматически пересылать все сообщений и фото в **Discord** с переводом на английский  
- автоматически пересылать все сообщений и фото в **Telegram**  
- мини-игры в **Telegram**: раунды `/roll`, турниры `/reroll` и викторину `/rpdao_trivia`  

---

## 🧹 Завершение работы

При завершении скрипта автоматически удаляется `bot.lock`, чтобы **Telegram** бот мог быть перезапущен без конфликтов.

---

## ⚠️ Примечания

- Если бот не отвечает - проверь лог `entrypoint.log` или `logs.log`.
- Убедись, что переменные окружения заданы корректно.
- Если бот запускается в группе, добавь его как администратора с правами на удаление, закрепление и отправку сообщений и медиа.

---

## 👤 Автор

Создано с ❤️ для [Red Planet DAO](https://linktr.ee/rpdao)  
Автор: [KOT](https://github.com/KOT0628)

---

## 📝 Лицензия

©️ RPDAO
