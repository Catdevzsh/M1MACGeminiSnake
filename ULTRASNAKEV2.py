import pygame
import random

# Initialize Pygame
pygame.init()

# Screen size and colors (use 3 distinct colors for snake, food, and background)
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

snake_color = (150, 255, 0)  # Light green
food_color = (255, 0, 0)  # Red
background_color = (0, 0, 0)  # Black

# Block size (adjust for desired snake segment size)
block_size = 10

# Snake speed
snake_speed = 15

# Initial snake position and direction
snake_x = screen_width // 2
snake_y = screen_height // 2
snake_x_change = block_size
snake_y_change = 0

# Initialize snake list
snake_list = []
snake_length = 1

# Food position
food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

# Game loop
game_over = False

clock = pygame.time.Clock()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_x_change != block_size:
                snake_x_change = -block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT and snake_x_change != -block_size:
                snake_x_change = block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP and snake_y_change != block_size:
                snake_x_change = 0
                snake_y_change = -block_size
            elif event.key == pygame.K_DOWN and snake_y_change != -block_size:
                snake_x_change = 0
                snake_y_change = block_size

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for wall collisions
    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        game_over = True

    # Check for snake collisions with itself
    for x in snake_list[:-1]:
        if snake_x == x[0] and snake_y == x[1]:
            game_over = True

    # Create a new head piece (update snake_list)
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.insert(0, snake_head)

    # Check for food collision
    if snake_x == food_x and snake_y == food_y:
        snake_length += 1
        food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
        food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    # Delete tail segment if snake hasn't grown
    if len(snake_list) > snake_length:
        del snake_list[-1]

    # Fill the screen with background color
    screen.fill(background_color)

    # Draw snake using rectangles
    for x in snake_list:
        pygame.draw.rect(screen, snake_color, [x[0], x[1], block_size, block_size])

    # Draw food using a rectangle
    pygame.draw.rect(screen, food_color, [food_x, food_y, block_size, block_size])

    # Update the display
    pygame.display.flip()

    # Clock
## write a 60 fps cap
    clock.tick(15)
    ### 
