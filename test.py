# Example file showing a circle moving on screen
import pygame
import math
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
rayon = 20
x_cercle = screen.get_width() - rayon  -20
y_cercle = screen.get_height() - rayon -20
départ = pygame.Vector2(screen.get_width() / 16, screen.get_height() / 16)
player_pos = départ.copy()
font = pygame.font.Font(None, 50)
texte = font.render("Go touch your blue friend", True, (255, 255, 255))
Morts=0
green_circle=False
def ajouter_mort():
    global Morts
    Morts += 1
def afficher_score():
    texte = font.render(f"Morts : {Morts}", True, (255, 255, 255))
    screen.blit(texte, (500, 20))
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(texte, (20, 20))
    pygame.draw.circle(screen, "red", player_pos, 20)
    blue_circle=pygame.draw.circle(screen, "blue", (x_cercle, y_cercle), rayon)
    if green_circle:
        pygame.draw.circle(screen, "green", (50, 50), rayon)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 250 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 250 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 250 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 250 * dt
    afficher_score()
    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    if player_pos.x < rayon or player_pos.x > screen.get_width() - rayon or player_pos.y < rayon or player_pos.y > screen.get_height() - rayon :
        player_pos = départ.copy()
        ajouter_mort()
    if abs((player_pos.x - x_cercle)**2 + (player_pos.y - y_cercle)**2  <= rayon**2):
        player_pos=départ
        green_circle=True
        