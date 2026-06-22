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
depart = pygame.Vector2(screen.get_width() / 16, screen.get_height() / 16)
player_pos = depart.copy()
font = pygame.font.Font(None, 50)
texte = font.render("Go touch your blue friend", True, (255, 255, 255))
Morts=0
is_blue_circle = True
is_green_circle = False
ligne_visible = False
is_meteorit = False
meteorit_color = "white"
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
    personnage_principal = pygame.draw.circle(screen, "red", player_pos, 20)
    if ligne_visible:
       ligne = pygame.draw.line(
        screen,
        "black",
        (screen.get_width() // 2, screen.get_height() // 8),
        (screen.get_width() // 2, screen.get_height()),
        2
    )
    if is_blue_circle:
        blue_circle = pygame.draw.circle(screen, "blue", (x_cercle, y_cercle), rayon)
    if is_green_circle:
        green_circle = pygame.draw.circle(screen, "green", (50, 680), rayon)
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
    if is_meteorit :
        meteorit = pygame.draw.rect(screen, meteorit_color , (x, y, rect_largeur, rect_hauteur))
      #  if (dt / 1000) % 2 == 0:
      #      meteorit.color = "black"
      #  else:
      #      meteorit.color = "255,255,255"
    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    if personnage_principal.left < 0 or personnage_principal.right >= screen.get_width() or personnage_principal.top < 0  or personnage_principal.bottom > screen.get_height() :
        player_pos = depart.copy()
        ajouter_mort()
    if pygame.Rect.colliderect(personnage_principal, blue_circle):
        is_green_circle=True
        is_blue_circle=False
        ligne_visible=True
        texte = font.render("Go touch your green friend", True, (255, 255, 255))
        is_meteorit=True
    if 'ligne' in locals():
        if pygame.Rect.colliderect(personnage_principal, ligne):
            ajouter_mort()