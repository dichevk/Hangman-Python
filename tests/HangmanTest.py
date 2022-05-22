import unittest
import controller
from controller import Hangman
from model import HangmanModel
from view import HangmanCanvas

class HangmanTest(unittest.TestCase):
    def test_word_checker(self):
        result = Hangman.word_checker("HANGMAN",['H','A','G','M','N'])
        self.assertEqual(result, "HANGMAN")
    def test_word_checker(self):
        result2 = Hangman.word_checker("HANGMAN",['A'])
        self.assertEqual(result2, "_ A_ _ _ A_ ")
    def test_word_checker(self):
        result3 = Hangman.word_checker("HANGMAN",['A','N'])
        self.assertEqual(result3, "_ AN_ _ AN")
    def test_word_checker(self):
        result4 = Hangman.word_checker("HANGMAN", [''])
        self.assertEqual(result4, "_ _ _ _ _ _ _ ")
    def test_word_checker(self):
        result5 = Hangman.word_checker("APPLE", ['A','L','E'])
        self.assertEqual(result5, "A_ _ LE")


