import os
import random


'''This is the model section of the game. This is mainly concerned with generating the needed elements for the project - 
    the lexicon and the hidden word'''


'''This function reads the lexicon.txt files and returns an array that contains all the words in the game
    @returns collection of all the words
'''
def generate_lexicon():
    text_file = open(os.path.abspath(os.curdir)+"\\"+"model"+"\\"+"HangmanLexicon.txt","r")
    lexicon = text_file.read().splitlines()
    text_file.close()
    return lexicon

''' This function generates a random word that is to be guessed by the player 
    @requires array/list of strings
    @returns string -> a random word from the lexicon
    @param lexicon -> list of words 
'''
def generate_random_word(lexicon):
    hidden_word = random.choice(lexicon)
    return hidden_word




