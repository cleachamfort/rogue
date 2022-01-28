import pygame as pg
import numpy as np
import objets


class Personnage:
    def __init__(self, xinit, yinit, vie, force):
        self.vie = vie
        self.force = force
        self.x = xinit
        self.y = yinit
    
    def perso_can_move(self, direction, room):
        x_pos=self.x + direction[0]
        y_pos=self.y + direction[1]
        if (is_in_room(x_pos,y_pos)) or (is_on_door(x_pos, y_pos)):
            return(True)
        return(False)
    
    

        # def ramasser(self):
        #     case_devant = np.add(personnage.position,personnage.direction)
        #     global sac
        #     liste_objets = sac.contenu
        #     for obj in liste_objets :
        #         if obj.position == case_devant:
        #             sac.add(obj)
        #             break

