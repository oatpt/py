import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Bouncing Rectangle")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
v=0
x=325
y=225
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                v=-1
            if event.key == pygame.K_RIGHT:
                v=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and v == -1:
                v=0
            if event.key == pygame.K_RIGHT and v == 1:
                v=0
            
    

    # --- Drawing
    # Set the screen background
    screen.fill(BLACK)

    if 0<x+v<650:
        x+=v
 
    # Draw the rectangle
    pygame.draw.line(screen,WHITE,[0,0],[700,500],10)
    pygame.draw.circle(screen,GREEN,[350,250],100)
    pygame.draw.rect(screen, WHITE, [x,y, 50, 50])
    pygame.draw.rect(screen, RED, [x+10,y+10, 30, 30])

 
    # --- Wrap-up
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Close everything down
pygame.quit()