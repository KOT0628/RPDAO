# 🔴 Red Planet Discord Bot

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
- 🌐 Фоновый HTTP-сервер для Render
- 🚀 Автоматический запуск на Render
- 🔄 Пересылка сообщений и фото из Discord в Telegram

---

## ⚙️ Установка

```bash
git clone https://github.com/KOT0628/RPDAO-DC-Harvester.git
cd RPDAO-DC-Harvester
pip install -r requirements.txt
```

---

## 🛠️ Необходимые переменные окружения

Создайте файл `.env` или задайте переменные в Render:

| Переменная          | Описание                        |
|---------------------|---------------------------------|
| `DISCORD_TOKEN`     | Discord токен бота              |
| `GUILD_ID`          | ID вашего Discord сервера       |
| `BTC_CHANNEL_ID`    | ID канала для отображения цены  |
| `TWITTER_CHANNEL_ID`| ID канала для твитов            |
| `TWITTER_BEARER`    | Bearer Token для Twitter API    |
| `TWITTER_USER_ID`   | ID профиля Twitter              |
| `TELEGRAM_TOKEN`    | Telegram токен бота             |
| `CHAT_ID`           | ID Telegram чата                |

---

---

## 📂 Структура проекта

| Файл                    | Назначение                         |
| ----------------------- | ---------------------------------- |
| `btc_discord_bot.py`    | основной скрипт бота               |
| `background.jpg`        | фон для изображения с ценой        |
| `SpicyRice-Regular.ttf` | кастомный шрифт для текста         |
| `last_price.txt`        | кэш последней цены BTC             |
| `last_tweet.txt`        | кэш последнего отправленного твита |
| `logs.txt`              | лог-файл                           |
| `.env`                  | конфигурация токенов и ID          |
| `requirements.txt`      | список зависимостей Python         |

---

## 🌍 Размещение на Render (бесплатно)

1. Зарегистрируйтесь на [Render](https://render.com)
2. Создайте новый **Web Service**
3. Подключите GitHub-репозиторий
4. Установите:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python btc_discord_bot.py`
5. Установите переменные окружения (см. выше)
6. Убедитесь, что порт привязан через `Flask` (порт 8080)
7. Нажмите **Deploy**

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

> ![Screenshot_4](https://github.com/user-attachments/assets/fb2ec14c-1439-4a4e-aaba-0c4c6b0b9718)
> 
> ![Screenshot_5](https://github.com/user-attachments/assets/9c235e51-ce6e-4126-9f01-c68e18b3dba8)
> 
> ![Screenshot_7](https://github.com/user-attachments/assets/5d30aaf5-3e83-42ce-bb18-51885ae4b44a)
> 
> ![Screenshot_6](https://github.com/user-attachments/assets/55b78b40-6ed0-4031-9af7-bc858ee48710)

---

## 👤 Автор

Создан с ❤️ для [Red Planet DAO](https://linktr.ee/rpdao)  
Автор: [KOT0628](https://github.com/KOT0628)

---

## 📝 Лицензия

RPDAO
