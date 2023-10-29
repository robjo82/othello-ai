import sys

import pygame

from src import settings, board


class Menu:
    def __init__(self):
        self.selected_option = None
        self.buttons = []

    def update_buttons(self):
        self.buttons = []
        for i, _ in enumerate(settings.OPTIONS):
            button = pygame.Rect(
                settings.WINDOW_WIDTH // 4,
                90 + i * 80,
                settings.WINDOW_WIDTH // 2,
                60
            )
            self.buttons.append(button)

    def display_menu(self, title=settings.CAPTION, option_list=settings.OPTIONS):
        window = board.display_background_and_title(title)
        for i, option in enumerate(option_list):
            button = self.buttons[i]
            if self.selected_option == i:
                pygame.draw.rect(window, settings.LIGHT_BLUE, button)
            else:
                pygame.draw.rect(window, settings.WHITE, button)

            text = settings.FONT.render(
                option,
                True,
                settings.BLACK)
            window.blit(text, text.get_rect(center=button.center))
        return window

    def run(self):
        pygame.display.set_caption(settings.CAPTION)
        clock = pygame.time.Clock()

        while True:
            self.update_buttons()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    for i, button in enumerate(self.buttons):
                        if button.collidepoint(x, y):
                            self.selected_option = i
                            if self.selected_option == 3:
                                pygame.quit()
                                sys.exit()
                            else:
                                print(f"Lancement du jeu {settings.OPTIONS[self.selected_option]}")
                                return settings.OPTIONS[self.selected_option]

            self.display_menu()

            pygame.display.flip()
            clock.tick(10)


class AIConfig:
    def __init__(self):
        self.selected_option = None
        self.selected_ai = None
        self.cursor_dragging = None
        self.cursors = [
            {'name': 'Profondeur', 'value': settings.MINIMAX_DEPTH, 'min_value': settings.MINIMAX_DEPTH,
             'max_value': settings.MAXIMAL_DEPTH},
            {'name': 'Timeout', 'value': settings.MAX_TIMEOUT, 'min_value': settings.MIN_TIMEOUT,
             'max_value': settings.MAX_TIMEOUT},
        ]
        self.final_selection = None

    def display_ai_parameters(self, title):
        window = board.display_background_and_title(title)
        self.update_buttons(window)
        return window

    def update_buttons(self, window):
        offset = 0
        for i, option in enumerate(settings.AVAILABLE_AIS.keys()):
            if self.selected_ai is not None and i > self.selected_ai:
                offset = 40 * len(settings.AVAILABLE_AIS[list(settings.AVAILABLE_AIS.keys())[self.selected_ai]])

            button = pygame.Rect(
                settings.WINDOW_WIDTH // 4,
                90 + i * 80 + offset,
                settings.WINDOW_WIDTH // 2,
                60
            )

            if self.selected_option == i:
                pygame.draw.rect(window, settings.LIGHT_BLUE, button)
            else:
                pygame.draw.rect(window, settings.WHITE, button)

            text = settings.FONT.render(
                option,
                True,
                settings.BLACK
            )
            window.blit(text, text.get_rect(center=button.center))

        if self.selected_ai is not None:
            ai_name = list(settings.AVAILABLE_AIS.keys())[self.selected_ai]
            eval_methods = settings.AVAILABLE_AIS[ai_name]

            for i, eval_method in enumerate(eval_methods):
                sub_button = pygame.Rect(
                    settings.WINDOW_WIDTH // 3,
                    120 + self.selected_ai * 80 + (i + 1) * 40,
                    settings.WINDOW_WIDTH // 3,
                    30
                )
                if sub_button.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(window, settings.LIGHT_BLUE, sub_button)
                else:
                    pygame.draw.rect(window, settings.WHITE, sub_button)

                sub_text = settings.FONT.render(
                    eval_method,
                    True,
                    settings.BLACK
                )
                window.blit(sub_text, sub_text.get_rect(center=sub_button.center))

        if self.selected_ai is not None:
            offset = 40 * len(settings.AVAILABLE_AIS[list(settings.AVAILABLE_AIS.keys())[self.selected_ai]])

        for idx, cursor in enumerate(self.cursors):
            cursor_rect = pygame.Rect(
                settings.WINDOW_WIDTH // 4,
                90 + len(settings.AVAILABLE_AIS.keys()) * 80 + offset + 80 * idx,  # Change 40 * idx to 80 * idx
                settings.WINDOW_WIDTH // 2,
                60
            )
            pygame.draw.rect(window, settings.WHITE, cursor_rect)

            pygame.draw.rect(
                window,
                settings.BLACK,
                (
                    (cursor['value'] - cursor['min_value']) / (cursor['max_value'] - cursor['min_value']) * (
                            cursor_rect.width - 30) + cursor_rect.x + 10,
                    cursor_rect.y + 10,
                    10,
                    40
                )
            )

            sub_text = settings.FONT.render(
                f"{cursor['name']}: {cursor['value']}",
                True,
                settings.BLACK
            )
            window.blit(sub_text, sub_text.get_rect(center=cursor_rect.center))

    def run(self, title):
        self.__init__()
        pygame.display.set_caption(settings.CAPTION)
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    self.handle_click(x, y)

                elif event.type == pygame.MOUSEMOTION and self.cursor_dragging is not None:
                    x, _ = event.pos
                    self.handle_cursor_drag(x)

                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.cursor_dragging = None

            if self.final_selection is not None:
                return self.final_selection

            self.display_ai_parameters(title)

            pygame.display.flip()
            clock.tick(10)

    def handle_click(self, x, y):
        offset = 0
        for i, option in enumerate(settings.AVAILABLE_AIS.keys()):
            if self.selected_ai is not None and i > self.selected_ai:
                offset = 40 * len(settings.AVAILABLE_AIS[list(settings.AVAILABLE_AIS.keys())[self.selected_ai]])

            button = pygame.Rect(
                settings.WINDOW_WIDTH // 4,
                90 + i * 80 + offset,
                settings.WINDOW_WIDTH // 2,
                60
            )

            if button.collidepoint(x, y):
                self.selected_option = i
                if self.selected_ai == self.selected_option:
                    self.selected_ai = None
                else:
                    self.selected_ai = self.selected_option

        if self.selected_ai is not None:
            ai_name = list(settings.AVAILABLE_AIS.keys())[self.selected_ai]
            eval_methods = settings.AVAILABLE_AIS[ai_name]

            for i, eval_method in enumerate(eval_methods):
                sub_button = pygame.Rect(
                    settings.WINDOW_WIDTH // 3,
                    120 + self.selected_ai * 80 + (i + 1) * 40,
                    settings.WINDOW_WIDTH // 3,
                    30
                )
                if sub_button.collidepoint(x, y):
                    cursor_values = ', '.join([f"{cursor['name']}: {cursor['value']}" for cursor in self.cursors])
                    print(
                        f"Lancement de l'IA {ai_name} avec la méthode d'évaluation {eval_method} et les paramètres {cursor_values}")
                    self.final_selection = (ai_name, eval_method, self.cursors[0]['value'], self.cursors[1]['value'])

        if self.selected_ai is not None:
            offset = 40 * len(settings.AVAILABLE_AIS[list(settings.AVAILABLE_AIS.keys())[self.selected_ai]])

        for idx, cursor in enumerate(self.cursors):
            cursor_rect = pygame.Rect(
                settings.WINDOW_WIDTH // 4,
                90 + len(settings.AVAILABLE_AIS.keys()) * 80 + offset + 80 * idx,  # Change 40 * idx to 80 * idx
                settings.WINDOW_WIDTH // 2,
                60
            )
            if cursor_rect.collidepoint(x, y):
                print(f"Cursor {cursor['name']} clicked")
                self.cursor_dragging = idx  # Save the index of the cursor being dragged

    def handle_cursor_drag(self, x):
        if self.cursor_dragging is not None:
            cursor = self.cursors[self.cursor_dragging]

            # Calcul de l'offset avant de définir cursor_rect
            offset = 0
            if self.selected_ai is not None:
                offset = 40 * len(settings.AVAILABLE_AIS[list(settings.AVAILABLE_AIS.keys())[self.selected_ai]])

            cursor_rect = pygame.Rect(
                settings.WINDOW_WIDTH // 4,
                90 + len(settings.AVAILABLE_AIS.keys()) * 80 + offset + 80 * self.cursor_dragging,
                settings.WINDOW_WIDTH // 2,
                60
            )
            cursor['value'] = round(int(((max(cursor_rect.left + 10,
                                              min(cursor_rect.right - 10, x)) - cursor_rect.left - 10) / (
                                                 cursor_rect.width - 20)) * (
                                                cursor['max_value'] - cursor['min_value']) + cursor['min_value']))


class AIVisibility:
    def __init__(self):
        self.final_selection = None
        self.selected_option = None
        self.buttons = []
        self.options = ["Voir les coups de l'IA", "Ne pas voir les coups de l'IA"]
        self.cursor_dragging = None
        self.cursor = {'name': 'Durée (ms)', 'value': 200, 'min_value': 100, 'max_value': 3000}

    def update_buttons(self):
        self.buttons = []
        for i, _ in enumerate(self.options):
            button = pygame.Rect(
                settings.WINDOW_WIDTH // 4,
                90 + i * 80,
                settings.WINDOW_WIDTH // 2,
                60
            )
            self.buttons.append(button)

    def display_menu(self):
        window = board.display_background_and_title("Visibilité de l'IA")
        for i, option in enumerate(self.options):
            button = self.buttons[i]
            if self.selected_option == i:
                pygame.draw.rect(window, settings.LIGHT_BLUE, button)
            else:
                pygame.draw.rect(window, settings.WHITE, button)

            text = settings.FONT.render(
                option,
                True,
                settings.BLACK)
            window.blit(text, text.get_rect(center=button.center))

        # Add cursor for duration
        cursor_rect = pygame.Rect(
            settings.WINDOW_WIDTH // 4,
            250,
            settings.WINDOW_WIDTH // 2,
            60
        )
        pygame.draw.rect(window, settings.WHITE, cursor_rect)

        pygame.draw.rect(
            window,
            settings.BLACK,
            (
                (self.cursor['value'] - self.cursor['min_value']) / (
                        self.cursor['max_value'] - self.cursor['min_value']) * (
                        cursor_rect.width - 30) + cursor_rect.x + 10,
                cursor_rect.y + 10,
                10,
                40
            )
        )

        sub_text = settings.FONT.render(
            f"{self.cursor['name']}: {self.cursor['value']}",
            True,
            settings.BLACK
        )
        window.blit(sub_text, sub_text.get_rect(center=cursor_rect.center))

        return window

    def run(self):
        pygame.display.set_caption("Visibilité de l'IA")
        clock = pygame.time.Clock()
        self.final_selection = None

        while True:
            self.update_buttons()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    for i, button in enumerate(self.buttons):
                        if button.collidepoint(x, y):
                            self.selected_option = i
                            self.final_selection = (self.selected_option == 0, self.cursor['value'] / 1000)

                    # Check if the cursor rectangle is clicked
                    cursor_rect = pygame.Rect(
                        settings.WINDOW_WIDTH // 4,
                        250,
                        settings.WINDOW_WIDTH // 2,
                        60
                    )
                    if cursor_rect.collidepoint(x, y):
                        self.cursor_dragging = True  # Initialize cursor_dragging

                elif event.type == pygame.MOUSEMOTION and self.cursor_dragging:
                    x, _ = event.pos
                    self.handle_cursor_drag(x)

                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.cursor_dragging = None

            self.display_menu()

            pygame.display.flip()
            clock.tick(10)

            if self.final_selection is not None:
                return self.final_selection

    def handle_cursor_drag(self, x):
        if self.cursor_dragging is not None:
            cursor_rect = pygame.Rect(
                settings.WINDOW_WIDTH // 4,
                250,
                settings.WINDOW_WIDTH // 2,
                60
            )
            self.cursor['value'] = round(int(((max(cursor_rect.left + 10,
                                                   min(cursor_rect.right - 10, x)) - cursor_rect.left - 10) / (
                                                      cursor_rect.width - 20)) * (
                                                     self.cursor['max_value'] - self.cursor['min_value']) + self.cursor[
                                                 'min_value']))
