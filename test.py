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
x_cercle = screen.get_width() - rayon - 10  
y_cercle = screen.get_height() - rayon - 10
player_pos = pygame.Vector2(screen.get_width() / 16, screen.get_height() / 16)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 20)
    pygame.draw.circle(screen, "blue", (x_cercle, y_cercle), rayon)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 250 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 250 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 250 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 250 * dt
    # flip() the display to put your work on screen
    pygame.display.flip()
    image = pygame.image.load("level 1.jpg")
    screen.blit(image , (100, 100))
    dt = clock.tick(60) / 1000
    if abs((player_pos.x - x_cercle)**2 + (player_pos.y - y_cercle)**2  <= rayon**2):
        pygame.quit

