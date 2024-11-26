import random
    
class Card:
    def __init__(self):
        self.numbers = self.generate_card()

    def generate_card(self):
        card = []
        for _ in range(3):
            row = sorted(random.sample(range(1, 91), 5))
            card.append(row + [' '] * 4)  # Добавляем 4 пустые клетки
        return card

    def mark_number(self, number):
        for row in self.numbers:
            for i, cell in enumerate(row):
                if cell == number:
                    row[i] = '-'
                    return True
        return False

    def __str__(self):
        card_str = "--------------------------\n"
        for row in self.numbers:
            card_str += ' '.join(f"{str(num).rjust(2)}" for num in row) + "\n"
        card_str += "--------------------------"
        return card_str
    
    def __eq__(self, other):
        return isinstance(other, Card) and self.numbers == other.numbers

    def __ne__(self, other):
        return not self.__eq__(other)

class Player:
    def __init__(self, name):
        self.name = name
        self.card = Card()

    def make_move(self, number):
        choice = input(f"{self.name}, хотите зачеркивать число {number}? (y/n): ").strip().lower()
        if choice == 'y':
            if self.card.mark_number(number):
                print(f"{self.name} зачеркивает число {number}.")
                return True
            else:
                print(f"{self.name} проиграл! Число {number} нет на карточке.")
                return False
        else:
            if self.card.mark_number(number):
                print(f"{self.name} проиграл! Число {number} есть на карточке.")
                return False
            else:
                print(f"{self.name} пропускает ход.")
                return True

    def __str__(self):
        return f"Игрок: {self.name}, Карточка:\n{self.card}"

    def __eq__(self, other):
        return isinstance(other, Player) and self.name == other.name and self.card == other.card

    def __ne__(self, other):
        return not self.__eq__(other)

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.balls = list(range(1, 91))
        random.shuffle(self.balls)

    def play(self):
        while self.balls:
            current_ball = self.balls.pop()
            print(f"Новый бочонок: {current_ball} (осталось {len(self.balls)})")
            for player in self.players:
                print(f"------ Карточка {player.name} -----")
                print(player.card)
                if not player.make_move(current_ball):
                    print(f"{player.name} проиграл!")
                    return
            print("\n" + "="*30 + "\n")
        print("Игра окончена!")

if __name__ == "__main__":
    player1 = Player("Игрок 1")
    player2 = Player("Компьютер")

    game = Game(player1, player2)
    game.play()