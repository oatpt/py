import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
pygame.mouse.set_visible(False)

# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Bouncing Rectangle")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
color=WHITE
x,y=0,0
velocity_x = 0
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render('GeeksForGeeks', False, GREEN)

    textRect = text.get_rect()
 
    textRect.center = (350, 250)

    screen.blit(text, textRect)

 
    # --- Wrap-up
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Close everything down
pygame.quit()