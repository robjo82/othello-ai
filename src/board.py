import pygame

from src import settings


def init_board():
    board = [['_' for _ in range(settings.BOARD_SIZE)] for _ in range(settings.BOARD_SIZE)]
    board[3][3], board[4][4] = 'W', 'W'
    board[3][4], board[4][3] = 'B', 'B'
    return board


def display_background_and_title(title=settings.CAPTION):
    window = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    window.fill(settings.GREEN)

    title = settings.TITLE_FONT.render(title, True, settings.BLACK)

    window.blit(
        title,
        title.get_rect(center=(settings.WINDOW_WIDTH // 2, 50))
    )

    pygame.display.flip()

    return window


class Board:
    def __init__(self, to_display=True):
        self.board = init_board()
        if to_display:
            self.window = display_background_and_title()

    def display_board(self):
        self.window = display_background_and_title()
        for row in range(settings.BOARD_SIZE):
            for column in range(settings.BOARD_SIZE):
                pygame.draw.rect(
                    self.window,
                    settings.LIGHT_BLUE,
                    pygame.Rect(
                        settings.LEFT_GRID_PADDING + column * settings.BOARD_CELL_SIZE,
                        settings.TOP_GRID_PADDING + row * settings.BOARD_CELL_SIZE,
                        settings.BOARD_CELL_SIZE,
                        settings.BOARD_CELL_SIZE
                    ),
                    1
                )
                pygame.draw.circle(
                    self.window,
                    settings.BLACK if self.board[row][column] == 'B' else settings.WHITE if self.board[row][
                                                                                                column] == 'W' else settings.GREEN,
                    (
                        settings.LEFT_GRID_PADDING + column * settings.BOARD_CELL_SIZE + settings.BOARD_CELL_SIZE // 2,
                        settings.TOP_GRID_PADDING + row * settings.BOARD_CELL_SIZE + settings.BOARD_CELL_SIZE // 2
                    ),
                    settings.BOARD_CELL_SIZE // 2 - 5
                )

        pygame.display.flip()

    def display_ia_thinking(self, show_score_during_thinking=False):
        self.display_board()
        if show_score_during_thinking:
            self.display_score()
        thinking_text = settings.FONT.render(
            "L'IA réfléchit...",
            True,
            settings.BLACK
        )
        thinking_rect = pygame.Rect(
            0,
            settings.WINDOW_HEIGHT - 100,
            settings.WINDOW_WIDTH,
            50
        )

        self.window.blit(
            thinking_text,
            thinking_text.get_rect(center=thinking_rect.center)
        )

        pygame.display.flip()

    def display_score(self):
        black_score = sum(row.count('B') for row in self.board)
        white_score = sum(row.count('W') for row in self.board)
        total_score = black_score + white_score
        player_turn = 'noir' if total_score % 2 == 0 else 'blanc'

        texts = [
            (f"Noir: {black_score}", 20),
            (f"Blanc: {white_score}", 60),
            (f"Tour: {total_score}", 100),
            (f"Joueur: {player_turn}", 140)
        ]

        for text, y_position in texts:
            rendered_text = settings.FONT.render(text, True, settings.BLACK)
            self.window.blit(rendered_text, rendered_text.get_rect(topright=(settings.WINDOW_WIDTH - 20, y_position)))

        button_texts = ["Quitter", "Rejouer"]
        for i, button_text in enumerate(button_texts):
            pygame.draw.rect(self.window, settings.LIGHT_BLUE,
                             (settings.WINDOW_WIDTH - 100, settings.WINDOW_HEIGHT - 60 - i * 60, 80, 40))
            rendered_button_text = settings.FONT.render(button_text, True, settings.BLACK)
            self.window.blit(rendered_button_text, rendered_button_text.get_rect(
                center=(settings.WINDOW_WIDTH - 60, settings.WINDOW_HEIGHT - 40 - i * 60)))

        pygame.display.flip()

    def display_winner(self):
        self.display_board()

        black_score = sum(row.count('B') for row in self.board)
        white_score = sum(row.count('W') for row in self.board)

        winner = 'noir' if black_score > white_score else 'blanc' if white_score > black_score else 'aucun'
        winner_text = settings.FONT.render(
            "Match nul !" if winner == 'aucun' else f"Le gagnant est le joueur {winner} !",
            True,
            settings.BLACK
        )
        winner_rect = pygame.Rect(
            0,
            settings.WINDOW_HEIGHT - 100,
            settings.WINDOW_WIDTH,
            50
        )

        pygame.draw.rect(
            self.window,
            settings.GREEN,
            winner_rect
        )

        self.window.blit(
            winner_text,
            winner_text.get_rect(center=winner_rect.center)
        )

        pygame.display.flip()

    def display_invalid_move(self):
        invalid_move_text = settings.FONT.render(
            "Coup invalide !",
            True,
            settings.BLACK
        )
        invalid_move_rect = pygame.Rect(
            0,
            settings.WINDOW_HEIGHT - 100,
            settings.WINDOW_WIDTH,
            50
        )

        self.window.blit(
            invalid_move_text,
            invalid_move_text.get_rect(center=invalid_move_rect.center)
        )

        pygame.display.flip()

    def display_turn_skipped(self):
        turn_skipped_text = settings.FONT.render(
            "Aucun coup n'est disponible ! Vous passez votre tour.",
            True,
            settings.BLACK
        )
        turn_skipped_rect = pygame.Rect(
            0,
            settings.WINDOW_HEIGHT - 100,
            settings.WINDOW_WIDTH,
            50
        )

        self.window.blit(
            turn_skipped_text,
            turn_skipped_text.get_rect(center=turn_skipped_rect.center)
        )

        pygame.display.flip()

    def available_cells(self, player):
        positions = []
        for x in range(8):
            for y in range(8):
                if self.is_valid_move(x, y, player)[0]:
                    positions.append((x, y))
        return positions

    def is_valid_move(self, x, y, player):
        opponent = 'W' if player == 'B' else 'B'
        flipped_cells = []

        # List of possible directions
        directions = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]

        # Verify that the cell is empty
        if self.board[x][y] != '_':
            return False, []

        # For each direction
        for dx, dy in directions:
            # List of opponent cells to flip
            temp_flips = []

            # Coordinates of the next cell in the direction
            nx, ny = x + dx, y + dy

            while 0 <= nx < 8 and 0 <= ny < 8:
                if self.board[nx][ny] == opponent:
                    # If the next cell is an opponent cell, add it to the list of opponent cells to flip
                    temp_flips.append((nx, ny))

                elif self.board[nx][ny] == player:
                    if temp_flips:
                        # If the next cell is a player cell and there are opponent cells to flip, the move is valid
                        flipped_cells.extend(temp_flips)
                    break
                else:
                    break  # If the next cell is empty, the move is invalid
                # Move to the next cell in the direction
                nx += dx
                ny += dy

        # If there are opponent cells to flip, the move is valid
        return len(flipped_cells) > 0, flipped_cells

    def find_player(self):
        return 'B' if sum(row.count('B') for row in self.board) == sum(row.count('W') for row in self.board) else 'W'

    def evaluate_board(self, ai_player):
        if ai_player.evaluating_method == settings.AVAILABLE_AIS[ai_player.ai_type][0]:
            return self.evaluate_board_by_position(ai_player, 1)

        elif ai_player.evaluating_method == settings.AVAILABLE_AIS[ai_player.ai_type][1]:
            return self.evaluate_board_by_position(ai_player, 2)

        elif ai_player.evaluating_method == settings.AVAILABLE_AIS[ai_player.ai_type][2]:
            return self.evaluate_board_by_score(ai_player)

        elif ai_player.evaluating_method == settings.AVAILABLE_AIS[ai_player.ai_type][3]:
            return self.evaluate_board_by_mobility(ai_player)

    def evaluate_board_by_score(self, ai_player):

        player_score = sum(cell == ai_player.color for row in self.board for cell in row)
        opponent_score = sum(cell != ' ' and cell != ai_player.color for row in self.board for cell in row)

        return player_score - opponent_score

    def evaluate_board_by_mobility(self, ai_player):
        opponent = 'W' if ai_player.color == 'B' else 'B'

        # Weights
        mobility_weight = 1.0  # Maximizes the player's mobility
        opponent_mobility_weight = -1.0  # Minimizes the opponent's mobility
        corner_weight = 10.0  # Maximizes the number of corners taken by the player

        # Count the number of moves available for the player and the opponent
        player_mobility = len(self.available_cells(ai_player.color))
        opponent_mobility = len(self.available_cells(opponent))

        # Count the number of corners taken by the player and the opponent

        player_corners = [self.board[0][0], self.board[0][7], self.board[7][0], self.board[7][7]].count(ai_player.color)
        opponent_corners = [self.board[0][0], self.board[0][7], self.board[7][0], self.board[7][7]].count(opponent)

        # Compute the score
        return (
                mobility_weight * player_mobility +
                opponent_mobility_weight * opponent_mobility +
                corner_weight * (player_corners - opponent_corners)
        )

    def evaluate_board_by_position(self, ai_player, version):
        player_score = 0
        opponent_score = 0
        position_values = []
        opponent = 'W' if ai_player.color == 'B' else 'B'

        # Board position values to prioritize corners and edges
        if version == 1:
            position_values = [
                [500, -150, 30, 10, 10, 30, -150, 500],
                [-150, -250, 0, 0, 0, 0, -250, -150],
                [30, 0, 1, 2, 2, 1, 0, 30],
                [10, 0, 2, 16, 16, 2, 0, 10],
                [10, 0, 2, 16, 16, 2, 0, 10],
                [30, 0, 1, 2, 2, 1, 0, 30],
                [-150, -250, 0, 0, 0, 0, -250, -150],
                [500, -150, 30, 10, 10, 30, -150, 500],
            ]
        elif version == 2:
            position_values = [
                [100, -20, 10, 5, 5, 10, -20, 100],
                [-20, -50, -2, -2, -2, -2, -50, -20],
                [10, -2, -1, -1, -1, -1, -2, 10],
                [5, -2, -1, -1, -1, -1, -2, 5],
                [5, -2, -1, -1, -1, -1, -2, 5],
                [10, -2, -1, -1, -1, -1, -2, 10],
                [-20, -50, -2, -2, -2, -2, -50, -20],
                [100, -20, 10, 5, 5, 10, -20, 100],
            ]

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == ai_player.color:
                    player_score += position_values[i][j]
                elif self.board[i][j] == opponent:
                    opponent_score += position_values[i][j]

        return player_score - opponent_score

    def add_move_to_board(self, x, y, player):
        if player is None:
            player = self.find_player()

        is_valid, flipped_cells = self.is_valid_move(x, y, player)

        if is_valid:
            self.board[x][y] = player

            for fx, fy in flipped_cells:
                self.board[fx][fy] = player

        return is_valid

    def board_is_full(self):
        return all(cell != '_' for row in self.board for cell in row)
