import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('C:/Users/oatpt/Desktop/py/game/pygame_tutorials-main/sprite_tutorial/doux.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)


frame_0 = sprite_sheet.get_image(0, 24, 24, 3, BLACK)
index=0
clock = pygame.time.Clock()
run = True
while run:

	#update background
	screen.fill(BG)

	#show frame image

	frame_0 = sprite_sheet.get_image(index, 24, 24, 3, BLACK)

	screen.blit(frame_0, (238, 238))
	index+=1
	if(index == 10):
		index=0
	clock.tick(10)
	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()