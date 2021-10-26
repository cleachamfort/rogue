import pygame as pg
from random import randint

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()


snake = [
    [10, 15],
    [11, 15],
    [12, 15]]
direction = [1, 0]
newdirection = [1, 0]
# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:
    clock.tick(1)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            elif event.key == pg.K_UP :
                newdirection = [0, -1]
            elif event.key == pg.K_DOWN :
                newdirection = [0, 1]
            elif event.key == pg.K_RIGHT :
                newdirection = [1, 0]
            elif event.key == pg.K_LEFT :
                newdirection = [-1, 0]
    
    if newdirection != - direction :
        direction = newdirection

        
         

    n, m = 400, 300
# les coordonnées de rectangle que l'on dessine
    #x = 0 # coordonnée x (colonnes) en pixels
    #y = 0 # coordonnée y (lignes) en pixels
    #width = 400 # largeur du rectangle en pixels
    #height = 300 # hauteur du rectangle en pixels
    #rect = pg.Rect(x, y, width, height)
# appel à la méthode draw.rect()
    color = (255, 255, 255)
    #pg.draw.rect(screen, color, rect)
    #for i in range(0, 400, 40):
      #  for j in range(0, 300, 40):
       #     rect = pg.Rect(i, j, 20, 20)
        #    pg.draw.rect(screen, color, rect)
    
   # for i in range(20, 400, 40):
    #    for j in range(20, 300, 40):
     #       rect = pg.Rect(i, j, 20, 20)
      #      pg.draw.rect(screen, color, rect)

    
    snake.append([snake[-1][0] + direction[0], snake[-1][1] + direction[1]])
    snake.pop(0)
    print(snake)
    screen.fill((0, 0, 0))
    for k in range(len(snake)):
        u, v = snake[k][0]*20, snake[k][1]*20
        rect = pg.Rect(u, v, 20, 20)
        color = (255, 255, 255)
        pg.draw.rect(screen, color, rect)


    pg.display.update()
