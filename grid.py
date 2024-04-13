import pygame


class Grid:
    """A class to manage the grid."""

    def __init__(self, game):
        """Initialize grid attributes."""
        self.screen = game.screen
        self.settings = game.settings

    def draw(self):
        """Draw the grid to the screen."""
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.settings.grid_line_color, (0, i * self.settings.grid_tile_size),
                             (self.settings.screen_width, i * self.settings.grid_tile_size), self.settings.grid_line_width)
            pygame.draw.line(self.screen, self.settings.grid_line_color, (i * self.settings.grid_tile_size, 0),
                             (i * self.settings.grid_tile_size, self.settings.screen_height), self.settings.grid_line_width)
