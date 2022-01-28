import pygame as pg


class Mur :
    def __init__(self, x, y, lenght, width, x_porte, y_porte):
        self.x = x
        self.y = y
        self.lenght = lenght
        self.width = width
        self.x_porte = x_porte
        self.y_porte = y_porte


    def is_a_wall(self, x_pos, y_pos):
        walls = [[x_pos, y_pos]]
        for i in range(1, self.lenght):
            walls.append([self.x, self.y+i])
            walls.append([self.x+self.width, self.y+i])
        for i in range(1, self.width):
            walls.append([self.x+i, self.y])
            walls.append([self.x+i, self.y+self.lenght])
        if [x_pos, y_pos] in walls :
            if [x_pos, y_pos] != [self.x_porte, self.y_porte] :
                return True
        return False
