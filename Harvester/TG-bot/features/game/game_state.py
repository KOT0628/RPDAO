# === РЕЖИМ ТУРНИРА В ИГРЕ /roll ===
# Новый режим: 'tournament' или 'free'
reroll_mode = 'free'                                        # по умолчанию свободный

# Очередь для дуэлей в режиме 'tournament'
reroll_duel_queue = []                                      # Очередь игроков
current_duel_players = set()                                # Пара для текущей дуэли

# == Глобальные переменные режима /reroll ==
reroll_enabled = False
reroll_temp_players = set()
reroll_game_state = {}                                      # текущая игра в /reroll
