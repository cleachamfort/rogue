import pygame as pg
import numpy as np
import objets



class Mechant : 
    def __init__(self, xinit, yinit, vie, force)
        self.vie = vie
        self.force = force
        self.x = xinit
        self.y = yinit
    def deplacement (mechant):
        while (running== True ):
            direction = rd.randint(0,3)
            if direction == 0 : 
                #on considère que ça veut dire up 
                mechant.y = mechant.y - 1
            elif direction == 1 :
                mechant.y=mechant.y - 1
            elif direction == 2 :
                mechant.x = mechant.x + 1 
            else :
                mechant.x =mechant.x + 1

class Personnage:
    def __init__(self, xinit, yinit, vie, force):
        self.vie = vie
        self.force = force
        self.x = xinit
        self.y = yinit

    def ramasser(self):
        global sac
        liste_objets = sac.contenu
        for obj in liste_objets :
            if obj.position == self.x,self.y:
                    sac.add(obj)
                    break

def deplacement (perso):
    while (running== True ):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
            elif event.type == pg.KEYDOWN:
                # si la touche est "Q" on veut quitter le programme
                if event.key == pg.K_q:
                    running = False
                elif event.key == pg.K_UP :
                    perso.y = perso.y - 1
                    perso.direction=np.array([1,0])
                elif event.key == pg.K_DOWN :
                    perso.y=perso.y - 1
                    perso.direction=np.array([-1,0])
                    perso.direction
                elif event.key == pg.K_RIGHT :
                    perso.x =perso.x + 1 
                    perso.direction=np.array([0,1])
                elif event.key == pg.K_LEFT :
                    perso.x =perso.x + 1
                    perso.direction=np.array([-1,0])