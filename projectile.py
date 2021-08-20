"""
Classe Projectile
"""
import pygame

class Projectile(pygame.sprite.Sprite):
    #Constructor
    def __init__(self,player, game):
        super().__init__()
        self.game = game
        self.player = player
        self.image = pygame.image.load('Assets/characters/blue_circle.png')
        self.rect = self.image.get_rect()
        self.speed = 5
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y

    #Supprimer des projectiles
    def remove(self):
        self.player.all_projectiles.remove(self)

    def move_selon_image(self):
            if self.game.up == True:
                self.rect.y -= 10
            if self.game.down:
                self.rect.y += 10
            if self.game.right:
                for enemy in self.game.chack_collisions(self, self.game.all_enemy):
                    self.remove()
                    enemy.damage(self.player.attack)
                self.rect.x += self.speed
            if self.game.left:
                for enemy in self.game.chack_collisions(self, self.game.all_enemy):
                    self.remove()
                    enemy.damage(self.player.attack)
                self.rect.x-= self.speed
            if self.rect.x> 1000:
                self.remove()