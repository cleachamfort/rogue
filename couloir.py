import pygame as pg
#from pyrsistent import T
import personnage


class Couloir:
    def __init__(self, cases):
        self.cases = cases
    
    def is_in_couloir (cases, x,y):
        if [x,y] == cases[0]:
            return (True, "begin")
        elif [x,y] == cases[-1]:
            return (True, "end")
        else: 
            return (False, "Nope")

            


    def draw_couloir(couloir):
        for i in range(len(couloir)):
            couloir_rect = pg.Rect(couloir[i][0]*W, couloir[i][1]*H, W, H)
            pg.draw.rect(screen, (255,127, 0), couloir_rect)




        



