# A module that stores the settings for the Alien Invasion game.


class Settings:
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1346
        self.screen_height = 668
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
