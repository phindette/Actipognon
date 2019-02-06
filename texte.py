import pygame
from constantes import *

class Texte(pygame.sprite.Sprite):
    def __init__(self,game,texte):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.texte = texte
        self._layer = 1
        self.groups = game.les_sprites,game.textes
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.font = pygame.font.SysFont("Arial", 20)
        self.textSurf = self.font.render(self.texte, 1, (0,0,0))
        self.image = pygame.Surface((100, 100))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [100/2 - W/2, 100/2 - H/2])
        self.rect.x = LARGEURFENETRE -100