import numpy as np 
import matplotlib.pyplot as plt
import pygame as pg
import personnage as perso
from room import * 
from couloir import * 

# on initialise pygame et on crée une fenêtre de 400x300 pixels
pg.init()
screen = pg.display.set_mode((600, 600))
# on crée aussi un objet "horloge"
clock = pg.time.Clock()
running = True

room1 = Room(5, 7, 10, 10,15, 11)
room2 = Room(20, 7, 7, 8, 20, 11)
actual_room = room1
perso = perso.Personnage(7,12,10,10, actual_room)

W, H = 20, 20
X, Y = 30, 30

WHITE = (240, 240, 240)
BLACK = (255, 255, 255)

def draw_background():
    screen.fill(WHITE)
    for x in range(X):
        for y in range(Y):
            if (x+y) % 2 == 0:
                draw_tile(x, y, BLACK)

def draw_couloir(couloir):
        for i in range(len(couloir)):
            couloir_rect = pg.Rect(couloir[i][0]*W, couloir[i][1]*H, W, H)
            pg.draw.rect(screen, (255,127, 0), couloir_rect)


def draw_tile(x, y, color):
    """
    x and y in tiles coordinates
    translate into pixel coordinates for painting
    """
    rect = pg.Rect(x*W, y*H, W, H)
    pg.draw.rect(screen, color, rect)

# enfin on boucle à l'infini pour faire le rendu de chaque image
while running:
    direction=[0,0]
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
                direction=np.array([1,0])
                if perso.perso_can_move(direction) :
                    perso.y = perso.y - 1
            elif event.key == pg.K_DOWN :
                direction=np.array([-1,0])
                if perso.perso_can_move(direction):
                    perso.y=perso.y + 1
            elif event.key == pg.K_RIGHT :
                direction=np.array([0,1])
                if perso.perso_can_move(direction):
                    perso.x =perso.x + 1 
            elif event.key == pg.K_LEFT :
                direction=np.array([-1,0])
                if perso. perso_can_move(direction):
                    perso.x =perso.x -1

    draw_background()
    room1.draw_room()
    room2.draw_room()
    draw_couloir([[16,11], [17, 11], [18,11], [19,11]])
    
    draw_tile(perso.x, perso.y, (255, 0, 0))
    
    

    

    #draw_room(5, 7, 15, 12, 5, 15)

    draw_room(5, 7, 15, 12)
    # enfin on met à jour la fenêtre avec tous les changements
    pg.display.update()

