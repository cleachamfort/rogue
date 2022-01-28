import pygame as pg
import numpy as np
import objets


class Personnage:
    def __init__(self, xinit, yinit, vie, force, direction):
        self.vie = vie
        self.force = force
        self.x = xinit
        self.y = yinit
        self.direction=direction

        # def ramasser(self):
        #     case_devant = np.add(personnage.position,personnage.direction)
        #     global sac
        #     liste_objets = self.contenu
        #     for obj in liste_objets :
        #         if obj.position == case_devant:
        #             self.add(obj)
        #             break

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
    
