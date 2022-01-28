##blabla
import numpy as np 
import matplotlib.pyplot as plt
import pygame as pg
import personnage

# on initialise pygame et on crée une fenêtre de 400x300 pixels
pg.init()
screen = pg.display.set_mode((400, 300))
# on crée aussi un objet "horloge"
clock = pg.time.Clock()
running = True

personnage = personnage(0,0,10,10,[0,1])

# enfin on boucle à l'infini pour faire le rendu de chaque image
while running:
    # l'objet "clock" permet de limiter le nombre d'images par secondes
    # ici pour cette démo on demande 1 image par seconde
    clock.tick(1)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
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

    # enfin on met à jour la fenêtre avec tous les changements
    pg.display.update()
pg.quit()
