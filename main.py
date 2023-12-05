import pygame
import sys
from button import Button
from game import MyGame
from pygame import mixer

pygame.init()

WIDTH, HEIGHT = 1280, 720
# Menu Screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/sprites/Background1.png")

# Add Background Music
mixer.init()
mixer.music.load("assets\sprites\BGsong.ogg")
mixer.music.play()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/sprites/font.ttf", size)


def play():
    game = MyGame()
    game.main()

# How to Play button - used to be an options button so everything is still coded under "option" name
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        rules = pygame.transform.scale(pygame.image.load("Assets\Sprites\options.png"), (WIDTH, HEIGHT))
        SCREEN.blit(rules, (0,0))

        # OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(1120, 680),
                              text_input="BACK", font=get_font(50), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# Main Menu Button
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Space Ghost", True, "#b10f60")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/sprites/Play Rect.png"), pos=(300, 250),
                             text_input="PLAY", font=get_font(75), base_color="#fc0882", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/sprites/Options Rect.png"), pos=(410, 400),
                                text_input="HOW TO PLAY", font=get_font(50), base_color="#7ffa75", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/sprites/Quit Rect.png"), pos=(300, 550),
                             text_input="QUIT", font=get_font(75), base_color="#7ffa75", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

# Makes button change color when mouse hover over
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
