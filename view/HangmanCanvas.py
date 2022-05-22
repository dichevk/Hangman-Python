import pygame


''' This is the view part of the game. This is concerned with setting up the pygame display 
    and rendering/displaying elements/words on the user's screen
'''


'''  SET VARIABLES '''
WIDTH, HEIGHT = 800, 500
RADIUS = 20
GAP = 15
window = pygame.display.set_mode((WIDTH, HEIGHT))






''' a simple function to set up the display and give it a title'''
def setup_display():

    pygame.init()
    window.fill((255,255,255))
    pygame.display.update()
    pygame.display.set_caption("Hangman")




''' A function that displays a message on the terminal screen. 
    This is used to show correct design 
    output based on wether the player won or lost
    @requires string parameter message
    @param message -> string
'''
def display_message(message):

    window.fill((255,255,255))
    text = pygame.font.SysFont('comicsans', 30).render(message, 1, (0, 0, 0))
    window.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    text2 = pygame.font.SysFont('comicsans', 30).render("The game will play again", 1, (0, 0, 0))
    window.blit(text2, (WIDTH /2 - text2.get_width() / 2, HEIGHT/1.5 - text2.get_height() / 2))
    text3 = pygame.font.SysFont('comicsans', 20).render("If you would like to stop playing,close the window on next game", 1, (0, 0, 0))
    window.blit(text3, (WIDTH/2 - text3.get_width() / 2, HEIGHT/1.1- text3.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)



