import numpy as np
import pygame

class Tablero:

    def __init__(self):
        # LAS PIEDRAS ESTAN OMPUESTAS:
        # 0 VACIO
        # 1 FICHA BLANCA
        # 2 BICHA NEGRA

        self.tns = np.array(
                [ [1, 1, 1, 1],[0, 0, 0, 0],[0, 0, 0, 0],[2, 2, 2, 2] ])

        self.tbs = np.array(
                [ [1, 1, 1, 1],[0, 0, 0, 0],[0, 0, 0, 0],[2, 2, 2, 2] ])

        self.tni = np.array(
                [ [1, 1, 1, 1],[0, 0, 0, 0],[0, 0, 0, 0],[2, 2, 2, 2] ])

        self.tbi = np.array(
                [ [1, 1, 1, 1],[0, 0, 0, 0],[0, 0, 0, 0],[2, 2, 2, 2] ])

        
        self.cafe_claro = (237, 224, 212)
        self.cafe_oscuro = (127, 85, 57)
        self.cafe_sombra = (89, 69, 54)
        self.escala = 60
        self.x_offset = 40
        self.y_offset = 40
        self.h_gap = self.escala/2
        self.v_gap = self.escala



    def print_tablero(self):
        # recorrido vertical
        
        
        for i in range(8):
            if i == 4:
                print("--------------------")
            if i < 4:
                print(str(self.tns[i]) + " " + str(self.tbs[i]))
            else: 
                print(str(self.tni[i-4]) + " " + str(self.tbi[i-4]))


    def dibujar_rect(self, screen, i, j, color, h_g = 0, v_g = 0):
        pygame.draw.rect(
                screen,
                color,
                pygame.Rect(
                    self.x_offset + h_g + self.escala*j,
                    self.y_offset + v_g + self.escala*i,
                    self.escala, 
                    self.escala))
        pygame.draw.rect(
                screen,
                self.cafe_sombra,
                pygame.Rect(
                    self.x_offset + h_g + self.escala*j,
                    self.y_offset + v_g + self.escala*i,
                    self.escala, 
                    self.escala),width=2)


    def dibujar_all(self, screen):
        
        
        for i in range(8):
            for j in range(8):
                if i < 4:
                    # superiores
                    if j < 4:
                        # tablero oscur
                        self.dibujar_rect(screen, i, j, self.cafe_oscuro);

                    else:
                        # tablero claro
                        self.dibujar_rect(screen, i, j, self.cafe_claro, self.h_gap);
                else:
                    # inferiores
                    if j < 4:
                        # tablero oscur
                        self.dibujar_rect(screen, i, j, self.cafe_oscuro, 0, self.v_gap);
                    else:
                        # tablero claro
                        self.dibujar_rect(screen, i, j, self.cafe_claro, self.h_gap, self.v_gap);



        

