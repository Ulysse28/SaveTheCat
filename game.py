"""
Class Game
"""

import pygame
import pytmx
import pyscroll
from player import Player
from enemy import Enemy
from walls import Walls
from cat import Cat



class Game:

    #Constructor
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.enemy = Enemy(self)
        self.up =False
        self.down = False
        self.right = False
        self.left = False


        # Charger la carte
        tmx_data = pytmx.util_pygame.load_pygame('Assets/maps/map-leve1.2.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, screen.get_size())

        # Dessiner le groupe de calques de la carte
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)

        # générer un joueur
        player_position = tmx_data.get_object_by_name("player")
        self.all_players = pygame.sprite.Group()
        self.player = Player(player_position.x, player_position.y, self)
        self.all_players.add(self.player)
        self.player.update()
        self.group.add(self.player)

        self.cat = Cat(self)
        self.group.add(self.cat)

        #générer les enemis
        self.all_enemy = pygame.sprite.Group()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()




        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()


        #générer un mur
        self.all_walls = pygame.sprite.Group()
        self.spawn_walls()
        self.spawn_walls()
        self.spawn_walls()
        self.spawn_walls()
        self.spawn_walls()
        #self.image_walls = pygame.image.load("Assets/characters/walls.png")
        #self.rect = self.image_walls.get_rect(x =0,  y= 0)
        #self.level1 = pygame.image.load('Assets/levels_images/one.png')
        #self.rect1 = self.level1.get_rect(x=200, y=300)








    #Gérer les événements du jeu

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            #Si le joeur appuie sur espace il lance des projectiles
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.launch_projectile()








        #déplacemment du joueur
        pressed = pygame.key.get_pressed()
        #En haut
        if pressed[pygame.K_UP]:

            self.player.move_up()
            self.player.change_animations('up')
            self.up = True
            self.down = False
            self.right = False
            self.left = False


        #En bas
        elif pressed[pygame.K_DOWN]:

            self.player.change_animations('down')
            self.player.move_down()
            self.up = False
            self.down = True
            self.right = False
            self.left = False

        #A droite
        elif pressed[pygame.K_RIGHT]:

            self.player.change_animations('right')
            self.player.move_right()
            self.up = False
            self.down = False
            self.right = True
            self.left = False

        #A gauche
        elif pressed[pygame.K_LEFT]:
            self.player.change_animations('left')
            self.player.move_left()
            self.up = False
            self.down = False
            self.right = False
            self.left = True




    #Fonction d'affichage
    def display(self):
        pygame.display.flip()
        self.screen.fill('white')







        #Dessiner le groupe(joueur)
        self.group.draw(self.screen)

        self.player.update_health_bar(self.screen)
        self.player.collision()

        #Dessiner les ennemis
        self.all_enemy.draw(self.screen)


        #Dessiner les projectiles
        self.player.all_projectiles.draw(self.screen)
        self.enemy.all_reds.draw(self.screen)

        self.all_walls.draw(self.screen)

        #Faire bouger les enenmis
        for enemy in self.all_enemy:
            enemy.move()
            enemy.update_health_bar(self.screen)

        #Faire bouger les projectiles
        for projectile in self.player.all_projectiles:
            projectile.move_selon_image()
            #projectile.move()

        for red in self.enemy.all_reds:
            red.move()
        self.cat.move()

    #boucle du jeu
    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            #self.handle_input()
            self.handling_events()
            self.display()
            #self.screen.blit(self.image_walls, self.rect)
            #pressed = pygame.key.get_pressed()
           # if pressed[pygame.K_a]:
                #self.rect.x = 200
            clock.tick(50)
            self.enemy.launch_projectile()

    
    #Méthodes pour créer des ennemis
    def spawn_enemy(self):
        enemy = Enemy(self)
        self.all_enemy.add(enemy)

    #Détecter si il y a des collisions entre un sprite et un groupe de sprite
    def chack_collisions(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_walls(self):
        wall = Walls()
        self.all_walls.add(wall)



