# 🔴 Red Planet Discord Bot (Разработка прекращена)

Многофункциональный бот для Discord, созданный для сообщества Red Planet DAO. Поддерживает:

- отображение актуальной цены BTC в названии канала,
- генерацию изображения с ценой,
- ретрансляцию твитов,
- пересылку сообщений и фото между Discord и Telegram,
- слеш-команды `/price`, `/roll`, `/reroll`.

---

## 🔧 Функционал и возможности

- 📈 Автообновление цены Bitcoin через CoinGecko и отображение её в названии голосового канала (каждые 10 минут)
- 🟢🔴 Эмоджи и стрелки в зависимости от изменения цены
- 🖼 Генерация изображения с текущей ценой BTC
- 🧵 Команда `/price` — отправляет картинку с ценой
- 🎲 Команда `/roll` — случайное число от 0 до 100
- 🎲 Команда `/reroll` — игра "Камень, ножницы, бумага"
- 🐦 Ретрансляция оригинальных твитов из аккаунта Twitter в канал Discord каждые 20 минут
- 🔗 Кнопки для перехода к твиту и ретвита
- ❤️ Автоматические реакции на твит
- 🔄 Пересылка сообщений и фото из Discord в Telegram

---

## 🛠️ Необходимые переменные окружения

Создайте файл `.env` или задайте переменные в Render:

| Переменная          | Описание                          |
|---------------------|-----------------------------------|
| `DISCORD_TOKEN`     | Discord токен бота                |
| `GUILD_ID`          | ID вашего Discord сервера         |
| `BTC_CHANNEL_ID`    | ID канала для отображения цены    |
| `TWITTER_CHANNEL_ID`| ID канала для твитов              |
| `TWITTER_BEARER`    | Bearer Token для Twitter API      |
| `TWITTER_USER_ID`   | ID профиля Twitter                |
| `TELEGRAM_TOKEN`    | Telegram токен бота               |
| `CHAT_ID`           | ID Telegram чата                  |


---

## 📂 Структура проекта

```
RPDAO-DC-bot/
│
├── __init__.py
├── main.py                            # Главная точка входа
│
├── config/                            # Конфигурации
│   ├── __init__.py
│   └── settings.py                    # Загрузка переменных окружения
│
├── utils/                             # Вспомогательные функции
│   ├── __init__.py
│   ├── logger.py                      # Настройка логирования
│   ├── scheduler.py                   # Планировщик schedule
│   ├── image.py                       # Генерация изображения
│   ├── helpers.py                     # Экранирование, сохранение последнего твита и др.
│   └── message_map.py                 # Маппинг сообщений Discord - Teegram
│
├── features/                          # Основной функционал
│   ├── __init__.py
│   ├── price.py                       # Команда /price
│   ├── roll.py                        # Команды /roll
│   ├── reroll.py                      # Команды /reroll
│   ├── telegram_bridge.py             # Пересылка сообщений и фото в Telegram
│   └── tweets.py                      # Ретрансляция твитов с Twitter в Discord
│
├── assets/
│   ├── backgrounds/
│   │   └── background.jpg             # Фон для /price
│   └── fonts/
│       └── SpicyRice-Regular.ttf      # Шрифт
│
├── data/
│   ├── message_map.json               # Файл маппинга сообщений
│   ├── last_price.txt                 # Последняя цена $BTC
│   ├── last_tweet.txt                 # Последний ретранслируемый твит
│   ├── btc_price_output.jpg           # Сгенерированное изображение с ценой $BTC
│   └── logs.txt                       # Файл логов
│
└── requirements.txt                   # Список зависимостей
```

---

## 👁 Поддерживаемые команды

| Команда   | Назначение                              |
| --------- | --------------------------------------- |
| `/price`  | Отправляет картинку с текущей ценой BTC |
| `/roll`   | Выдаёт случайное число от 0 до 100      |
| `/reroll` | Камень, ножницы или бумага (эмодзи)     |

---

## 🛠️ Используемые технологии

- [discord.py](https://discordpy.readthedocs.io/en/stable/) библиотека Python для взаимодействия с Discord API
- [discord.ui](https://discordpy.readthedocs.io/en/stable/interactions/api.html#module-discord.ui) модуль для создания кнопок и интерактивных элементов в Discord
- [Flask](https://flask.palletsprojects.com/en/stable/) лёгкий веб-фреймворк на Python, нужен для запуска HTTP-сервера на Render
- [Tweepy](https://docs.tweepy.org/en/stable/) Python-библиотека для работы с Twitter API
- [aiohttp](https://docs.aiohttp.org/en/stable/) Асинхронная библиотека Python для работы с HTTP
- [requests](https://pypi.org/project/requests/) Библиотека Python для выполнения HTTP-запросов.
- [CoinGecko API](https://www.coingecko.com/en/api) бесплатный API для получения информации о криптовалютах
- [Pillow](https://pillow.readthedocs.io/en/stable/) библиотека для обработки изображений в Python
- [asyncio](https://docs.python.org/3/library/asyncio.html) стандартный модуль Python для асинхронного программирования
- [Render](https://render.com/) облачная платформа, которая позволяет легко запускать и размещать веб-приложения, ботов и фоновые задачи.

---

## 📷 Скриншоты

---

## 👤 Автор

Создан с ❤️ для [Red Planet DAO](https://linktr.ee/rpdao)  
Автор: [KOT0628](https://github.com/KOT0628)

---

## 📝 Лицензия

RPDAO
