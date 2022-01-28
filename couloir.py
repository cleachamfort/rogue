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

            



        



