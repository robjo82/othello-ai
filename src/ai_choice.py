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
bleu_clair = (161, 212, 164)
noir = (0, 0, 0)

# Police de texte
police = pygame.font.Font(None, 36)

# Curseur/slider
curseur_min = 2
curseur_max = 10
curseur_valeur = curseur_min
curseur_rect = pygame.Rect(largeur // 4, 450, largeur // 2, 60)

# Texte des options
options = ["Alphabeta1", "Alphabeta2", "Minmax", "Retour au menu principal"]
selected_option = None

# Titre du menu
titre_police = pygame.font.Font(None, 72)
titre = titre_police.render("Nouveau Menu", True, noir)
titre_rect = titre.get_rect()
titre_rect.center = (largeur // 2, 50)


def afficher_menu():
    fenetre.fill(vert)
    fenetre.blit(titre, titre_rect)

    for i, option in enumerate(options):
        bouton = pygame.Rect(largeur // 4, 150 + i * 80, largeur // 2, 60)
        if selected_option == i:
            pygame.draw.rect(fenetre, bleu_clair, bouton)
        else:
            pygame.draw.rect(fenetre, blanc, bouton)
        texte = police.render(option, True, noir)
        texte_rect = texte.get_rect()
        texte_rect.center = bouton.center
        fenetre.blit(texte, texte_rect)

    # Affichage du curseur et de sa valeur
    pygame.draw.rect(fenetre, blanc, curseur_rect)
    position_curseur = (curseur_valeur - curseur_min) / (curseur_max - curseur_min) * (
            curseur_rect.width - 20) + curseur_rect.x + 10
    pygame.draw.rect(fenetre, noir, (position_curseur, curseur_rect.y + 10, 10, 40))

    texte_curseur = police.render(f"Nombre : {curseur_valeur}", True, noir)
    texte_curseur_rect = texte_curseur.get_rect()
    texte_curseur_rect.center = curseur_rect.center
    fenetre.blit(texte_curseur, texte_curseur_rect)


def main():
    global selected_option
    global curseur_valeur
    en_jeu = False
    curseur_dragging = False
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
                            print("Lancement d'Alphabeta1 avec nombre =", curseur_valeur)
                            # Ici, vous pouvez lancer Alphabeta1 avec curseur_valeur
                        elif selected_option == 1:
                            print("Lancement d'Alphabeta2 avec nombre =", curseur_valeur)
                            # Ici, vous pouvez lancer Alphabeta2 avec curseur_valeur
                        elif selected_option == 2:
                            print("Lancement de Minmax avec nombre =", curseur_valeur)
                            # Ici, vous pouvez lancer Minmax avec curseur_valeur
                            game_modes.game_pvai()
                        elif selected_option == 3:
                            return  # Retour au menu principal
                if curseur_rect.collidepoint(x, y):
                    curseur_dragging = True
            elif event.type == pygame.MOUSEMOTION:
                if curseur_dragging:
                    x, _ = event.pos
                    x = max(curseur_rect.left + 10, min(curseur_rect.right - 10, x))
                    position_relative = x - curseur_rect.left - 10
                    curseur_valeur = int(
                        (position_relative / (curseur_rect.width - 20)) * (curseur_max - curseur_min) + curseur_min)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                curseur_dragging = False

        if not en_jeu:
            afficher_menu()

        pygame.display.flip()


if __name__ == "__main__":
    main()
