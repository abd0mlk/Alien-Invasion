# A module that initializes the sound effects for the game.

import pygame

pygame.mixer.init()

laser_sound = pygame.mixer.Sound("sounds/laser.wav")
explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
