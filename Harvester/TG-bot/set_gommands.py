
import requests
import os
import json

TOKEN = "YOUR_TELEGRAM_TOKEN"

url = f"https://api.telegram.org/bot{TOKEN}/setMyCommands"

commands = [
    {"command": "price", "description": "Show current price $BTC"},
    {"command": "roll", "description": "ROLL"},
    {"command": "reroll", "description": "Throw the dice"},
    {"command": "score", "description": "Leaderboard"},
    {"command": "gm", "description": "Good morning RPDAO"},
    {"command": "gn", "description": "Good night RPDAO"},
    {"command": "start_roll", "description": "Start ROLL (only admins)"},
    {"command": "rpdao_trivia", "description": "Launch of TRIVIA (only admins)"},
    {"command": "reroll_on", "description": "Launch of Throw the dice (only admins)"},
    {"command": "stop_roll", "description": "Stop ROLL (only admins)"},
    {"command": "rpdao_trivia_off", "description": "Stop TRIVIA (only admins)"},
    {"command": "reroll_off", "description": "Stop Throw the dice (only admins)"},
    {"command": "start", "description": "Restart RPDAO Harvester"},
]

response = requests.post(url, json={"commands": commands})

if response.ok:
    print("✅ Команды успешно установлены!")
else:
    print("❌ Ошибка при установке команд:")
    print(response.text)
    
