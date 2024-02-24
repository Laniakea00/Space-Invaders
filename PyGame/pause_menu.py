import pygame,sys

class PauseMenu:
    def __init__(self, screen_width, screen_height, game):
        self.font = pygame.font.Font('Fonts/Pixeled.ttf', 36)
        self.menu_active = False
        self.options = ["Continue Game", "Quit Game"]
        self.selected_option = 0
        self.background = pygame.Surface((screen_width, screen_height))
        self.background.fill((128, 128, 128))
        self.game = game


    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.selected_option = (self.selected_option - 1) % len(self.options)
        elif keys[pygame.K_DOWN]:
            self.selected_option = (self.selected_option + 1) % len(self.options)

        if keys[pygame.K_RETURN]:
            if self.selected_option == 0:
                self.menu_active = False  # Continue Game
            elif self.selected_option == 1:
                pygame.quit()
                sys.exit()  # Quit Game

    def draw(self, screen, screen_width, screen_height):
        screen.blit(self.background, (0, 0))

        screen.fill((30, 30, 30))

        title_surf = self.font.render("Pause Menu", False, 'white')
        title_rect = title_surf.get_rect(center=(screen_width / 2, screen_height / 4))
        screen.blit(title_surf, title_rect)

        for i, option in enumerate(self.options):
            text_color = 'green' if i == self.selected_option else 'white'
            option_surf = self.font.render(option, False, text_color)
            option_rect = option_surf.get_rect(center=(screen_width / 2, screen_height / 2 + i * 50))
            screen.blit(option_surf, option_rect)

        pygame.display.flip()
