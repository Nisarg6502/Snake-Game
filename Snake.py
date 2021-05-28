import pygame
import random
pygame.init()

#color
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 800
screen_height = 600

#creating window
gameWindow=pygame.display.set_mode((screen_width, screen_height))

#game title
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(black)
        text_screen("Welcome to Snakes by Nisarg", (0, 255, 0), 130, 150)
        text_screen("Press Space to Play", red, 220, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()


        pygame.display.update()
        clock.tick(60)

#game loop
def gameloop():
    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 400
    snake_y = 300
    velocity_x = 0
    velocity_y = 0
    snake_size = 13
    food_x = random.randint(10, screen_width-10)
    food_y = random.randint(10, screen_height-10)
    score = 0
    fps = 30
    snake_list = []
    snake_length = 1
    with open("highscore", "r") as f:
        highscore = f.read()
    while not exit_game:
        if game_over:
            with open("highscore", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(black)
            text_screen("Game Over! Press Enter to Continue", red, screen_width/10, screen_height/2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_y += 7
                        velocity_x = 0
                    if event.key == pygame.K_RIGHT:
                        velocity_x += 7
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x += -7
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y += -7
                        velocity_x = 0

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 1
                # print("Score", score)
                food_x = random.randint(10, screen_width)
                food_y = random.randint(10, screen_height)
                snake_length += 3
                if score>int(highscore):
                    highscore = score

            snake_x += velocity_x
            snake_y += velocity_y

            gameWindow.fill(black)
            text_screen("Score: "+str(score)+" Highscore: "+str(highscore), (255, 255, 0), 10, 10)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                print("Game Over")
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            plot_snake(gameWindow, white, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()