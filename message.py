import pygame.font


class Message:
    def __init__(self, game, msg, font_size, color, center=None):
        """Initialize message attributes."""
        self.screen = game.screen
        self.font = pygame.font.Font(None, font_size)
        self.text_color = color
        self._prep_msg(msg, center)

    def _prep_msg(self, msg, center):
        """Prepare the message image and position it."""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        if center:
            self.msg_image_rect.center = center
        else:
            self.msg_image_rect.center = self.screen.get_rect().center

    def draw(self):
        """Draw the message to the screen."""
        self.screen.blit(self.msg_image, self.msg_image_rect)
