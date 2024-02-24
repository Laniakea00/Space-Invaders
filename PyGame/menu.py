import pygame,sys

class Menu:
    def __init__(self,screen_width,screen_height):
        self.font = pygame.font.Font('Fonts/Pixeled.ttf', 36)
        self.menu_active = True
        self.options = ["Start Game", "Quit Game"]
        self.selected_option = 0
        self.background = pygame.image.load('Images/menu_background.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.selected_option = (self.selected_option - 1) % len(self.options)
        elif keys[pygame.K_DOWN]:
            self.selected_option = (self.selected_option + 1) % len(self.options)

        if keys[pygame.K_RETURN]:
            if self.selected_option == 0:
                self.menu_active = False  # Start Game
            elif self.selected_option == 1:
                pygame.quit()
                sys.exit()  # Quit Game

    def draw(self, screen, screen_width, screen_height):
        screen.blit(self.background, (0, 0))

        for i, option in enumerate(self.options):
            text_color = 'green' if i == self.selected_option else 'white'
            option_surf = self.font.render(option, False, text_color)
            option_rect = option_surf.get_rect(center=(screen_width / 2, screen_height / 2 + i * 50))
            screen.blit(option_surf, option_rect)

        pygame.display.flip()


    def run(self, screen, screen_width, screen_height):
        while self.menu_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.handle_input()
            self.draw(screen, screen_width, screen_height)
