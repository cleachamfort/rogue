import numpy as np 
import matplotlib.pyplot as plt
import pygame as pg
import personnage

# on initialise pygame et on crée une fenêtre de 400x300 pixels
pg.init()
screen = pg.display.set_mode((600, 600))
# on crée aussi un objet "horloge"
clock = pg.time.Clock()
running = True

W, H = 20, 20
X, Y = 30, 30

# DIRECTIONS = {
#     'DOWN': (0, -1),
#     'UP': (0, 1),
#     'RIGHT': (1, 0),
#     'LEFT': (-1, 0),
# }

WHITE = (240, 240, 240)
BLACK = (255, 255, 255)

def draw_background():
    screen.fill(WHITE)
    for x in range(X):
        for y in range(Y):
            if (x+y) % 2 == 0:
                draw_tile(x, y, BLACK)


def draw_tile(x, y, color):
    """
    x and y in tiles coordinates
    translate into pixel coordinates for painting
    """
    rect = pg.Rect(x*W, y*H, W, H)
    pg.draw.rect(screen, color, rect)


def draw_room(x, y, lenght, width, x_porte, y_porte):
    rect_haut = pg.Rect(x*W, y*H, W*width, H)
    pg.draw.rect(screen, (0, 0, 255), rect_haut)
    rect_gauche = pg.Rect(x*W, y*H, W, H*lenght)
    rect_droite = pg.Rect((x+width)*W, y*H, W, H*(lenght+1))
    rect_bas = pg.Rect(x*W, (y+lenght)*H, W*width, H)
    rect_porte = pg.Rect(x_porte*W, y_porte*H, W, H)
    pg.draw.rect(screen, (0, 0, 255), rect_bas)
    pg.draw.rect(screen, (0, 0, 255), rect_gauche)
    pg.draw.rect(screen, (0, 0, 255), rect_droite)
    pg.draw.rect(screen, (255, 0, 0), rect_porte)

personnage = personnage(0,0,10,10,[0,1])

# enfin on boucle à l'infini pour faire le rendu de chaque image
while True:
    # l'objet "clock" permet de limiter le nombre d'images par secondes
    # ici pour cette démo on demande 1 image par seconde
    clock.tick(1)

    # on itère sur tous les évènements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
            break
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            elif event.key == pg.K_UP :
                personnage.y = personnage.y - 1
                personnage.direction=np.array([1,0])
            elif event.key == pg.K_DOWN :
                personnage.y=personnage.y - 1
                personnage.direction=np.array([-1,0])
                personnage.direction
            elif event.key == pg.K_RIGHT :
                personnage.x =personnage.x + 1 
                personnage.direction=np.array([0,1])
            elif event.key == pg.K_LEFT :
                personnage.x =personnage.x + 1
                personnage.direction=np.array([-1,0])

    draw_background()

    draw_room(5, 7, 15, 12, 5, 15)

    # enfin on met à jour la fenêtre avec tous les changements
    pg.display.update()