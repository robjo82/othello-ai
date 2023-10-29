import sys
import time

import pygame

import main
import menu

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu Othello")

# Couleurs
vert = (42, 81, 45)
blanc = (255, 255, 255)
bleu_clair = (161, 212, 164)  # Couleur bleu clair
noir = (0, 0, 0)

# Police de texte
police = pygame.font.Font(None, 36)

# Titre du jeu
titre_police = pygame.font.Font(None, 72)
titre = titre_police.render("Othello", True, noir)
titre_rect = titre.get_rect()
titre_rect.center = (largeur // 2, 50)


def afficher_grille(board):
    fenetre.fill(vert)
    fenetre.blit(titre, titre_rect)  # Affichage du titre en haut

    taille_grille = len(board)
    taille_case = 50

    # Calcul des coordonnées pour centrer le tableau de jeu
    x_debut = (largeur - (taille_grille * taille_case)) // 2
    y_debut = (hauteur - (taille_grille * taille_case)) // 2

    for row in range(taille_grille):
        for col in range(taille_grille):
            x = x_debut + col * taille_case
            y = y_debut + row * taille_case

            # Dessiner un rectangle autour de chaque case
            pygame.draw.rect(fenetre, bleu_clair, (x, y, taille_case, taille_case), 1)

            # Dessiner les pions
            if board[row][col] == 'B':
                pygame.draw.circle(fenetre, noir, (x + taille_case // 2, y + taille_case // 2), taille_case // 2 - 5)
            elif board[row][col] == 'W':
                pygame.draw.circle(fenetre, blanc, (x + taille_case // 2, y + taille_case // 2), taille_case // 2 - 5)


def afficher_info(tour, pions_noirs, pions_blancs, player_turn):
    # Affichage du décompte des tours
    tour_texte = police.render(f"Tour : {tour}", True, noir)
    tour_texte_rect = tour_texte.get_rect()
    tour_texte_rect.topright = (largeur - 20, 20)
    fenetre.blit(tour_texte, tour_texte_rect)

    # Affichage du nombre de pions noirs et blancs
    pions_noirs_texte = police.render(f"Noirs : {pions_noirs}", True, noir)
    pions_noirs_texte_rect = pions_noirs_texte.get_rect()
    pions_noirs_texte_rect.topright = (largeur - 20, 60)
    fenetre.blit(pions_noirs_texte, pions_noirs_texte_rect)

    pions_blancs_texte = police.render(f"Blancs : {pions_blancs}", True, noir)
    pions_blancs_texte_rect = pions_blancs_texte.get_rect()
    pions_blancs_texte_rect.topright = (largeur - 20, 100)
    fenetre.blit(pions_blancs_texte, pions_blancs_texte_rect)

    # Affichage du joueur actuel
    joueur_texte = police.render(f"Joueur : {player_turn}", True, noir)
    joueur_texte_rect = joueur_texte.get_rect()
    joueur_texte_rect.topright = (largeur - 20, 140)
    fenetre.blit(joueur_texte, joueur_texte_rect)

    # Bouton "Retour" sous la grille de jeu
    pygame.draw.rect(fenetre, bleu_clair, (largeur - 100, hauteur - 60, 80, 40))
    retour_texte = police.render("Retour", True, noir)
    retour_texte_rect = retour_texte.get_rect()
    retour_texte_rect.center = (largeur - 60, hauteur - 40)
    fenetre.blit(retour_texte, retour_texte_rect)


def afficher_bouton_rejouer():
    # Bouton "Rejouer" sous la grille de jeu
    pygame.draw.rect(fenetre, bleu_clair, (largeur - 100, hauteur - 60, 80, 40))
    retour_texte = police.render("Rejouer", True, noir)
    retour_texte_rect = retour_texte.get_rect()
    retour_texte_rect.center = (largeur - 60, hauteur - 40)
    fenetre.blit(retour_texte, retour_texte_rect)


def afficher_victoire(board, player):
    # Créez un rectangle pour afficher le message de victoire
    victoire_rect = pygame.Rect(0, hauteur - 100, largeur, 50)

    afficher_grille(board)
    # Remplissez le rectangle avec une couleur de fond
    pygame.draw.rect(fenetre, vert, victoire_rect)

    # Utilisez la police de texte pour afficher le message de victoire
    if player == 'Egalité':
        victoire_texte = police.render("Egalité !", True, noir)
    elif player == 'Timeout':
        victoire_texte = police.render("Timeout !", True, noir)
    else:
        victoire_texte = police.render(f"Bravo, le joueur {player} a gagné !", True, noir)
    victoire_texte_rect = victoire_texte.get_rect()
    victoire_texte_rect.center = victoire_rect.center

    # Affichez le texte de victoire dans le rectangle
    fenetre.blit(victoire_texte, victoire_texte_rect)


def game_pvp():
    board = main.init_board()
    player_turn = 'B'  # Commencez avec les Noirs

    taille_grille = len(board)
    taille_case = 50

    x_debut = (largeur - (taille_grille * taille_case)) // 2
    y_debut = (hauteur - (taille_grille * taille_case)) // 2

    tour = 0  # Initialisez le décompte des tours
    pions_noirs = 2  # Initialisez le nombre de pions noirs
    pions_blancs = 2  # Initialisez le nombre de pions blancs

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Obtenez les coordonnées du clic de souris
                x, y = pygame.mouse.get_pos()

                if largeur - 100 <= x <= largeur - 20 and hauteur - 60 <= y <= hauteur - 20:
                    menu.main()  # Appeler menu.main() lorsque le bouton "Retour" est cliqué

                # Convertissez les coordonnées de la souris en coordonnées de case
                x_case = (x - x_debut) // taille_case
                y_case = (y - y_debut) // taille_case

                # Vérifiez si le coup est valide
                is_valid, _ = main.is_valid_move(board, y_case, x_case, player_turn)

                if is_valid:
                    # Mettez à jour le plateau avec le coup
                    main.make_move(board, y_case, x_case, player_turn)

                    # Mettez à jour le décompte des tours
                    tour += 1

                    # Mettez à jour le nombre de pions de chaque couleur
                    pions_noirs = sum(row.count('B') for row in board)
                    pions_blancs = sum(row.count('W') for row in board)

                    # Passez au tour suivant
                    player_turn = 'W' if player_turn == 'B' else 'B'

        # Affichez le plateau mis à jour et les informations
        afficher_grille(board)
        afficher_info(tour, pions_noirs, pions_blancs, player_turn)
        pygame.display.flip()

        # Vérifiez si la partie est terminée   
        if not main.has_valid_move(board, 'B') and not main.has_valid_move(board, 'W'):
            print("Fin de la partie car plus de coups possibles")
            if pions_noirs > pions_blancs:
                afficher_victoire(board, 'Noir')
                afficher_info(tour, pions_noirs, pions_blancs, player_turn)
            elif pions_blancs > pions_noirs:
                afficher_victoire(board, 'Blanc')
                afficher_info(tour, pions_noirs, pions_blancs, player_turn)
            else:
                afficher_victoire(board, 'Égalité')
                afficher_info(tour, pions_noirs, pions_blancs, player_turn)
            pygame.display.flip()
            pygame.time.delay(5000)  # Pause de 3 secondes pour afficher le résultat
            # return  # Sortez de la boucle de jeu
        elif not main.has_valid_move(board, 'B') and player_turn == 'B':
            print("changement de joueur de B à W")
            player_turn = 'W'
        elif not main.has_valid_move(board, 'W') and player_turn == 'W':
            player_turn = 'B'
            print("changement de joueur de W à B")


def game_pvai():
    board = main.init_board()
    player_turn = 'B'  # Commencez avec les Noirs

    # Initialisation de la grille et d'autres paramètres
    taille_grille = len(board)
    taille_case = 50
    x_debut = (largeur - (taille_grille * taille_case)) // 2
    y_debut = (hauteur - (taille_grille * taille_case)) // 2
    tour = 0  # Initialisez le décompte des tours
    pions_noirs = 2  # Initialisez le nombre de pions noirs
    pions_blancs = 2  # Initialisez le nombre de pions blancs

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                x_case = (x - x_debut) // taille_case
                y_case = (y - y_debut) // taille_case

                if largeur - 100 <= x <= largeur - 20 and hauteur - 60 <= y <= hauteur - 20:
                    menu.main()  # Appeler menu.main() lorsque le bouton "Retour" est cliqué

                is_valid, _ = main.is_valid_move(board, y_case, x_case, player_turn)

                if is_valid:
                    main.make_move(board, y_case, x_case, player_turn)
                    tour += 1
                    pions_noirs = sum(row.count('B') for row in board)
                    pions_blancs = sum(row.count('W') for row in board)

                    if all(cell != ' ' for row in board for cell in row) or (
                            not main.has_valid_move(board, 'B') and not main.has_valid_move(board,
                                                                                            'W')):
                        print("Fin de la partie car plus de coups possibles")
                        if pions_noirs > pions_blancs:
                            afficher_victoire(board, 'Noir')
                            afficher_info(tour, pions_noirs, pions_blancs, player_turn)
                        elif pions_blancs > pions_noirs:
                            afficher_victoire(board, 'Blanc')
                            afficher_info(tour, pions_noirs, pions_blancs, player_turn)
                        else:
                            afficher_victoire(board, 'Égalité')
                            afficher_info(tour, pions_noirs, pions_blancs, player_turn)
                        pygame.display.flip()
                        pygame.time.delay(5000)  # Pause de 5 secondes pour afficher le résultat
                        break  # Fin de la partie
                    elif player_turn == 'W':
                        if main.has_valid_move(board, 'B'):
                            player_turn = 'B'
                        elif main.has_valid_move(board, 'W'):
                            print("On passe le tour du joueur Noir")
                            player_turn = 'W'
                        else:
                            print("fin de partie")
                            break
                    elif player_turn == 'B':
                        if main.has_valid_move(board, 'W'):
                            player_turn = 'W'
                        elif main.has_valid_move(board, 'B'):
                            print("On passe le tour du joueur Blanc")
                            player_turn = 'B'
                        else:
                            print("fin de partie")
                            break
                    afficher_grille(board)
                    afficher_info(tour, pions_noirs, pions_blancs, player_turn)
                    pygame.display.flip()
                    # pygame.time.delay(500)  # Pause de 1 seconde pour afficher le résultat

        if player_turn == 'B':
            timeout = time.time() + 5  # 2 secondes de time-out pour l'IA
            possible_moves = main.positions_jouables(board, 'B')
            result = main.minmax_with_memory(board, 5, True, 'B', timeout, possible_moves)
            print(result)
            if result is None or result[1] is None or result[1][0] is None or result[1][1] is None or result[0] is None:
                afficher_victoire(board, 'Timeout')
                afficher_info(tour, pions_noirs, pions_blancs, player_turn)
                pygame.display.flip()
                print("AI timeout. Human wins!")
                pygame.time.delay(10000)  # Pause de 5 secondes pour afficher le résultat
                break

            _, (x, y) = result

            main.make_move(board, x, y, player_turn)
            tour += 1
            pions_noirs = sum(row.count('B') for row in board)
            pions_blancs = sum(row.count('W') for row in board)
            if main.has_valid_move(board, 'W'):
                player_turn = 'W'
            elif main.has_valid_move(board, 'B'):
                print("On passe le tour du joueur Blanc")
                player_turn = 'B'
            else:
                afficher_grille(board)
                afficher_info(tour, pions_noirs, pions_blancs, player_turn)
                if pions_blancs > pions_noirs:
                    afficher_victoire(board, 'Blanc')
                    afficher_info(tour, pions_noirs, pions_blancs, player_turn)
                elif pions_noirs > pions_blancs:
                    afficher_victoire(board, 'Noir')
                    afficher_info(tour, pions_noirs, pions_blancs, player_turn)
                elif pions_blancs == pions_noirs:
                    afficher_victoire(board, 'Egalité')
                    afficher_info(tour, pions_noirs, pions_blancs, player_turn)

                pygame.display.flip()
                pygame.time.delay(5000)  # Pause de 5 secondes pour afficher le résultat
                break  # Fin de la partie

        afficher_grille(board)
        afficher_info(tour, pions_noirs, pions_blancs, player_turn)
        pygame.display.flip()


if __name__ == "__main__":
    game_pvai()
