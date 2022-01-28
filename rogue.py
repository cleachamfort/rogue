##blabla
import numpy as np 
import matplotlib.pyplot as plt
import pygame as pg

# on initialise pygame et on crée une fenêtre de 400x300 pixels
pg.init()
screen = pg.display.set_mode((400, 300))
# on crée aussi un objet "horloge"
clock = pg.time.Clock()
running = True

# enfin on boucle à l'infini pour faire le rendu de chaque image
while running:
    # l'objet "clock" permet de limiter le nombre d'images par secondes
    # ici pour cette démo on demande 1 image par seconde
    clock.tick(1)

<<<<<<< HEAD
    # on itère sur tous les évènements qui ont eu lieu depuis le précédent appel
=======
    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
>>>>>>> 4b3c54b73e796a53a7c4e1f357e0f3f0d9db03b4
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

    # enfin on met à jour la fenêtre avec tous les changements
    pg.display.update()
<<<<<<< HEAD
pg.quit()
=======
>>>>>>> 4b3c54b73e796a53a7c4e1f357e0f3f0d9db03b4
