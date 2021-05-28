import pygame
x=pygame.init()

#creating window
gameWindow=pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First game!")

#creating variables specific to game
exit_game = False
game_over = False