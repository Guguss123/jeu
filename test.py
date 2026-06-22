# Example file showing a circle moving on screen
import pygame
import math
import random
import time
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
rayon = 20
x_cercle = screen.get_width() - rayon  -20
y_cercle = screen.get_height() - rayon -20
rect_largeur = 100
rect_hauteur = 50
x = random.randint(0, screen.get_width() - rect_largeur)
y = random.randint(0, screen.get_height() - rect_hauteur)
départ = pygame.Vector2(screen.get_width() / 16, screen.get_height() / 16)
player_pos = départ.copy()
font = pygame.font.Font(None, 50)
texte = font.render("Go touch your blue friend", True, (255, 255, 255))
Morts=0
blue_circle=True
green_circle=False
ligne_visible=False
meteorit =False
white = (255,255,255)
black = (0,0,0)
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
    PP=pygame.draw.circle(screen, "red", player_pos, 20)
    if ligne_visible:
       pygame.draw.line(
        screen,
        (0, 0, 0),
        (screen.get_width() // 2, screen.get_height() // 8),
        (screen.get_width() // 2, screen.get_height()),
        2
    )
    if blue_circle:
        pygame.draw.circle(screen, "blue", (x_cercle, y_cercle), rayon)
    if green_circle:
        pygame.draw.circle(screen, "green", (50, 680), rayon)
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
    if meteorit :
        pygame.draw.rect(screen,white , (x, y, rect_largeur, rect_hauteur))
        time.sleep(1)
        meteorit = black
    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    if player_pos.x < rayon or player_pos.x > screen.get_width() - rayon or player_pos.y < rayon or player_pos.y > screen.get_height() - rayon :
        player_pos = départ.copy()
        ajouter_mort()
    if abs((player_pos.x - x_cercle)**2 + (player_pos.y - y_cercle)**2  <= rayon**2):
        green_circle=True
        blue_circle=False
        ligne_visible=True
        texte = font.render("Go touch your green friend", True, (255, 255, 255))
        meteorit=True
        if pygame.rect.colliderect(PP.rect,ligne_visible.rect):
            ajouter_mort