import pygame
import random

class Red(pygame.sprite.Sprite):

    #Constructor
    def __init__(self , game, enemy):
        super().__init__()
        self.game = game

        self.enemy = enemy
        self.image = pygame.image.load('Assets/characters/circle.png')
        self.rect = self.image.get_rect()
        self.speed = 3
        self.rect.x = random.randint(0, 500)
        self.rect.y = random.randint(0, 500)

    #Supprimer des projectiles
    def remove(self):
        self.enemy.all_reds.remove(self)
        print("remove")


    #Faire bouger les ennemis
    def move(self):

        #si il y a collision avec un ennemi, le supprimer
        for player in self.game.chack_collisions(self, self.game.all_players):

            print('collisions')
            self.remove()
            #Infliger des dégats aux enemis
            player.damage(self.enemy.attack)
        for wall in self.game.chack_collisions(self, self.game.all_walls):
            self.remove()
        #le faire monter
        self.rect.y += self.speed
        print(self.rect.y)

        #s'il sort de la fenêtre, le supprimer
        if self.rect.y < -50:
            self.remove()
