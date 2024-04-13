import pygame

from player import Player


class Grid:
    """A class to manage the grid."""

    def __init__(self, game):
        """Initialize grid attributes."""
        self.screen = game.screen
        self.settings = game.settings
        self.cells = [[None, None, None] for _ in range(3)]
        self.x_image = pygame.image.load('images/x.png').convert()
        self.o_image = pygame.image.load('images/o.png').convert()
        self.players = {
            'X': Player('images/x.png', 'X'),
            'O': Player('images/o.png', 'O')
        }
        self.current_turn = 'X'

    def _get_center_coords(self, row, col):
        """Calculate the center coordinates of a cell."""
        center_x = col * self.settings.grid_cell_size + self.settings.grid_cell_size // 2
        center_y = row * self.settings.grid_cell_size + self.settings.grid_cell_size // 2
        return center_x, center_y

    def draw(self):
        """Draw the grid and player symbols to the screen."""
        # Draw grid lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.settings.grid_line_color, (0, i * self.settings.grid_cell_size),
                             (self.settings.screen_width, i * self.settings.grid_cell_size), self.settings.grid_line_width)
            pygame.draw.line(self.screen, self.settings.grid_line_color, (i * self.settings.grid_cell_size, 0),
                             (i * self.settings.grid_cell_size, self.settings.screen_height), self.settings.grid_line_width)

        # Draw X and O images
        for row in range(3):
            for col in range(3):
                if self.cells[row][col]:
                    center_x, center_y = self._get_center_coords(row, col)
                    self.players[self.cells[row][col]].draw(
                        self.screen, (center_x, center_y))

    def update(self, mouse_pos):
        """Handle updates to the grid based on mouse clicks."""
        col = mouse_pos[0] // self.settings.grid_cell_size
        row = mouse_pos[1] // self.settings.grid_cell_size
        if self.cells[row][col] is None:
            self.cells[row][col] = self.current_turn
            self.current_turn = 'O' if self.current_turn == 'X' else 'X'
