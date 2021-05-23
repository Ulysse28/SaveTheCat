"""
classe enemy
"""

import pygame
import random
from red import Red


class Enemy(pygame.sprite.Sprite ):
    #constructor
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('Assets/characters/triste.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(700, 900)
        self.rect.y =  random.randint(0, 1000)
       # self.position = [x, y]
        self.speed = 1
        self.velocity = [1, -1]
        self.health = 50
        self.max_health = 50
        self.attack = 2
        self.all_reds = pygame.sprite.Group()

    #Gérer les dégats
    def damage(self, amount):
        #infliger les dégats
        self.health -= amount

        #vérifier si son nouveau nombre de point de vie est inférieur ou égale à 0
        if self.health <= 0:
            #le faire réapparaitre
            self.rect.y =  0
            self.health = self.max_health

    #méthode de déplacement
    def move(self):
        #si il n'y a pas de collisisons
        if not self.game.chack_collisions(self, self.game.all_players) and not self.game.chack_collisions(self, self.game.all_walls):
            self.rect.x -= self.speed
        if self.rect.x <0 or self.game.chack_collisions(self, self.game.all_walls):
            self.rect.x = 800

    #Barre de vie
    def update_health_bar(self, screen):
        #couleur de la bar de vie

        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)

        bar_position = [self.rect.x - 10, self.rect.y - 5, self.health,5]
        back_bar_position =[self.rect.x - 10, self.rect.y - 5, self.max_health,5]
        #dessiner la barre de vie

        pygame.draw.rect(screen, back_bar_color, back_bar_position)
        pygame.draw.rect(screen, bar_color, bar_position)

    def remove(self):
        self.game.all_enemy.remove(self)

        # Lancer des projectiles
    def launch_projectile(self):
        self.all_reds.add(Red(self.game, self))
        print('ok')

