import pygame

# Initialize Pygame
pygame.init()

# Window settings
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
CAPTION = "Othello"

# Colors
GREEN = (42, 81, 45)
WHITE = (255, 255, 255)
LIGHT_BLUE = (161, 212, 164)
BLACK = (0, 0, 0)

# Text settings
FONT = pygame.font.Font(None, 32)
TITLE_FONT = pygame.font.Font(None, 72)

# Menu settings
OPTIONS = ["Joueur vs. Joueur", "Joueur vs. IA", "IA vs. IA", "Quitter"]

# Game settings
BOARD_SIZE = 8
BOARD_CELL_SIZE = 50
LEFT_GRID_PADDING = (WINDOW_WIDTH - (BOARD_SIZE * BOARD_CELL_SIZE)) // 2
TOP_GRID_PADDING = (WINDOW_HEIGHT - (BOARD_SIZE * BOARD_CELL_SIZE)) // 2
MINIMAX_DEPTH = 2
MAXIMAL_DEPTH = 10
AVAILABLE_AIS = {
    "Minimax": ["Positionnel1", "Positionnel2", "Score", "Mobilité"],
    "Alphabeta": ["Positionnel1", "Positionnel2", "Score", "Mobilité"]
}
MAX_TIMEOUT = 60
MIN_TIMEOUT = 1
