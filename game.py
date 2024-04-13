import sys

import pygame

from settings import Settings
from grid import Grid


class Game:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Tic Tac Toe")

        self.grid = Grid(self)

    def _check_mouse_button_down_events(self, event):
        """Respond to mouse button presses."""
        mouse_pos = event.pos
        self.grid.update(mouse_pos)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse_button_down_events(event)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.grid.draw()

        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run_game()
