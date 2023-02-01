import pygame
import button

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_run = False
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load("C:/Users/oatpt/Desktop/py/game/pygame_tutorials-main/Menu/images/button_resume.png").convert_alpha()
options_img = pygame.image.load("C:/Users/oatpt/Desktop/py/game/pygame_tutorials-main/Menu/images/button_options.png").convert_alpha()
quit_img = pygame.image.load("C:/Users/oatpt/Desktop/py/game/pygame_tutorials-main/Menu/images/button_quit.png").convert_alpha()
video_img = pygame.image.load('C:/Users/oatpt/Desktop/py/game/pygame_tutorials-main/Menu/images/button_video.png').convert_alpha()
audio_img = pygame.image.load('C:/Users/oatpt/Desktop/py/game/pygame_tutorials-main/Menu/images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('C:/Users/oatpt/Desktop/py/game/pygame_tutorials-main/Menu/images/button_keys.png').convert_alpha()
back_img = pygame.image.load('C:/Users/oatpt/Desktop/py/game/pygame_tutorials-main/Menu/images/button_back.png').convert_alpha()
start_img = pygame.image.load("images/button_start.png").convert_alpha()

#create button instances
start_button = button.Button(284, 115, start_img, 0.8)
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_run == False:
    if menu_state == "main":
      if start_button.draw(screen):
        print(game_run)
        game_run = True
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"
  elif game_paused == True and game_run == True:
    #check menu state
    if menu_state == "pause":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        game_run = False
        menu_state = "main"
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "pause"
  elif game_paused == False and game_run == True:
    draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)
    
  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE and game_paused == False:
        game_paused = True
        menu_state = "pause"
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()