import pygame as pg


class Room :
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


    def is_in_room(self, x_pos, y_pos) :
        if x_pos > self.x  and x_pos < self.x + self.width and y_pos > self.y and y_pos < self.y + self.lenght :
            return True
        return False

    def is_on_door(self, x_pos, y_pos) :
        if x_pos == self.x_porte and y_pos == self.y_porte :
            return True
        return False


    def draw_room(x, y, lenght, width, x_porte, y_porte):
    rect_haut = pg.Rect(x*W, y*H, W*width, H)
    pg.draw.rect(screen, (0, 0, 255), rect_haut)
    rect_gauche = pg.Rect(x*W, y*H, W, H*lenght)
     pg.draw.rect(screen, (0, 0, 255), rect_gauche)
    rect_droite = pg.Rect((x+width)*W, y*H, W, H*(lenght+1))
    rect_bas = pg.Rect(x*W, (y+lenght)*H, W*width, H)
    rect_porte = pg.Rect(x_porte*W, y_porte*H, W, H)
    pg.draw.rect(screen, (0, 0, 255), rect_bas)
    pg.draw.rect(screen, (0, 0, 255), rect_droite)
    pg.draw.rect(screen, (139, 69, 19), rect_porte)
