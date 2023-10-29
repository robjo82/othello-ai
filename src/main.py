from time import sleep

import pygame

from src.board import Board
from src.menu import AIConfig, Menu, AIVisibility
from src.players.ai_player import AIPlayer
from src.players.human_player import HumanPlayer


def main():
    clock = pygame.time.Clock()
    pygame.init()

    # Menu
    menu = Menu()
    chosen_game_mode = menu.run()
    show_ai_moves = False
    standby_duration = 0.2

    # AI Config
    if chosen_game_mode == "Joueur vs. IA" or chosen_game_mode == "IA vs. IA":
        ai_config = AIConfig()
        ai_type, evaluating_method, depth, max_timeout = ai_config.run("First AI param")
        player2 = AIPlayer(color='W', ai_type=ai_type, evaluating_method=evaluating_method, depth=depth,
                           max_timeout=max_timeout)

        if chosen_game_mode == "IA vs. IA":
            ai_type, evaluating_method, depth, max_timeout = ai_config.run("Second AI param")
            player1 = AIPlayer(color='B', ai_type=ai_type, evaluating_method=evaluating_method, depth=depth,
                               max_timeout=max_timeout)

        else:
            player1 = HumanPlayer('B')

        ai_visibility = AIVisibility()
        show_ai_moves, standby_duration = ai_visibility.run()

    else:
        player1 = HumanPlayer('B')
        player2 = HumanPlayer('W')

    board = Board()
    turn_skipped = False
    players = [player1, player2]

    while True:
        for player in players:
            move_made = False

            available_cells = board.available_cells(player.color)
            if len(available_cells) == 0:
                if turn_skipped:
                    board.display_winner()
                    sleep(5)
                    return
                else:
                    turn_skipped = True
                    board.display_turn_skipped()
                    sleep(0.3)
                    break

            while not move_made:  # Boucle pour gérer les coups invalides
                board.display_board()
                board.display_score()

                if isinstance(player, AIPlayer):
                    if chosen_game_mode == "Joueur vs. IA":
                        move_made = player.make_move(board, standby_duration=standby_duration,
                                                     show_ai_moves=show_ai_moves, show_score_during_thinking=False)
                    else:
                        move_made = player.make_move(board, standby_duration=standby_duration,
                                                     show_ai_moves=show_ai_moves, show_score_during_thinking=True)
                else:
                    move_made = player.make_move(board)

                if not move_made:
                    board.display_invalid_move()
                    sleep(0.3)

            turn_skipped = False

            if isinstance(player, AIPlayer):
                sleep(1)

            clock.tick(10)


if __name__ == "__main__":
    main()
