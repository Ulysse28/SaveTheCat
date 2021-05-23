"""
classe joueur
"""

import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    #Constructor
    def __init__(self,x ,y, game):
        super().__init__()
        self.game = game
        self.sprite_sheet = pygame.image.load('Assets/characters/player.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x,y]
        self.images = {
            'down' : self.get_image(0, 0),
            'left': self.get_image(0, 34),
            'right': self.get_image(0, 64),
            'up': self.get_image(0 , 96)
        }
        self.speed = 3
        self.all_projectiles = pygame.sprite.Group()
        self.attack = 5
        self.health = 50
        self.max_health = 50
        self.up = False

    #Lancer des projectiles
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self, self.game))


    def update(self):
        self.rect.topleft = self.position

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32 ))
        return image

    """
    Méthodes de déplacement: en haut, en bas, a droite, à gauche
    """
    def move_up(self):

        self.rect.y -= self.speed

    def move_down(self):

        self.rect.y += self.speed
    def move_right(self):
        if not self.game.chack_collisions(self, self.game.all_enemy) and not self.game.chack_collisions(self,
                                                                                                        self.game.all_walls):
            self.rect.x += self.speed
    def move_left(self):

        self.rect.x -= self.speed

    #Changer d'image selon la direction de déplacement du joueur
    def change_animations(self, name):
        self.image = self.images[name]
        self.image.set_colorkey([0, 0, 0])





        # Barre de vie

    def update_health_bar(self, screen):
        # couleur de la bar de vie

        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)

        bar_position = [self.rect.x - 10, self.rect.y - 5, self.health, 5]
        back_bar_position = [self.rect.x - 10, self.rect.y - 5, self.max_health, 5]
        # dessiner la barre de vie

        pygame.draw.rect(screen, back_bar_color, back_bar_position)
        pygame.draw.rect(screen, bar_color, bar_position)

    def damage(self, amount):
        self.health -= amount

    def collision(self):
        if self.game.chack_collisions(self, self.game.all_enemy):
            self.damage(self.game.enemy.attack)



