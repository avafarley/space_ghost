import pygame
import time
import random
import math
from pygame import mixer


class MyGame:

    def __init__(self):
        pygame.font.init()

        self.WIDTH = 1000
        self.HEIGHT = 600

        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Space Ghost")

        # images
        self.background = pygame.transform.scale(pygame.image.load("Assets\Sprites\galax.png"), (self.WIDTH, self.HEIGHT))
        self.background_width = self.background.get_width()
        self.ghost = pygame.image.load("Assets\Sprites\BlueGhost.png")
        self.ghost2 = pygame.image.load("Assets\Sprites\PinkGhost.png")
        self.donut = pygame.image.load("Assets\Sprites\Donut.png")

        # Dimensions
        self.PLAYER_WIDTH = 38
        self.PLAYER_HEIGHT = 46

        self.DONUT_WIDTH = 52
        self.DONUT_HEIGHT = 36

        self.STAR_WIDTH = 10
        self.STAR_HEIGHT = 10

        self.PLAYER_VEL = 15
        self.STAR_VEL = 3

        self.FONT = pygame.font.SysFont("luckiestguy", 40)
        self.BIG_FONT = pygame.font.SysFont("luckiestguy", 96)

        self.FPS = 60


    def draw(self, player, player2, elapsed_time, stars):
        time_text = self.FONT.render(f"{round(elapsed_time)}", 1, "red")
        self.WINDOW.blit(time_text, (10, 10))
        self.WINDOW.blit(self.ghost, (player.x, player.y))
        self.WINDOW.blit(self.ghost2, (player2.x, player2.y))

        for star in stars:
            self.WINDOW.blit(self.donut, star)

        pygame.display.update()

    def main(self):
        run = True

        clock = pygame.time.Clock()
        start_time = time.time()

        elapsed_time = 0

        # scroll background
        scroll = 0
        tiles = math.ceil(self.WIDTH / self.background_width) + 1

        player_hit = False
        player2_hit = False

        player = pygame.Rect(200, self.HEIGHT - self.PLAYER_HEIGHT, self.PLAYER_WIDTH, self.PLAYER_HEIGHT)
        player2 = pygame.Rect(100, self.HEIGHT - self.PLAYER_HEIGHT, self.PLAYER_WIDTH, self.PLAYER_HEIGHT)

        # donuts were originally stars
        star_add_increment = 800
        star_count = 0
        stars = []

        while run:

            clock.tick(self.FPS)

            star_count += clock.tick(60)
            elapsed_time = time.time() - start_time

            if star_count > star_add_increment:
                # Sets it where donuts fall in increments of 3
                for _ in range(3):
                    star_x = random.randint(0, self.WIDTH - self.STAR_WIDTH)
                    star = pygame.Rect(star_x, - self.STAR_HEIGHT, self.STAR_WIDTH, self.STAR_HEIGHT)

                    stars.append(star)
                # Increasingly adds donuts as time goes on
                star_add_increment = max(200, star_add_increment - 60)
                star_count = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            # Player 2 controls (arrow keys)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x - self.PLAYER_VEL >= -10:
                player.x -= self.PLAYER_VEL
            if keys[pygame.K_RIGHT] and player.x + self.PLAYER_VEL + player.width <= self.WIDTH:
                player.x += self.PLAYER_VEL
            if keys[pygame.K_UP] and player.y + self.PLAYER_VEL >= 10:
                player.y -= self.PLAYER_VEL
            if keys[pygame.K_DOWN] and player.y + self.PLAYER_VEL + player.height <= self.HEIGHT:
                player.y += self.PLAYER_VEL

            # Player 1 controls (a,w,s,d)
            if keys[pygame.K_a] and player2.x - self.PLAYER_VEL >= -10:
                player2.x -= self.PLAYER_VEL
            if keys[pygame.K_d] and player2.x + self.PLAYER_VEL + player.width <= self.WIDTH:
                player2.x += self.PLAYER_VEL
            if keys[pygame.K_w] and player2.y + self.PLAYER_VEL >= 10:
                player2.y -= self.PLAYER_VEL
            if keys[pygame.K_s] and player2.y + self.PLAYER_VEL + player.height <= self.HEIGHT:
                player2.y += self.PLAYER_VEL

            # Make donuts fall onto screen
            for star in stars[:]:
                star.y += self.STAR_VEL
                if star.y > self.HEIGHT:
                    stars.remove(star)
                elif star.y + star.height >= player.y and star.colliderect(player):
                    stars.remove(star)
                    player_hit = True
                    mixer.init()
                    mixer.music.load("assets\sprites\DeathSound.ogg")
                    mixer.music.play()
                    break

            for star in stars[:]:
                star.y += self.STAR_VEL
                if star.y > self.HEIGHT:
                    stars.remove(star)
                elif star.y + star.height >= player2.y and star.colliderect(player2):
                    stars.remove(star)
                    player2_hit = True
                    mixer.init()
                    mixer.music.load("assets\sprites\DeathSound.ogg")
                    mixer.music.play()
                    break


            # making it so if player 1 hit donut it's game over
            if player_hit:
                lost_text = self.BIG_FONT.render("Player 2 Won!", 1, "red")
                self.WINDOW.blit(lost_text, (self.WIDTH / 2 - lost_text.get_width() / 2, self.HEIGHT / 2 - lost_text.get_height() / 2))
                pygame.display.update()
                pygame.time.delay(3000)
                break

            # making it so if player 2 hit donut it's game over
            if player2_hit:
                lost_text = self.BIG_FONT.render("Player 1 Won!", 1, "red")
                self.WINDOW.blit(lost_text, (self.WIDTH / 2 - lost_text.get_width() / 2, self.HEIGHT / 2 - lost_text.get_height() / 2))
                pygame.display.update()
                pygame.time.delay(3000)
                break

            # Makes moving background
            for i in range(0, tiles):
                self.WINDOW.blit(self.background, (i * self.background_width + scroll, 0))
                scroll -= 5

            if abs(scroll) > self.background_width:
                scroll = 0


            self.draw(player, player2, elapsed_time, stars)

        pygame.quit()


if __name__ == "__main__":
    game = MyGame()

    game.main()