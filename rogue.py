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

    # enfin on met à jour la fenêtre avec tous les changements
    pg.display.update()
