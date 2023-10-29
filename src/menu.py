import sys

import pygame

import game_modes

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Menu de jeu")

# Couleurs
vert = (42, 81, 45)
blanc = (255, 255, 255)
bleu_clair = (161, 212, 164)  # Couleur bleu clair
noir = (0, 0, 0)

# Police de texte
police = pygame.font.Font(None, 36)

# Texte des options
options = ["Joueur vs. Joueur", "Joueur vs. IA", "IA vs. IA", "Quitter"]  # Ajout de "Quitter"
selected_option = None

# Titre du jeu
titre_police = pygame.font.Font(None, 72)
titre = titre_police.render("Othello", True, noir)
titre_rect = titre.get_rect()
titre_rect.center = (largeur // 2, 50)


def afficher_menu():
    fenetre.fill(vert)
    fenetre.blit(titre, titre_rect)  # Affichage du titre en haut

    for i, option in enumerate(options):
        bouton = pygame.Rect(largeur // 4, 150 + i * 80, largeur // 2, 60)
        if selected_option == i:
            pygame.draw.rect(fenetre, bleu_clair,
                             bouton)  # Utilisation de la couleur bleu clair pour l'option sélectionnée
        else:
            pygame.draw.rect(fenetre, blanc, bouton)
        texte = police.render(option, True, noir)
        texte_rect = texte.get_rect()
        texte_rect.center = bouton.center
        fenetre.blit(texte, texte_rect)


def main():
    global selected_option
    en_jeu = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                for i, option in enumerate(options):
                    bouton = pygame.Rect(largeur // 4, 150 + i * 80, largeur // 2, 60)
                    if bouton.collidepoint(x, y):
                        selected_option = i
                        if selected_option == 0:
                            print("Lancement du jeu Joueur vs. Joueur")
                            game_modes.game_pvp()
                            # Ici, vous pouvez lancer votre jeu Joueur vs. Joueur
                        elif selected_option == 1:
                            print("Lancement du jeu Joueur vs. IA")
                            game_modes.game_pvai()
                            # Ici, vous pouvez lancer votre jeu Joueur vs. IA
                        elif selected_option == 2:
                            print("Lancement du jeu IA vs. IA")
                            # Ici, vous pouvez lancer votre jeu IA vs. IA
                        elif selected_option == 3:
                            pygame.quit()
                            sys.exit()

        if not en_jeu:
            afficher_menu()

        pygame.display.flip()


if __name__ == "__main__":
    main()
