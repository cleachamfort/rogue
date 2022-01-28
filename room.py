import pygame as pg


screen = pg.display.set_mode((600, 600))
W, H = 20, 20
X, Y = 30, 30

class Room :
    def __init__(self, x, y, lenght, width, x_porte, y_porte):
        self.x = x
        self.y = y
        self.lenght = lenght
        self.width = width
        self.x_porte = x_porte
        self.y_porte = y_porte


    # def is_a_wall(self, x_pos, y_pos):
    #     walls = [[x_pos, y_pos]]
    #     for i in range(1, self.lenght):
    #         walls.append([self.x, self.y+i])
    #         walls.append([self.x+self.width, self.y+i])
    #     for i in range(1, self.width):
    #         walls.append([self.x+i, self.y])
    #         walls.append([self.x+i, self.y+self.lenght])
    #     if [x_pos, y_pos] in walls :
    #         if [x_pos, y_pos] != [self.x_porte, self.y_porte] :
    #             return True
    #     return False


    def is_in_room(self, x_pos, y_pos) :
        if x_pos > self.x  and x_pos < self.x + self.width -1 and y_pos > self.y  and y_pos < self.y + self.lenght -1 :
            return True
        return False

    def is_on_door(self, x_pos, y_pos) :
        if x_pos == self.x_porte and y_pos == self.y_porte :
            return True
        return False


    def draw_room(self):
        rect_haut = pg.Rect(self.x*W, self.y*H, W*self.width, H)
        pg.draw.rect(screen, (0, 0, 255), rect_haut)
        rect_gauche = pg.Rect(self.x*W, self.y*H, W, H*self.lenght)
        pg.draw.rect(screen, (0, 0, 255), rect_gauche)
        rect_droite = pg.Rect((self.x+self.width)*W, self.y*H, W, H*(self.lenght+1))
        rect_bas = pg.Rect(self.x*W, (self.y+self.lenght)*H, W*self.width, H)
        rect_porte = pg.Rect(self.x_porte*W, self.y_porte*H, W, H)
        pg.draw.rect(screen, (0, 0, 255), rect_bas)
        pg.draw.rect(screen, (0, 0, 255), rect_droite)
        pg.draw.rect(screen, (139, 69, 19), rect_porte)
