import sys

import pygame


class Game:
    """Overall class to manage game assets and behaviour."""

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("Tic Tac Toe")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
