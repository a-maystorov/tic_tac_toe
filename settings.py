class Settings:
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 300
        self.screen_height = 300
        self.bg_color = (255, 255, 255)

        # Grid settings
        self.grid_line_color = (50, 50, 50)
        self.grid_line_width = 6
        self.grid_cell_size = 100
