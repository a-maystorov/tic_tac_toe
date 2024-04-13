import pygame


class Player:
    """Class to represent a player in the game."""

    def __init__(self, image_path, symbol):
        """Initialize a player with a specific symbol ('X' or 'O') and image."""
        self.image = pygame.image.load(image_path).convert()
        self.symbol = symbol
        self.rect = self.image.get_rect()

    def draw(self, screen, center_position):
        """Draw the player's symbol at the cell center position."""
        self.rect.center = center_position
        screen.blit(self.image, self.rect)
