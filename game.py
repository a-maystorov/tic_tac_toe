import sys

import pygame


class Game:
    """Overall class to manage game assets and behaviour."""

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("Tic Tac Toe")

        self.clock = pygame.time.Clock()

        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
