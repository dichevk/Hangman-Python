import os
import pygame
from view import HangmanCanvas
from model import HangmanModel
import math
import sys

''' This is the controller section of the MVC implementation of the game. 
Here the functions used for the logic of the game and the communication between the View, the Model and the Controller 
take place
'''

''' SET VARIABLES '''
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
guessed = []

letters =[]

hangman_status = 0
RADIUS = 20
GAP = 15
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65 #the ASCI code of A


''' this function sets the position for the letters on the screen and fills the array 
    letters with all the 26 letters in the English alphabet
'''
def set_letters():
    for i in range(26):
        x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))  # simulate having 2 rows
        y = starty + ((i // 13) * (GAP + RADIUS * 2))  # gives us 1st or 2nd row
        letters.append([x, y, chr(A + i), True])
set_letters()

''' a function to update the array that contains the guessed letters for the variable guessed
    @requires guessed array and character of type character that are not null 
    @param guessed -> list of guessed letters, character -> a newly guessed character 
'''
def update_guessed_arr(guessed,character):
    guessed.append(character)

''' This is one of the core functions that checks if the letters of the provided word 
    have been guessed and returns the word based on the 
    elements contained in guessed
    @requires word -> string, guessed -> list of characters, not null
    @returns a string that represents the current state of the word 
    @param word -> a randomly generated word, @param guessed -> list of guessed letters
'''
def word_checker(word,guessed):
    displayed_word = ""
    for letter in word:
        if letter in guessed:
            displayed_word += letter + ""
        else:
            displayed_word += "_ "
    return displayed_word


'''This is the function that is concerned with the main logic of the game,
    here user mouse input and game conditions are checked'''

def run_game():
    global hangman_status
    global word
    endgame_flag = False
    word = HangmanModel.generate_random_word(HangmanModel.generate_lexicon())
    run_flag = True
    clock = pygame.time.Clock()
    while run_flag:

        clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_flag = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y =pygame.mouse.get_pos()
                for letter in letters:
                    x, y, specific_letter,visible = letter
                    if visible:
                        distance = math.sqrt((x-pos_x)**2 + (y-pos_y)**2)#distance between mouse position and the position of the center of the button
                        if distance < RADIUS:
                            letter[3] = False #set visible status to False
                            update_guessed_arr(guessed, specific_letter)
                            if specific_letter not in word:
                                hangman_status+=1
        update_game(hangman_status)
        if check_win() == True:
            HangmanCanvas.display_message("YOU WON !")
            guessed.clear()
            letters.clear()
            set_letters()
            hangman_status = 0
            endgame_flag = True
            break
        if hangman_status == 6:
            HangmanCanvas.display_message("YOU LOST !" +" "+ "The word was"+ " " + word)
            guessed.clear()
            letters.clear()
            set_letters()
            hangman_status = 0
            endgame_flag = True
            break

    return endgame_flag

'''This function updates the game based on the current status of the hangman and the word
    @requires integer hangman_status
    @param hangman_status -> integer, the status of the hangman represented by an integer based on number of mistakes
'''
def update_game(hangman_status):
    window.fill((255, 255, 255))
    text_font = pygame.font.SysFont('comicsans', 30)

    text = text_font.render(word_checker(word,guessed),1, (0,0,0))
    window.blit(text, (400,200))
    for letter in letters:
        x, y, specific_letter, visible = letter
        if visible:
            pygame.draw.circle(window,(0,0,0),(x,y),RADIUS,3)
            text = text_font.render(specific_letter,1, (0,0,0))
            window.blit(text, (x-text.get_width()/2,y-text.get_height()/2))#put it in the middle (width/2 and heigh/2)
    window.blit(load_images()[hangman_status], (150, 100))
    pygame.display.update()


''' This function is used to load the hangman images and store them in an array
    @returns a list of description of images after formatting with Image Magick Display
'''
def load_images():
    images_arr = []


    imagepath = sys.path[1] +"\\view\\images"
    images = os.listdir(imagepath)


    for image in images:
        hangman_image = pygame.image.load(imagepath+"\\"+image)
        images_arr.append(hangman_image)


    return images_arr


''' This function checks if the player won which is based on whether all letters in the word have been guessed
    @returns boolean won -> True if the whole word is guessed
'''
def check_win():
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    return won


