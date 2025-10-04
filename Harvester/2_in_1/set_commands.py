import os
import json

import requests

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

url = f"https://api.telegram.org/bot{TOKEN}/setMyCommands"

commands = [
    {"command": "price", "description": "Show current price $BTC"},
    {"command": "roll", "description": "ROLL"},
    {"command": "reroll", "description": "Throw the dice"},
    {"command": "gm", "description": "Good morning RPDAO"},
    {"command": "gn", "description": "Good night RPDAO"},
    {"command": "rpdao_game", "description": "Game Zone RPDAO"},
    {"command": "start_roll", "description": "Launch Roll-game"},
    {"command": "link", "description": "Official links Red Planet DAO"},
    {"command": "stop", "description": "Disabling the use of slash commands"},
    {"command": "resume", "description": "Enabling the use of slash commands"},
]

response = requests.post(url, json={"commands": commands})

if response.ok:
    print("Команды успешно установлены!")
else:
    print("Ошибка при установке команд:")
    print(response.text)
    
