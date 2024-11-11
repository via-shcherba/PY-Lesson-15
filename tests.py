import unittest
from unittest.mock import patch
from loto import Card, Player, Game
import random

class TestCard(unittest.TestCase):
    def test_generate_card(self):
        card = Card()
        self.assertEqual(len(card.numbers), 3)  
        for row in card.numbers:
            self.assertEqual(len(row), 9)  
            self.assertTrue(all(isinstance(num, (int, str)) for num in row))  

    def test_mark_number(self):
        card = Card()
        number_to_mark = card.numbers[0][0]  
        self.assertTrue(card.mark_number(number_to_mark))  
        self.assertIn('-', card.numbers[0])  

    def test_mark_number_not_found(self):
        card = Card()
        self.assertFalse(card.mark_number(100)) 


class TestPlayer(unittest.TestCase):
    def test_make_move_mark(self):
        player = Player("Тестовый Игрок")
        number_to_mark = player.card.numbers[0][0]  
        with patch('builtins.input', side_effect=['y']):
            self.assertTrue(player.make_move(number_to_mark))  

    def test_make_move_not_mark(self):
        player = Player("Тестовый Игрок")
        number_to_mark = player.card.numbers[0][0]  
        with patch('builtins.input', side_effect=['n']):
            self.assertFalse(player.make_move(number_to_mark))  


class TestGame(unittest.TestCase):
    @patch('random.shuffle')
    def test_play(self, mock_shuffle):
        player1 = Player("Игрок 1")
        player2 = Player("Игрок 2")
        game = Game(player1, player2)

        game.balls = [1, 2, 3, 4, 5]

        with patch('builtins.input', side_effect=['y', 'y', 'y', 'y', 'y']):
            game.play()  
        self.assertTrue(len(game.balls) == 4) 



if __name__ == '__main__':
    unittest.main()