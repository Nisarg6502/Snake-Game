import pygame
x=pygame.init()

#creating window
gameWindow=pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First game!")

#creating variables specific to game
exit_game = False
game_over = False

#creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed the right key")
            elif event.key == pygame.K_LEFT:
                print("Left")

pygame.quit()
quit()