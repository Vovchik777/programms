import pygame
class Zmea():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/zmik.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def draw_zm(self):
        self.screen.blit(self.image, self.rect)
    def update_zm(self):
        pygame.display.flip()