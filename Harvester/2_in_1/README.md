## 📚 Contents

* [🔴 Red Planet Harvester Bot](#-red-planet-harvester-bot)
* [📦 Functionality and Capabilities](#-functionality-and-capabilities)

  * [🟣 Telegram](#-telegram)
  * [🔵 Discord](#-discord)
  * [🔴 General Features](#-general-features)

* [📚 Supported slash commands](#-supported-slash-commands)

  * [🟣 Telegram](#-telegram-1)
  * [🔵 Discord](#-discord-1)

* [🛠 Requirements](#-requirements)

  * [🗂 Project Structure](#-1-project-structure)
  * [📥 Installing dependencies](#-2-installing-dependencies)
  * [🔐 Creating .env](#-3-create-a-env-file-with-the-following-variables)
  * [📂 Auxiliary files](#-4-auxiliary-files)

* [🛠️ Technologies used](#%EF%B8%8F-technologies-used)
* [📷 Screenshots](#-screenshots)
* [🚀 Launch](#-launch)
* [🧹 Shutdown](#-shutdown)
* [⚠️ Notes](#%EF%B8%8F-notes)
* [👤 Author](#-author)
* [📝 License](#-license)

---

# 🔴 Red Planet Harvester Bot

> ***Red Planet Harvester*** - *is a multifunctional, universal bot for the Red Planet DAO community, combining the capabilities of Telegram and Discord in one script.*

This bot will automatically:

- sends a generated image with the current Bitcoin price to [Telegram](https://t.me/rpdao) and [Discord](https://discord.gg/g4b8RsbnNd) **"Red Planet DAO"** every 4 hours;
- processes slash commands: `/price`, `/roll`, `/reroll`, `/gm`, `/gn`, `/rpdao_game`, `/start_roll`, `/link`, `/stop`, `/resume`;
- forwards all messages and images **from Telegram to Discord**, with automatic translation into English;
- forwards all messages and images **from Discord to Telegram**;
- supports tweet relaying **from Twitter to Discord**.

---

## 📦 Functionality and capabilities

### 🟣 **Telegram:**

- 🕓 Automatic posting of an image with the price of $BTC every 4 hours
- 💬 Forwarding all messages and images from Telegram to Discord (with translation into English)
- 🎮 Game zone:
  - 🎲 mini-game `ROLL` - a random number from 0 to 100, using `/roll`
  - 🎰 mini-game `"Rock, paper, scissors"`, using `/reroll`
  - 🧠 quiz `TRIVIA` with automatic hints and two game modes:
    - **Random mode** - a question comes 30-90 minutes after the previous correct answer.
    - **Fixed mode** - a strict 60-second interval between rounds.
  - 🏆 View leaderboard (with page navigation):
    - 📤 in general chat
    - 📬 in private messages
  - 🏆 Crimson Envoys leaderboard:
    - `/crimson_board` — view Crimson Envoys leaderboard (with page navigation):
      - 📤 in general chat
      - 📬 in private messages
  - 🔗 Red Planet DAO social media links:
    - `/link` — view official Red Planet DAO links:
      - 📤 in general chat
      - 📬 in private messages
- 🛡️ Protection:
  - from old messages (does not respond to outdated ones)
  - from double launch via `bot.lock`
- 📝 Translator logging:
  - to `translate.txt` file (automatically cleared every 3 days)

- 📤 CLI bot for Telegram:
  - 💬 multiline input
  - 📷 photos and 📹 videos
  - 📁 recent file selection
  - 📌 pinning
  - 🧾 reply to message
  - 📦 drag-and-drop

### 🔵 **Discord:**

- 📈 Automatic Bitcoin price update via CoinGecko API:
  - display it in the voice channel name
  - 🟢🔴 emoji and arrows depending on the price change
- 🎲 Command `/roll` - random number from 0 to 100
- 🎰 Command `/reroll` - mini-game "Rock, paper, scissors"
- 🐦 Relaying original tweets from a Twitter account to a Discord channel:
  - 🔗 buttons to go to a tweet and retweet
  - ❤️ automatic reactions to a tweet
- 🔄 Forwarding messages and photos from Discord to Telegram
- 📬 Sending notifications to Telegram about new "Tickets"
- 🛡️ Protection:
  - 🐦 Twitter API - multi-level protection against exceeding limits:
    - ⏱️ **Limit frequencies** - takes into account the time of the last successful verification of tweets;
    - 🔁 **Automatic blocking** when receiving the `429 Too Many Requests` error;
    - 📅 **Detection of the monthly limit** (`Usage cap exceeded`) and disabling retransmission until the Nth number;
    - 📁 **Saving the blocking state** to a file - even when restarting, the bot will not use the API until the end of the blocking period;
    - ✅ **Restoration of access** after the end of a temporary or monthly blocking - automatically.

### 🔴 **General Features:**

- 📸 Image generation:
  - `/price` - $BTC price
  - `/gm` - good morning (random phrase, random background)
  - `/gn` - good night (random phrase, random background)
- 📝 Logging:
  - in one file `logs.txt` - with time rotation (1 day) and automatic deletion of old files (older than 7 days)

---

## 👁 Supported slash commands

### 🟣 **Telegram:**

| Command             | Purpose                                      |
| ------------------- | -------------------------------------------- |
| `/price`            | Sends a picture with the current BTC price   |
| `/roll`             | Generates a random number from 0 to 100      |
| `/reroll`           | Rock, paper or scissors (emoji)              |
| `/gm`               | Sends a picture with "Good morning"          |
| `/gn`               | Sends a picture with "Good night"            |
| `/rpdao_game`       | Opens the "Game Zone" menu                   |
| `/crimson_board`    | Opens the Crimson Envoy leaderboard          |
| `/link`             | Sends links to social-media                  |
| `/start_roll`       | Starts the "ROLL" tournament mode            |
| `/stop_roll`        | Stops the "ROLL" tournament mode             |
| `/reroll_on`        | Starts the Rock, Paper, Scissors minigame    |
| `/reroll_off`       | Stops the Rock, Paper, Scissors minigame     |
| `/rpdao_trivia`     | Starts the TRIVIA                            |
| `/rpdao_trivia_off` | Stops the TRIVIA                             |
| `/score`            | Opens the Game Zone leaderboard              |
| `/tag`              | Tags active chat participants from the list  |
| `/stop`             | Disables slash commands                      |
| `/resume`           | Enables slash commands                       |

### 🔵 **Discord:**

| Command   | Purpose                                    |
| --------- | ------------------------------------------ |
| `/price`  | Sends a picture with the current BTC price |
| `/roll`   | Gives a random number from 0 to 100        |
| `/reroll` | Rock, paper or scissors (emoji)            |

---

## 🛠 Requirements

### 🗂 **1. Project structure**

```
RPDAO-Harvester_v2.0/
│
├── __init__.py
├── main.py                            # Main entry point
├── tg_bot.py                          # Launching a Telegram bot
├── dc_bot.py                          # Launching a Discord bot
│
├── console_sender.py                  # CLI bot for Telegram
│
├── config/                            # Configurations
│   ├── __init__.py
│   └── settings.py                    # Loading environment variables
│
├── utils/                             # Auxiliary functions
│   ├── __init__.py
│   ├── check_admin.py                 # Checking administrator rights
│   ├── dc_helpers.py                  # Screening, saving the last tweet, etc.
│   ├── helpers.py                     # Screening, deleting messages, etc.
│   ├── image.py                       # Image generation
│   ├── logger.py                      # Setting up logging
│   ├── message_map.py                 # Discord - Telegram message mapping
│   ├── scheduler.py                   # Scheduler
│   ├── scoreboard.py                  # Formation of Leaderboard
│   ├── telegram_notify.py             # Sending a notification about a new "ticket" in Telegram
│   ├── translate.py                   # Universal translator
│   └── tweets_guard.py                # Monitoring Twitter API call rates
│
├── features/                          # Main functionality
│   ├── game/                          # Red Planet DAO chat mini games
│   │   ├── __init__.py 
│   │   ├── dc_reroll.py               # Discord slash command /reroll
│   │   ├── dc_roll.py                 # Discord slash command /reroll
│   │   ├── game_menu.py               # Game menu module
│   │   ├── game_state.py              # Reroll Mode status module
│   │   ├── handlers.py                # Common facade for Roll, Reroll and TRIVIA
│   │   ├── reroll.py                  # Reroll logic
│   │   ├── roll.py                    # Roll logic
│   │   └── trivia.py                  # TRIVIA logic
│   ├── __init__.py
│   ├── crimson_board.py               # Crimson Envoy Leaderboard logic
│   ├── dc_price.py                    # Discord slash command /price
│   ├── discord_bridge.py              # Forwarding messages and photos in Discord
│   ├── gm_gn.py                       # Telegram slash commands /gm and /gn
│   ├── link.py                        # Telegram slash command /link
│   ├── price.py                       # Telegram slash command /price
│   ├── score.py                       # Game Leaderboard logic
│   ├── stop_start.py                  # Disabling/enabling the use of slash commands
│   ├── tag.py                         # Tag active users in chat
│   ├── telegram_bridge.py             # Forwarding messages and photos in Telegram
│   ├── ticket_notify.py               # Processing the creation of a new channel with a "ticket"
│   └── tweets.py                      # Relaying tweets from Twitter to Discord
│
├── assets/
│   ├── backgrounds/
│   │   ├── morning/                   # Backgrounds for /gm
│   │   │   ├── 1.jpg
│   │   │   ├── 2.jpg
│   │   │   ├── 3.jpg
│   │   ├── night/                     # Backgrounds for /gn
│   │   │   ├── 1.jpg
│   │   │   ├── 2.jpg
│   │   │   ├── 3.jpg
│   │   └── background.jpg             # Background for /price
│   ├── fonts/
│   │   └── SpicyRice-Regular.ttf      # Font
│   ├── game_zone.jpg                  # Background for the main menu of the "Game Zone"
│   ├── leaderboard.jpg                # Background of the submenu "Game zone"
│   ├── link.png                       # Background for social media links menu
│   ├── reroll.jpg                     # Background of the submenu "Game zone"
│   ├── roll.jpg                       # Background of the submenu "Game zone"
│   └── trivia.txt                     # Background of the submenu "Game zone"
│
├── data/
│   ├── discord/
│   │   ├── last_price.txt             # Latest Price $BTC
│   │   └── message_map.json           # Message mapping file
│   ├── game/
│   │   ├── active_users.json          # List of active chat users
│   │   └── trivia_questions.txt       # Quiz questions
│   ├── img_output/
│   │   ├── btc_price_output.jpg       # Generated image with $BTC price
│   │   ├── gm_output.jpg              # Generated image "Good morning"
│   │   └── gn_output.jpg              # Generated image "Good night"
│   ├── leadeboard/
│   │   ├── crimson_scores.json        # Crimson Envoy Leaderboard
│   │   └── scores.json                # "Game Zone" Leaderboard
│   ├── logs/
│   │   ├── logs.log                   # Log file
│   │   └── translate.log              # Translator log file
│   ├── secrets/
│   │   └── google_key.json            # GoogleCloud Translate API key
│   └── twitter/
│       ├── last_tweet.txt             # Last Rebroadcast Tweet
│       ├── last_twitter_check.txt     # Contains the time of the last successful Twitter check
│       ├── twitter_block.txt          # Contains the expiration time of the API temporary block
│       └── twitter_disabled.txt       # Contains information about the API lock state
│
└── requirements.txt                   # List of dependencies
```
### 📥 **2. Installing dependencies:**

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
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

### 🔐 **3. Create a `.env` file with the following variables:**

| Variable                         | Description                                     |
|----------------------------------|-------------------------------------------------|
| `TELEGRAM_TOKEN`                 | Telegram bot token                              |
| `CHAT_ID`                        | Telegram chat ID                                |
| `DISCORD_TOKEN`                  | Discord bot token                               |
| `GUILD_ID`                       | ID of your Discord server                       |
| `COMMAND_CHANNEL_ID`             | Channel ID for using commands                   |
| `GAME_CHANNEL_ID`                | Channel ID for using game commands              |
| `DISCORD_CHANNEL_ID`             | Channel ID for forwarding messages              |
| `BTC_CHANNEL_ID`                 | Channel ID for displaying prices                |
| `TWITTER_CHANNEL_ID`             | Channel ID for tweets                           |
| `TWITTER_BEARER`                 | Bearer Token for Twitter API                    |
| `TWITTER_USER_ID`                | Twitter profile ID                              |
| `DISCORD_WEBHOOK_URL`            | Discord Webhook URL (for forwarding to Discord) |
| `DEEPL_API_KEY`                  | DeepL translator API key                        |
| `GOOGLE_APPLICATION_CREDENTIALS` | GoogleCloud translator API key                  |
| `DISCORD_AVATAR_URL`             | Bot avatar URL                                  |

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

# Deepl (transkate)
DEEPL_API_KEY=deepl_api_key
GOOGLE_APPLICATION_CREDENTIALS=data/secrets/google_key.json

# Other
DISCORD_AVATAR_URL=your_avatar_url
```

### 📂 **4. Auxiliary files:**

| File                     | Purpose                                                              |
| ------------------------ | -------------------------------------------------------------------- |
| `acrive_users.json`      | list of active Telegram chat users                                   |
| `background.jpg`         | background for price image                                           |
| `morning1-6.jpg`         | backgrounds for "Good morning" image                                 |
| `night1-6.jpg`           | backgrounds for "Good night" image                                   |
| `game_zone.jpg`          | background for "Game zone" main menu                                 |
| `roll.jpg`               | background for `ROLL` submenu                                        |
| `reroll.jpg`             | background for `REROLL` submenu                                      |
| `trivia.jpg`             | background for `TRIVIA` submenu                                      |
| `leaderboard.jpg`        | background for `LEADERBOARD` submenu                                 |
| `SpicyRice-Regular.ttf`  | custom font for text                                                 |
| `last_price.txt`         | cache of the latest BTC price (automatically generated)              |
| `last_tweet.txt`         | cache of the last sent tweet (automatically generated)               |
| `last_twitter_check.txt` | time of the last successful Twitter check (automatically generated)  |
| `twitter_block.txt`      | time of the end of the API temporary block (automatically generated) |
| `logs.log`               | general bot log file (automatically generated)                       |
| `translate.log`          | translator log file (automatically generated)                        |
| `trivia_questions.txt`   | questions for the mini-game `TRIVIA`                                 |
| `scores.json.`           | "Game Zone" leaderboard file (automatically generated)               |
| `crimson_scores.json`    | "Crimson Envoy" leaderboard file                                     |
| `message_map.json`       | message mapping file (automatically generated)                       |
| `.env`                   | token and ID configuration                                           |
| `google_key.json`        | GoogleCloud Translate API key                                        |
| `requirements.txt`       | Python dependency list                                               |

---

## 🛠️ Technologies Used

- [os](https://docs.python.org/3/library/os.html) built-in Python module for working with the operating system (files, environment variables, processes)
- [sys](https://docs.python.org/3/library/sys.html) built-in Python module for accessing system parameters and interacting with the interpreter
- [re](https://docs.python.org/3/library/re.html) built-in Python module for working with regular expressions
- [time](https://docs.python.org/3/library/time.html) built-in Python module for working with time and delays
- [uuid](https://docs.python.org/3/library/uuid.html) built-in Python module for generating unique identifiers (UUIDs)
- [json](https://docs.python.org/3/library/json.html) built-in Python module for encoding and decoding JSON data
- [random](https://docs.python.org/3/library/random.html) built-in Python module for generating random numbers and samples
- [logging](https://docs.python.org/3/library/logging.html) built-in Python module for logging applications
- [threading](https://docs.python.org/3/library/threading.html) built-in Python module for multithreading
- [tempfile](https://docs.python.org/3/library/tempfile.html) built-in Python module for creating temporary files and directories
- [datetime](https://docs.python.org/3/library/datetime.html) built-in module Python for working with dates and times
- [discord.py](https://discordpy.readthedocs.io/en/stable/) Python library for interacting with the Discord API
- [discord.ui](https://discordpy.readthedocs.io/en/stable/interactions/api.html#module-discord.ui) module for creating buttons and interactive elements in Discord
- [discord.ext](https://discordpy.readthedocs.io/en/stable/ext/commands/index.html) extension of the `discord.py` library, providing a system of commands for creating Discord bots
- [Tweepy](https://docs.tweepy.org/en/stable/) Python library for working with the Twitter API
- [aiohttp](https://pypi.org/project/aiohttp/) Python library for performing asynchronous HTTP requests based on asyncio. Used for high-performance interaction with APIs, including working with Twitter via Tweepy
- [async_lru](https://pypi.org/project/async-lru/) asynchronous implementation of LRU (Least Recently Used) caching for Python functions. Allows caching the results of asynchronous calls, reducing the load and speeding up repeated requests
- [oauthlib](https://pypi.org/project/oauthlib/) Python library implementing the OAuth 1.0 and OAuth 2.0 protocols. Provides secure authorization and authentication when working with APIs, including the Twitter API via Tweepy
- [aiohttp](https://docs.aiohttp.org/en/stable/) an asynchronous Python library for working with HTTP
- [asyncio](https://docs.python.org/3/library/asyncio.html) a standard Python module for asynchronous programming
- [colorama](https://pypi.org/project/colorama/?utm_source=chatgpt.com) a Python library that provides support for ANSI escape sequences (for colored text and terminal cursor control) across various operating systems
- [requests](https://pypi.org/project/requests/) a Python library for making HTTP requests
- [Pillow](https://pillow.readthedocs.io/en/stable/) a library for image processing in Python
- [psutil](https://psutil.readthedocs.io/en/latest/) a Python library for getting information about system resources (CPU, memory, disks, network) and managing processes
- [schedule](https://schedule.readthedocs.io/en/stable/) a Python library for easily scheduling periodic tasks using clear syntax
- [python-dotenv](https://saurabh-kumar.com/python-dotenv/) Python library for loading environment variables from `.env` file into system environment variables
- [python-telegram-bot](https://docs.python-telegram-bot.org/) Python library for creating Telegram bots with support for asynchrony, convenient handlers and interaction with Telegram Bot API
- [pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/) simple Python library for creating Telegram bots with synchronous and convenient API based on [telebot](https://github.com/eternnoir/pyTelegramBotAPI)
- [telebot](https://pypi.org/project/pyTelegramBotAPI/) Python library (part of `pyTelegramBotAPI`) for creating Telegram bots
- [discord-webhook](https://pypi.org/project/discord-webhook/) simple Python library for sending messages via Discord Webhooks
- [word2number](https://pypi.org/project/word2number/) Python library for converting numbers written in words (e.g. "two hundred") to numeric format (`200`)
- [PyNaCl](https://pynacl.readthedocs.io/) Python binding to the [NaCl](https://nacl.cr.yp.to/) library, implementing modern cryptographic functions (e.g. digital signatures, encryption, etc.)
- [CoinGecko] API](https://www.coingecko.com/en/api) free API for getting information about cryptocurrencies
- [DeepL API](https://www.deepl.com/docs-api) programming interface from DeepL for automatic text translation with support for high-quality translations
- [deepl](https://pypi.org/project/deepl/) official Python library for working with DeepL API - one of the highest quality services for machine translation of text
- [Google Cloud Translation API](https://cloud.google.com/translate) API from Google for text translation. Supports automatic language detection, terminology customization, and integration into web and mobile apps
- [google-cloud-translate](https://cloud.google.com/python/docs/reference/translate/latest) official Python library for using Google Cloud Translation API for automatic text translation
- [deep-translator](https://deep-translator.readthedocs.io/en/latest/) universal Python library for text translation with support for several services, including Google Translate, DeepL, Microsoft Translator, and others
- [langdetect](https://pypi.org/project/langdetect/) Python library for automatic text language detection based on Google Language Detection algorithms

---

## 📷 Screenshots

![001](https://github.com/user-attachments/assets/92295d29-269f-4f49-b2a4-8e95059fd38c)

---

![002](https://github.com/user-attachments/assets/61d96108-7678-4a22-bbe8-f79b9fcb74da)

---

![003](https://github.com/user-attachments/assets/1febf595-574b-4146-aa78-dcb4b09261e8)

---

![004](https://github.com/user-attachments/assets/2dd836d5-bc50-4bce-be9b-54963cdfe0f9)

---

![005](https://github.com/user-attachments/assets/928b4efc-1006-4321-b55a-f2552297cbb5)

---

![006](https://github.com/user-attachments/assets/3a427db5-5e32-4d6a-9126-a33ddc749563)

---

![007](https://github.com/user-attachments/assets/1f36afc1-c035-4df4-8fed-e2fcdcc1576d)

---

## 🚀 Launch

```powershell
python main.py
```

### **The bot will start working and will:**

- every 10 minutes update the channel name in **Discord** with the current price of $BTC
- every 30 minutes check for a new tweet to relay to Discord
- monitor the creation of new "tickets" and send a notification to Telegram
- every 4 hours publish an image with the price of $BTC in **Telegram**
- react to the processing of slash commands:
- **Telegram** `/price`, `/gm`, `/gn`, `/rpdao_game`, `/crimson_board`, `/link`, `/start_roll` / `/roll` / `/stop_roll`, `/reroll_on` / `/reroll` / `/reroll_off`, `/rpdao_trivia` / `/rpdao_trivia_off`, `/score`, `/tag`, `/stop` / `/resume`
- **Discord** `/price`, `/roll`, `/reroll`
- automatically forward all messages and photos to **Discord** with English translation
- automatically forward all messages and photos to **Telegram**
- mini-games in **Telegram**: rounds `/roll`, tournaments `/reroll` and quiz `/rpdao_trivia`

---

## 🧹 Shutdown

When the script terminates, `bot.lock` is automatically removed so that the **Telegram** bot can be restarted without conflicts.

---

## ⚠️ Notes

- If the bot does not respond, check the log `entrypoint.log` or `logs.log`.
- Make sure the environment variables are set correctly.
- If the bot is running in a group, add it as an administrator with rights to delete, pin and send messages and media.

---

## 👤 Author

Created with ❤️ for [Red Planet DAO](https://linktr.ee/rpdao)  
Author: [KOT](https://github.com/KOT0628)

---

## 📝 License

©️ RPDAO
