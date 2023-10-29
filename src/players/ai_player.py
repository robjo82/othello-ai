import copy
import time

from src import settings
from src.board import Board
from src.players.player import Player

MAX_SCORE = 1000000


class AIPlayer(Player):

    def __init__(self, color, ai_type, evaluating_method, max_timeout=settings.MAX_TIMEOUT, depth=6):
        super().__init__(color)  # AI always plays as 'B'
        self.depth = depth
        self.max_timeout = max_timeout
        self.ai_type = ai_type
        self.evaluating_method = evaluating_method
        self.transposition_table = {}

    def make_move(self, board, show_ai_moves=True, show_score_during_thinking=False, standby_duration=0.2):
        print("AI is thinking...")
        move_to_make = []

        if self.ai_type == list(settings.AVAILABLE_AIS.keys())[0]:
            available_cells = board.available_cells(self.color)

            move_to_make = self.min_max(
                board=board,
                maximizing=True,
                timeout=time.time() + self.max_timeout,
                available_moves=available_cells,
                depth=self.depth,
                standby_duration=standby_duration,
                show_ai_moves=show_ai_moves,
                show_score_during_thinking=show_score_during_thinking
            )[1]

        elif self.ai_type == list(settings.AVAILABLE_AIS.keys())[1]:

            move_to_make = self.alpha_beta(
                board=board,
                alpha=float('-inf'),
                beta=float('inf'),
                maximizing=True,
                timeout=time.time() + self.max_timeout,
                depth=self.depth,
                standby_duration=standby_duration,
                show_ai_moves=show_ai_moves,
                show_score_during_thinking=show_score_during_thinking
            )[1]

        print("AI has found a move")

        if move_to_make is not None:
            if board.add_move_to_board(move_to_make[0], move_to_make[1], self.color):
                print("AI made a move: ", move_to_make)
                return True
        else:
            return False

    def min_max(self, board, maximizing, timeout, available_moves, depth, standby_duration=0.2,
                show_ai_moves=True, show_score_during_thinking=False):
        print("Entering minmax with memory")
        if show_ai_moves:
            board.display_ia_thinking(show_score_during_thinking)
            time.sleep(standby_duration)

        opponent = 'W' if self.color == 'B' else 'B'
        best_move = None
        board_str = ''.join(''.join(row) for row in board.board) + self.color

        if self.depth == 0:
            print("depth = 0")
            return board.evaluate_board(self), None

        if time.time() >= timeout:
            print("timeout")

            if not available_moves:
                print("no available moves")
                return board.evaluate_board(self), (-1, -1)

            best_move = available_moves[0]
            print("best move: ", best_move)
            return board.evaluate_board(self), best_move

        if board_str in self.transposition_table:
            print("board in memo")
            return self.transposition_table[board_str]

        if maximizing:
            max_eval = -MAX_SCORE

            for move in available_moves:
                x, y = move
                new_board = Board(to_display=False)
                new_board.board = copy.deepcopy(board.board)

                if new_board.add_move_to_board(x, y, self.color):
                    eval_value, _ = self.min_max(new_board, False, timeout, available_moves, depth=depth - 1,
                                                 standby_duration=standby_duration, show_ai_moves=show_ai_moves,
                                                 show_score_during_thinking=show_score_during_thinking)

                    if eval_value is None:
                        available_moves.append((x, y))

                    elif eval_value > max_eval:
                        max_eval = eval_value
                        best_move = (x, y)

            if best_move is None:
                best_move = available_moves[0]
                max_eval = board.evaluate_board(self)

            self.transposition_table[board_str] = max_eval, best_move

            print("Maximizing. Maximal evaluation: ", max_eval)
            print("best move: ", best_move)

            return max_eval, best_move

        else:
            min_eval = MAX_SCORE

            for move in available_moves:
                x, y = move
                new_board = Board(to_display=False)
                new_board.board = copy.deepcopy(board.board)

                if new_board.add_move_to_board(x, y, opponent):
                    eval_value, _ = self.min_max(new_board, True, timeout, available_moves, depth=depth - 1,
                                                 standby_duration=standby_duration, show_ai_moves=show_ai_moves,
                                                 show_score_during_thinking=show_score_during_thinking)

                    if eval_value is None:
                        available_moves.append((x, y))

                    elif eval_value < min_eval:
                        min_eval = eval_value
                        best_move = (x, y)

            if best_move is None:
                best_move = available_moves[0]
                min_eval = board.evaluate_board(self)

            self.transposition_table[board_str] = min_eval, best_move

            print("Minimizing. Minimal evaluation: ", min_eval)
            print("best move: ", best_move)

            return min_eval, best_move

    def alpha_beta(self, board, alpha, beta, maximizing, timeout, depth, standby_duration=0.2,
                   show_ai_moves=True, show_score_during_thinking=False):
        print("Entering alpha beta minmax")
        if show_ai_moves:
            board.display_ia_thinking(show_score_during_thinking)
            time.sleep(standby_duration)

        board_str = ''.join(''.join(row) for row in board.board) + self.color
        best_move = None
        current_player = self.color if maximizing else ('W' if self.color == 'B' else 'B')
        best_move_so_far = None

        """if time.time() > timeout:
            print("timeout")
            return None, None"""

        if board_str in self.transposition_table:
            print("board in transposition table : ", self.transposition_table[board_str])
            return self.transposition_table[board_str]

        if depth == 0:
            print("depth = 0")
            score = board.evaluate_board(self)
            # self.transposition_table[board_str] = score, None
            return score, None

        if maximizing:
            max_eval = float('-inf')
            move_found = False

            for x in range(8):

                for y in range(8):
                    new_board = Board(to_display=False)
                    new_board.board = copy.deepcopy(board.board)
                    move_made = new_board.add_move_to_board(x, y, current_player)

                    if move_made:
                        move_found = True  # Update this flag
                        eval_value, _ = self.alpha_beta(board=new_board, alpha=alpha, beta=beta, maximizing=False,
                                                        timeout=timeout, depth=depth - 1,
                                                        standby_duration=standby_duration, show_ai_moves=show_ai_moves,
                                                        show_score_during_thinking=show_score_during_thinking)

                        if eval_value is None:  # Timeout occurred
                            print("timeout")
                            return max_eval, best_move_so_far

                        if eval_value > max_eval:
                            max_eval = eval_value
                            best_move = (x, y)
                            best_move_so_far = best_move

                        alpha = max(alpha, eval_value)

                        if beta <= alpha:
                            break

            if not move_found:  # Check the flag here
                print("no available moves")
                return board.evaluate_board(self), None

            self.transposition_table[board_str] = max_eval, best_move

            print("Maximizing. Maximal evaluation: ", max_eval)
            return max_eval, best_move

        else:
            min_eval = float('inf')
            move_found = False

            for x in range(8):

                for y in range(8):

                    new_board = Board(to_display=False)
                    new_board.board = copy.deepcopy(board.board)
                    move_made = new_board.add_move_to_board(x, y, current_player)

                    if move_made:
                        move_found = True

                        eval_value, _ = self.alpha_beta(board=new_board, alpha=alpha, beta=beta, maximizing=True,
                                                        timeout=timeout, depth=depth - 1,
                                                        standby_duration=standby_duration, show_ai_moves=show_ai_moves,
                                                        show_score_during_thinking=show_score_during_thinking)

                        if eval_value is None:  # Timeout occurred
                            print("timeout")
                            return min_eval, best_move_so_far

                        if eval_value < min_eval:
                            min_eval = eval_value
                            best_move = (x, y)
                            best_move_so_far = best_move

                        beta = min(beta, eval_value)

                        if beta <= alpha:
                            break

            if not move_found:  # Check the flag here
                print("no available moves")
                return board.evaluate_board(self), None

            self.transposition_table[board_str] = min_eval, best_move
            print("Minimizing. Minimal evaluation: ", min_eval)
            return min_eval, best_move
