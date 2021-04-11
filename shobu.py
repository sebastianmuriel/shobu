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

        
        #self.cafe_claro = (237, 224, 212)
        #self.cafe_claro = (193, 159, 111)
        self.cafe_claro = (188, 150, 98)
        self.cafe_oscuro = (127, 85, 57)
        #self.cafe_sombra = (72, 64, 55)
        self.cafe_sombra = (74, 54, 35)
        #self.cafe_luz = (196, 162, 130)
        self.cafe_luz = (209, 183, 158)

        self.color_selection = (176, 254, 118)
        self.color_selection = (134, 97, 193) 

        self.color_fichaNegra = (28, 28, 27)
        self.color_sombra_fichaNegra = (19, 18, 15)
        self.color_fichaBlanca = (199, 203, 199)
        self.color_sombra_fichaBlanca = (180, 182, 174)

        self.escala_ficha = 40
        self.x_offset_ficha = 10
        self.y_offset_ficha = 10

        self.escala = 60
        self.x_offset = 40
        self.y_offset = 60
        self.h_gap = self.escala/2
        self.v_gap = self.escala

        self.pos_selection = None

        self.tipo_movimiento = 1 # 1 pasivo 2 agresivo
        
        # 1 2
        # 3 4
        self.tableto_movimientos = 0 # 1 2 3 4

        # 1 Humano
        # 2 IA
        self.turno = 1

        #Fuente 
        self.font = pygame.font.Font(None,30)


    def print_tablero(self):
        # recorrido vertical
        for i in range(8):
            if i == 4:
                print("--------------------")
            if i < 4:
                print(str(self.tns[i]) + " " + str(self.tbs[i]))
            else: 
                print(str(self.tni[i-4]) + " " + str( self.tbi[i-4]))


    def dibujar_rect(self, screen, i, j, color, h_g = 0, v_g = 0):

        offset_sombra = 6
        offset_luz = 2

        pygame.draw.rect(
                screen,
                self.cafe_luz,
                pygame.Rect(
                    self.x_offset + h_g + self.escala*j,
                    self.y_offset + v_g + self.escala*i,
                    self.escala - offset_sombra//2, 
                    self.escala - offset_sombra//2))

        pygame.draw.rect(
                screen,
                self.cafe_sombra,
                pygame.Rect(
                    self.x_offset + h_g + self.escala*j + offset_luz,
                    self.y_offset + v_g + self.escala*i + offset_luz,
                    self.escala - offset_luz, 
                    self.escala - offset_luz))

        pygame.draw.rect(
                screen,
                color,
                pygame.Rect(
                    self.x_offset + h_g + self.escala*j + offset_luz,
                    self.y_offset + v_g + self.escala*i + offset_luz,
                    self.escala - offset_sombra, 
                    self.escala - offset_sombra))


    def dibujar_pieza(self, screen, indicador, i, j, h_g=0, v_g=0):
        if indicador == 0:
            # no hacer nada si la no hay fichas
            return 0

        if indicador == 1 :
            # fichas blancas
            color = self.color_fichaBlanca
            color_sombr = self.color_sombra_fichaBlanca
        else : 
            # fichas negras
            color = self.color_fichaNegra
            color_sombr = self.color_sombra_fichaNegra

        pygame.draw.ellipse(
                screen, 
                color_sombr, 
                pygame.Rect(
                    self.x_offset + self.x_offset_ficha + h_g + self.escala*j,
                    self.y_offset + self.y_offset_ficha + v_g + self.escala*i,
                    self.escala_ficha, 
                    self.escala_ficha))

        pygame.draw.ellipse(
                screen, 
                color, 
                pygame.Rect(
                    self.x_offset + self.x_offset_ficha + h_g + self.escala*j,
                    self.y_offset + self.y_offset_ficha + v_g + self.escala*i,
                    self.escala_ficha-4, 
                    self.escala_ficha-4))


    def dibujar_selector(self, screen, i, j, h_g=0, v_g=0):
        pygame.draw.ellipse(
            screen, 
            (125, 223, 100),
            pygame.Rect(
                self.x_offset + self.x_offset_ficha + h_g + self.escala*j - 4,
                self.y_offset + self.y_offset_ficha + v_g + self.escala*i - 4,
                self.escala_ficha + 8, 
                self.escala_ficha + 8,
                ),width=4)

        pygame.draw.ellipse(
            screen, 
            self.color_selection,
            pygame.Rect(
                self.x_offset + self.x_offset_ficha + h_g + self.escala*j - 2,
                self.y_offset + self.y_offset_ficha + v_g + self.escala*i - 2,
                self.escala_ficha + 4, 
                self.escala_ficha + 4,
                ),width=4)


    def obtener_tablero(self):
        if self.tableto_movimientos ==1:
            return self.tns
        elif self.tableto_movimientos == 2:
            return self.tbs
        elif self.tipo_movimiento == 3:
            return self.tni
        elif self.tipo_movimiento == 4:
            return self.tbi

    
    def validar_movimiento(self, i, j, mai, maj):
        if (mai >= 0 and mai < 4)  and (maj >= 0 and maj < 4 ):
            # Movimiento dentro del tablero
            difI = i - mai
            difJ = j - maj
            if (difI*difI <= 4 ) and (difJ*difJ <= 4):
                # el movimiento se esta haciendo maximo de 2 espacios

                if self.tableto_movimientos == 1:
                    # es pasivo, por ende no puede empuajar rocas
                    if difI == 0 or difJ == 0:
                        if difJ == 0:
                            tbTemporal = self.obtener_tablero()
                            if difI < 0:
                                # estoy bajando
                                choq = 0
                                for iterat in range(i+1, mai+1):
                                    if tbTemporal[iterat][j] != 0:
                                        choq += 1
                                    if choq > 0 and self.tipo_movimiento == 1:
                                        return False
                                    if choq > 0 and (iterat != mai):
                                        return False
                                    if choq == 2 :
                                        return False
                            else:
                                # eestoy suibir
                                choq = 0
                                for iterat in range(i-1, mai-1,-1):
                                    if tbTemporal[iterat][j] != 0:
                                        choq += 1
                                    if choq > 0 and self.tipo_movimiento == 1:
                                        return False
                                    if choq > 0 and (iterat != mai):
                                        return False
                                    if choq == 2 :
                                        return False
                        else:
                            tbTemporal = self.obtener_tablero()
                            if difJ < 0:
                                # derecha
                                choq = 0
                                for iterat in range(j+1, maj+1):
                                    if tbTemporal[i][iterat] != 0:
                                        choq += 1
                                    if choq > 0 and self.tipo_movimiento == 1:
                                        return False
                                    if choq > 0 and (iterat != mai):
                                        return False
                                    if choq == 2 :
                                        return False
                            else:
                                # izquierda
                                choq = 0
                                for iterat in range(j-1, maj-1):
                                    if tbTemporal[i][iterat] != 0:
                                        choq += 1
                                    if choq > 0 and self.tipo_movimiento == 1:
                                        return False
                                    if choq > 0 and (iterat != mai):
                                        return False
                                    if choq == 2 :
                                        return False

                         
                    elif difJ*difJ == 1 and difJ*difJ == difI*difI:
                        tbTemporal = self.obtener_tablero

                        if tbTemporal[mai][maj] != 0 and self.tipo_movimiento == 1:
                            return False
                        
                    elif difJ*difJ == 4 and difJ*difJ == difI*difI:
                        if difI < 0:
                            stepi = -1
                        else:
                            stepi = 1

                        if difJ < 0:
                            stepj = -1
                        else:
                            stepj = 1
                        
                        choq = 0
                        if tbTemporal[i+stepi][j+stepj] != 0:
                            if self.tipo_movimiento == 1:
                                return False
                            else:
                                choq += 1   
                        
                        if tbTemporal[i+stepi*2][j+stepj*2] != 0:
                            choq +=1
                            if choq == 2:


                    else :
                        return False 

                else:
                    # es agresivo puede empujar roca, pero no más una
                    pass
            else:
                return False
        else:
            return False


    def dibujar_posibilidades(self, screen):
        pass
        #i = self.pos_selection[0] 
        #j = self.pos_selection[1]

        


    def dibujar_seleccion(self, screen):

        if self.pos_selection != None:
            i = self.pos_selection[0]
            j = self.pos_selection[1]

            if i < 4:
                # superiores
                if j < 4:
                # tablero oscur
                    self.dibujar_selector(screen, i, j )
                else:
                    # tablero claro
                    self.dibujar_selector(screen, i, j, self.h_gap)
            else:
                # inferiores
                if j < 4:
                    # tablero oscur
                    self.dibujar_selector(screen, i, j, 0, self.v_gap)
                else:
                    # tablero claro
                    self.dibujar_selector(screen, i, j, self.h_gap, self.v_gap)

        self.dibujar_posibilidades(screen)


    def dibujar_barra(self, screen):
        if self.turno == 1:
            turnoText = "Turno: Humano"
        else:
            turnoText = "Turno: IA"

        if turnoText == "Turno: Humano":
            if self.tipo_movimiento == 1:
                movimientoText = "PASIVO"
            else:
                movimientoText = "AGRESIVO"
        else:
            movimientoText = "--"

        textoTurnoTRender = self.font.render(turnoText, 0 , ( 174, 246, 199  ))

        if movimientoText == "PASIVO":
            textoTipoMovimiento = self.font.render(movimientoText, 0 , ( 147, 183, 190 ))
        else:
            textoTipoMovimiento = self.font.render(movimientoText, 0 , ( 249, 42, 130 ))
        
        screen.blit(textoTurnoTRender,(0,0))
        screen.blit(textoTipoMovimiento,(200,0))


    def dibujar_all(self, screen):
        # dibujar barra de estado
        self.dibujar_barra(screen)
        # recorrer tablero
        for i in range(8):
            for j in range(8):
                if i < 4:
                    # superiores
                    if j < 4:
                        # tablero oscur
                        self.dibujar_rect(screen, i, j, self.cafe_oscuro)
                        self.dibujar_pieza(screen, self.tns[i][j] , i, j)

                    else:
                        # tablero claro
                        self.dibujar_rect(screen, i, j, self.cafe_claro, self.h_gap)
                        self.dibujar_pieza(screen, self.tbs[i][j-4] , i, j,self.h_gap)
                else:
                    # inferiores
                    if j < 4:
                        # tablero oscur
                        self.dibujar_rect(screen, i, j, self.cafe_oscuro, 0, self.v_gap)
                        self.dibujar_pieza(screen, self.tni[i-4][j] , i, j,0,self.v_gap)
                    else:
                        # tablero claro
                        self.dibujar_rect(screen, i, j, self.cafe_claro, self.h_gap, self.v_gap)
                        self.dibujar_pieza(screen, self.tbi[i-4][j-4] , i, j, self.h_gap, self.v_gap)

        self.dibujar_seleccion(screen)



    def selecionar_pieza(self, x, y):


        limx = self.x_offset + self.h_gap + self.escala*8 - 6
        limy = self.y_offset + self.v_gap + self.escala*8 - 6

        rangoNX = self.x_offset + self.escala*4 - 6
        rangoNY = self.y_offset + self.escala*4 - 6


        # validar ejecucion solo en click para lso tableros
        if ((x <= self.x_offset or y <= self.y_offset) or \
                (x > limx or y > limy)) or \
                (( x > rangoNX and x < rangoNX + self.h_gap +6)or \
                ( y > rangoNY and y < rangoNY + self.v_gap + 6)) :
            return 0

        # determinar la posicion del selector 
        if x <= rangoNX:
            # tablero oscuro izquieda
            if y <= rangoNY:
                # arriba
                j = int((x - self.x_offset) // self.escala)
                i = int((y - self.y_offset) // self.escala)
                print(i,j)
                valor_selecionado = self.tns[i][j]
                self.tableto_movimientos = 1
            else:
                # abajo
                j = int((x - self.x_offset) // self.escala)
                i = int((y - self.y_offset - self.v_gap) // self.escala)
                print(i,j)
                valor_selecionado = self.tni[i-4][j]
                self.tableto_movimientos = 3

        else:
            # tablero claro derecha 
            if y <= rangoNY: 
                # arriba
                j = int((x - self.x_offset - self.h_gap) // self.escala)
                i = int((y - self.y_offset ) // self.escala)
                print(i,j)
                valor_selecionado = self.tbs[i][j-4]
                self.tableto_movimientos = 2

            else:
                # abajo
                j = int((x - self.x_offset - self.h_gap) // self.escala)
                i = int((y - self.y_offset - self.v_gap) // self.escala)
                print(i,j)
                valor_selecionado = self.tbi[i-4][j-4]
                self.tableto_movimientos = 4
            

        if valor_selecionado == 2 :
            # el movimineto que se quiere hacer es pasivo
            if self.tipo_movimiento == 1:
                # si el movimiento esta en tipo pasivo, 
                # solo permitir selecionar los homeboards
                if self.tableto_movimientos == 3 or self.tableto_movimientos == 4:
                    self.pos_selection = (i,j)



