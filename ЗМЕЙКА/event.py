import sys

import pygame

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
def update(bg_color,screen):
    screen.fill(bg_color)
    pygame.display.flip()
