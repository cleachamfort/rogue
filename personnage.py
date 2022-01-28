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
        #     liste_objets = sac.contenu
        #     for obj in liste_objets :
        #         if obj.position == case_devant:
        #             sac.add(obj)
        #             break

