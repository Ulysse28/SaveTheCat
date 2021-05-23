"""
Class Walls
"""

import pygame
import random

class Walls(pygame.sprite.Sprite):

    #Constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/characters/walls.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0, 900)


