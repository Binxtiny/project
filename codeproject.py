import pygame 

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
is_fullscreen = False 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run: 
     screen.fill ((0,0,0))
     pygame.display.update()

     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run = False

pygame.quit ()