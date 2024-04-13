class Settings:
    """A class to store all settings for the game."""

    def __init__(self) -> None:
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 300
        self.screen_height = 300
        self.bg_color = (230, 230, 230)

        # Grid settings
        self.grid_line_color = (50, 50, 50)
        self.grid_line_width = 6
        self.grid_tile_size = 100
