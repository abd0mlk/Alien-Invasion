# A module that initializes the sound effects for the game.

import pygame


class SoundEffects:
    """A class to manage the sound effects in the game."""

    def __init__(self):
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound("sounds/laser.wav")
        self.explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
