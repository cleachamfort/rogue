import pygame as pg
import numpy as np
import objets


class personnage:
    def __init__(self, xinit, yinit, vie, force, direction):
        self.xinit = xinit
        self.yinit = yinit
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

def deplacement ():
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
    
