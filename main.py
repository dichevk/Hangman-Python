import sys
import pygame
from view import HangmanCanvas
from controller import Hangman



Hangman.load_images()
HangmanCanvas.setup_display()




continue_flag = True
inner_loop_flag = True
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        continue_flag = False
        pygame.quit()
        sys.exit()
        break

if continue_flag == True:
    if Hangman.run_game() == True:
        HangmanCanvas.setup_display()
        if inner_loop_flag == True:
            while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            inner_loop_flag = False
                            break
                        else:
                            Hangman.run_game()
                            break
                
else:
    pygame.quit()
    sys.exit()



