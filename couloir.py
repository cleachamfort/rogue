import pygame as pg
import personnage


class Couloir:
    def __init__(self, cases):
        self.cases = cases
    def passage (self, x,y): #x,y est la position du personnage
        clock = pg.time.Clock()
        if [x,y] == self.cases[0]:
            # Le personnage va passer automatiquement dans le couloir
            for i in range(len(self)):
                clock.tick(1)
                personnage.x = self.cases[i][0]
                personnage.y = self.cases[i][1]
                pg.display.update()
        elif [x,y] == self.cases[-1]:
            # Le personnage va passer automatiquement dans le couloir
            for i in range(len(self), -1):
                clock.tick(1)
                personnage.x = self.cases[i][0]
                personnage.y = self.cases[i][1]
                pg.display.update()



        



