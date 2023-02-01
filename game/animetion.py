import pygame
from pygame.locals import *
 
# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()
 
# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((1500, 600))
 
 
# Create a list of different sprites
# that you want to use in the animation
image_sprite = [pygame.image.load("C:/Users/oatpt/Desktop/py/game/cat1.png"),
                pygame.image.load("C:/Users/oatpt/Desktop/py/game/cat2.jpg")]
 
 
# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()
 
# Creating a new variable
# We will use this variable to
# iterate over the sprite list
value = 0
 
# Creating a boolean variable that
# we will use to run the while loop
run = True
 
# Creating an infinite loop
# to run our game
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Setting the framerate to 3fps just
    # to see the result properly
    clock.tick(60)
 
    # Setting 0 in value variable if its
    # value is greater than the length
    # of our sprite list
    if value >= len(image_sprite):
        value = 0
 
    # Storing the sprite image in an
    # image variable
    image = image_sprite[value]
    # Displaying the image in our game window
    window.blit(image, (0, 0))
 
    # Updating the display surface
    pygame.display.update()
 
    # Filling the window with black color
    window.fill((0, 0, 0))
 
    # Increasing the value of value variable by 1
    # after every iteration
    value += 1