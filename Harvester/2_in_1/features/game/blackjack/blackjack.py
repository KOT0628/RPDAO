import random

CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9,
               '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
SUITS = ['♠', '♥', '♦', '♣']

class Deck:
    def __init__(self):
        self.cards = [f"{v}{s}" for v in CARD_VALUES for s in SUITS]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class Player:
    def __init__(self, user, name=None):
        from telebot import types

        self.user = user

        if isinstance(user, types.User):
            self.user_id = user.id
            self.username = user.username or f"id{user.id}"
            self.name = (
                user.first_name
                or (user.username and f"@{user.username}")
                or str(user.id)
            )
        else:
            # Бот или псевдопользователь
            self.user_id = str(user)
            self.username = name or f"id{user}"
            self.name = name or str(user)

        self.cards = []
        self.stopped = False

    @property
    def score(self):
        total = sum(CARD_VALUES[c[:-1]] for c in self.cards)
        aces = sum(1 for c in self.cards if c.startswith('A'))
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def __repr__(self):
        """Удобное представление игрока для логов"""
        return f"<Player @{self.username} ({self.name}) id={self.user_id}>"

class Game:
    def __init__(self, player1, player2=None):
        self.deck = Deck()
        self.player1 = player1

        # если второго игрока нет — создаем бота
        self.player2 = player2 or Player("bot", "🤖 Harvester")
        self.turn = player1.user_id
        self.finished = False
        self.waiting_for = player1.user_id                 # кто сейчас должен ходить
        self.phase = 1                                     # 1 — ход игрока 1, 2 — ход игрока 2

    def deal_start(self):
        for p in (self.player1, self.player2):
            p.cards = [self.deck.draw(), self.deck.draw()]

# === Unicode-символы для визуальных карт ===
# Каждая масть и ранг имеет собственный Unicode в диапазоне "Playing Cards"
CARD_EMOJI_MAP = {
    "A♠": "🂡", "2♠": "🂢", "3♠": "🂣", "4♠": "🂤", "5♠": "🂥", "6♠": "🂦", "7♠": "🂧", "8♠": "🂨", "9♠": "🂩", "10♠": "🂪", "J♠": "🂫", "Q♠": "🂭", "K♠": "🂮",
    "A♥": "🂱", "2♥": "🂲", "3♥": "🂳", "4♥": "🂴", "5♥": "🂵", "6♥": "🂶", "7♥": "🂷", "8♥": "🂸", "9♥": "🂹", "10♥": "🂺", "J♥": "🂻", "Q♥": "🂽", "K♥": "🂾",
    "A♦": "🃁", "2♦": "🃂", "3♦": "🃃", "4♦": "🃄", "5♦": "🃅", "6♦": "🃆", "7♦": "🃇", "8♦": "🃈", "9♦": "🃉", "10♦": "🃊", "J♦": "🃋", "Q♦": "🃍", "K♦": "🃎",
    "A♣": "🃑", "2♣": "🃒", "3♣": "🃓", "4♣": "🃔", "5♣": "🃕", "6♣": "🃖", "7♣": "🃗", "8♣": "🃘", "9♣": "🃙", "10♣": "🃚", "J♣": "🃛", "Q♣": "🃝", "K♣": "🃞",
}

def render_cards(cards: list[str], hide_second: bool = False) -> str:
    """
    Возвращает визуальное представление карт игрока в виде Unicode-эмодзи.

    :param cards: список карт, например ["A♠", "10♦"]
    :param hide_second: если True — скрывает вторую карту (для дилера в начале игры)
    :return: строка вроде "🂡 🂩 🃍"
    """
    if not cards:
        return "—"

    rendered = []
    for i, card in enumerate(cards):
        if hide_second and i == 1:
            rendered.append("🂠")  # скрытая рубашка карты
        else:
            rendered.append(CARD_EMOJI_MAP.get(card, card))

    return " ".join(rendered)

__all__ = [render_cards]
