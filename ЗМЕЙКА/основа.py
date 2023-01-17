import sys
from zmea import Zmea
import pygame,event
import time
import fruits
from fruits import Yabloko
def run():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Змейка")
    zmea = Zmea(screen)
    bg_color = (0,255,0)
    #screen.fill(bg_color)
    #pygame.display.flip()
    zmea.draw_zm()
    while True:
        event.update(bg_color,screen)
        apple = Yabloko(screen)
        apple.draw()
        apple.update_apple()
run()