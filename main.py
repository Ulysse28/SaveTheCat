"""
Main file fo the game
By Ulysse Valdenaire
"""
import pygame
from game import Game

pygame.init()
#Music
pygame.mixer.init()
SIFFLEMENT = pygame.mixer.music.load("Assets/music/19th Floor - Bobby Richards.mp3")
pygame.mixer.music.play(1000, 0.0)
#Window of the game
screen = pygame.display.set_mode((800, 650))
#Lauching the game
game = Game(screen)
game.run()