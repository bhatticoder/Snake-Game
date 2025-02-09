import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 900
screen_height = 600

# Snake settings
snakeX = 45
snakeY = 55
snakeSize = 10
fps = 60

velocityX = 0
velocityY = 0
init_velocity = 5

# Generate random food position
FoodX = random.randint(20, screen_width - 20)
FoodY = random.randint(20, screen_height - 20)
score = 0

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Create game window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Game variables
exit_game = False
game_over = False
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# Function to render text on the screen
def textScreen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x, y))

# Function to draw the snake with circles
def plotSnake(gameWindow, color, snakeList, snakeSize):
    for x, y in snakeList:
        pygame.draw.circle(gameWindow, color, (x, y), snakeSize)

# Function to draw walls
def drawWalls():
    pygame.draw.rect(gameWindow, black, [0, 0, screen_width, 10])  # Top wall
    pygame.draw.rect(gameWindow, black, [0, screen_height - 10, screen_width, 10])  # Bottom wall
    pygame.draw.rect(gameWindow, black, [0, 0, 10, screen_height])  # Left wall
    pygame.draw.rect(gameWindow, black, [screen_width - 10, 0, 10, screen_height])  # Right wall

snakeList = []
snakeLen = 1

# Game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocityX = init_velocity
                velocityY = 0
            if event.key == pygame.K_LEFT:
                velocityX = -init_velocity
                velocityY = 0
            if event.key == pygame.K_UP:
                velocityY = -init_velocity
                velocityX = 0
            if event.key == pygame.K_DOWN:
                velocityY = init_velocity
                velocityX = 0

    if not game_over:
        snakeX += velocityX
        snakeY += velocityY

        # Check collision with walls
        if snakeX <= 10 or snakeX >= screen_width - 10 or snakeY <= 10 or snakeY >= screen_height - 10:
            game_over = True

        # Check collision with food
        if abs(snakeX - FoodX) < 10 and abs(snakeY - FoodY) < 10:
            score += 1
            FoodX = random.randint(20, screen_width - 20)
            FoodY = random.randint(20, screen_height - 20)
            snakeLen += 5

        # Fill the window with white color
        gameWindow.fill(white)

        # Draw walls
        drawWalls()

        # Display score
        textScreen("Score: " + str(score * 2), red, 5, 5)

        # Draw food
        pygame.draw.circle(gameWindow, red, (FoodX, FoodY), snakeSize)

        # Append new position to snakeList
        head = [snakeX, snakeY]
        snakeList.append(head)
        if len(snakeList) > snakeLen:
            del snakeList[0]

        # Draw the snake with circles
        plotSnake(gameWindow, green, snakeList, snakeSize)

        # Update display
        pygame.display.update()
        clock.tick(fps)

    else:
        gameWindow.fill(white)
        textScreen("Game Over! Press Enter to Continue", red, 100, screen_height // 2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_over = False
                    snakeX = 45
                    snakeY = 55
                    snakeList = []
                    snakeLen = 1
                    score = 0
                    velocityX = 0
                    velocityY = 0

# Quit pygame properly
pygame.quit()
