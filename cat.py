"""
Class Cat
"""

import pygame
from player import Player


class Cat(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load('Assets/characters/cat.png')
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 500
        self.game = game
        self.speed = 2
        self.velocity=[1, -1]

    def move(self):
        if abs(self.game.player.rect.x - self.rect.x) < 50:

            if self.game.player.rect.x < self.rect.x:
                self.rect.x += self.speed * self.velocity[1]
                print("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
            if self.game.player.rect.x > self.rect.x:
                self.rect.x += self.speed * self.velocity[0]
            if self.game.player.rect.y < self.rect.y:
                self.rect.y += self.speed * self.velocity[1]
            if self.game.player.rect.y > self.rect.y:
                self.rect.y += self.speed * self.velocity[0]
