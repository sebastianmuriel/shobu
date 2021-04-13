import numpy as np
import pygame
from pygame.math import Vector2

class Tablero:


    def __init__(self):
        # LAS PIEDRAS ESTAN OMPUESTAS:
        # 0 VACIO
        # 1 FICHA BLANCA
        # 2 BICHA NEGRA

        self.tns = np.array(
                [ [0, 1, 1, 1],[0, 0, 0, 0],[1, 0, 0, 0],[2, 2, 2, 2] ])

        #self.tbs = np.array(
        #        [ [1, 1, 1, 1],[0, 0, 0, 0],[0, 0, 0, 0],[2, 2, 2, 2] ])
        self.tbs = np.array(
                [ [1, 1, 1, 1],[2, 2, 0, 0],[0, 0, 0, 0],[0, 0, 2, 2] ])

        self.tni = np.array(
                [ [1, 1, 1, 1],[0, 2, 0, 0],[0, 0, 0, 0],[2, 0, 2, 2] ])

        self.tbi = np.array(
                [ [1, 1, 1, 1],[2, 0, 0, 0],[0, 2, 0, 0],[0, 0, 2, 2] ])

        
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

        # posicion que representa la ficha selecionada
        self.pos_selection = None
        # posibles movimientos cargados por la logica
        # reglamentaria del juego
        self.posibles_movimientos = [] 
        # movimiento guardado desde pasivo para agresivo
        self.movimiento_reciente = None
        self.tableros_obligatorios = 0
        self.tipo_movimiento = 1 # 1 pasivo 2 agresivo
        
        # 1 2
        # 3 4
        self.tableto_movimientos = 0 # 1 2 3 4

        # 1 Humano
        # 2 IA
        self.turno = 1

        #Fuente  
        self.font = pygame.font.Font(None,30)


    # imprimir tablero por consola
    def print_tablero(self):
        # recorrido vertical
        for i in range(8):
            if i == 4:
                print("--------------------")
            if i < 4:
                print(str(self.tns[i]) + " " + str(self.tbs[i]))
            else: 
                print(str(self.tni[i-4]) + " " + str( self.tbi[i-4]))


    # dibujar un rectangulo
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


    # dibujar pieza
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


    # dibujar el selector
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


    # obtener el tablero que se estáa manejando 
    def obtener_tablero(self ):
        if self.tableto_movimientos ==1:
            return self.tns
        elif self.tableto_movimientos == 2:
            return self.tbs
        elif self.tableto_movimientos == 3:
            return self.tni
        elif self.tableto_movimientos == 4:
            return self.tbi


    # dibuja una linea de punto a punto
    def dibujar_linea(self, screen, i, j, si, sj, h_g = 0, v_g = 0, tab_i=0, tab_j=0):
        pygame.draw.line(screen, 
                        (177, 183, 209), 
                        Vector2(self.x_offset + self.x_offset_ficha + h_g + self.escala_ficha/2 + self.escala*(j+tab_j),
                        self.y_offset + self.y_offset_ficha + v_g + self.escala_ficha/2 + self.escala*(i+tab_i)),
                        Vector2(self.x_offset + self.x_offset_ficha + h_g + self.escala_ficha/2 + self.escala*(sj+tab_j),
                        self.y_offset + self.y_offset_ficha + v_g + self.escala_ficha/2 + self.escala*(si+tab_i)),
                        width=3
                    )
        pygame.draw.ellipse(
            screen,
            (177, 183, 209), 
            pygame.Rect(
                self.x_offset + self.x_offset_ficha + h_g + self.escala_ficha/2 + self.escala*(sj+tab_j) - 5,
                self.y_offset + self.y_offset_ficha + v_g + self.escala_ficha/2 + self.escala*(si+tab_i) - 5,
                10,10
            )
        )


    # permite validar un movimiento agresivo determinado
    def validar_movimiento_agresivo(self, i, j, si, sj, tableroAgresivo):
        
        # no desborde la matriz
        if (si < 0 or si > 3 ) or (sj < 0 or sj > 3 ):
            return False
        
        distancia_i = si - i
        distancia_j = sj - j

        if distancia_i < 0:
            #subiendo
            aumentoI = -1
        elif distancia_i > 0:
            # bajando
            aumentoI = 1
        else:
            #quieto
            aumentoI = 0
        
        if distancia_j < 0:
            #izquierda
            aumentoJ = -1
        elif distancia_j > 0:
            #derecha
            aumentoJ = 1
        else:
            #quieto
            aumentoJ = 0
         
        # recorrer cada componente para ver que no hallan piedras
        piedras = 0
        posi = i + aumentoI
        posj = j + aumentoJ
        
        # verifica que no hayan mas de 2 piedras en el camino
        while True:
            # no puedo ocupar una casilla ya ocupada
            if tableroAgresivo[posi][posj] == 2:
                return False

            if tableroAgresivo[posi][posj] == 1:
                piedras += 1

            if piedras == 2:
                return False
            
            if posi == si  and  posj == sj :
                break

            if (posi > 0 and posi < 3) and posi != si:
                posi += aumentoI
            if (posj > 0 and posj < 3) and posj != sj:
                posj += aumentoJ
        
        # la piedra de más adelante
        posi += aumentoI
        posj += aumentoJ

        if (posi >= 0  and posi < 4) and (posj >= 0  and posj < 4):
            if piedras == 1:
                # no puedo empujar una piedra donde ya hay una piedra
                if tableroAgresivo[posi][posj] != 0:
                    return False
        
        return True


    # permite saber si un movimietno se puede replicar de forma agresiva
    def replica_posible(self, i, j, si, sj):
        ## se hace de cuanta de que el movimiento pasivo ya existe
        if self.tableto_movimientos == 3 :
            tableros_agresivos = (self.tbs, self.tbi)
        else :
            tableros_agresivos = (self.tns, self.tni)
        
        # rrecorridos
        recorrido_i = si - i
        recorrido_j = sj - j

        for tabla in tableros_agresivos:
            # reccorer tableros
            for posi in range(4):
                for posj in range(4):
                    if (posi >= 0  and posi < 4) and (posj >= 0  and posj < 4):
                        if tabla[posi][posj] == 2:
                            # encontre una fucha mia, se verifica 
                            # si esta peude replicar mi de maner agresiva
                            if self.validar_movimiento_agresivo(posi,posj,posi + recorrido_i,posj + recorrido_j, tabla):
                                return True
        
        # porque no encontre como replicar el movimiento en 
        # las sotras fichas del ablero de coolor contrario
        return False
        

    # valida un movimento pasivo
    def validar_movimiento_pasivo(self, i, j, si, sj):
        
        if self.tipo_movimiento == 1:
            # seria un movimiento pasivo

            # solo se puede hacer en los tablelor homeboaard
            # 1 2
            # 3 4
            if self.tableto_movimientos != 3 and self.tableto_movimientos != 4:
                return False
            # si no se hace por fuera de la matriz
            if (si < 0 or si > 3 ) or (sj < 0 or sj > 3 ):
                return False
            
            # no pueden empujar piedras
            #   0 1 2 3
            # 0 x x 1 x
            # 1 x x x x
            # 2 x x 1 x
            # 3 x x 2 x

            distancia_i = si - i
            distancia_j = sj - j

            # el movimiento es más largo de lo que debe
            if distancia_i*distancia_j > 4 or distancia_j*distancia_j > 4:
                return False

            if distancia_i < 0:
                #subiendo
                aumentoI = -1
            elif distancia_i > 0:
                # bajando
                aumentoI = 1
            else:
                #quieto
                aumentoI = 0
            
            if distancia_j < 0:
                #izquierda
                aumentoJ = -1
            elif distancia_j > 0:
                #derecha
                aumentoJ = 1
            else:
                #quieto
                aumentoJ = 0
        

            # limite de movimietos es de 2 cacillas
            if distancia_i*distancia_i > 4 or distancia_j*distancia_j > 4:
                return False

            # movimientos en L
            if distancia_i*distancia_i + distancia_j*distancia_j == 5:
                return False
            

            # genero las primeras posiciones
            posi = i + aumentoI
            posj = j + aumentoJ
            
            # verifica que no hayan piedras en el recorrido
            while True:
                # no puedo ocupar empujar si estoy moviendo pasivo

                if (posi < 0 or posi > 3) or (posj < 0 or posj > 3):
                    return False
                
                if self.obtener_tablero()[posi][posj] != 0:
                    return False

                if posi == si  and  posj == sj :
                    break

                if (posi > 0 and posi < 3) and posi != si:
                    posi += aumentoI
                if (posj > 0 and posj < 3) and posj != sj:
                    posj += aumentoJ

            # buscar si la ficha exxiste otra dicha distina a la presente que pueda duplicar el movimiento
            #return self.replica_posible(i, j, si, sj)

            if self.replica_posible(i, j, si, sj):
                
                self.posibles_movimientos.append((si,sj))
                return True
            else:
                return False
            #return True

        else:
            # seria un movimiento agressivo
            return False
            
    
    # dibuja las posibilidades de movimento para una ficha determinada
    def dibujar_posibilidades_pasivas(self, screen):
        if self.tableto_movimientos == 3:
            resi = -4
            resj = 0
        else :
            resi = -4
            resj = -4
        
        i = self.pos_selection[0] + resi
        j = self.pos_selection[1] + resj

        
        for posi in range(i - 2,i + 3 , 1):
            for posj in range(j - 2,j + 3, 1):
                if self.validar_movimiento_pasivo(i ,j,posi,posj):
                    
                    if self.tableto_movimientos == 3:
                        self.dibujar_linea(screen,i,j, posi,posj, 0, self.v_gap, 4, 0)
                        
                    elif self.tableto_movimientos == 4:
                        self.dibujar_linea(screen,i,j, posi,posj, self.h_gap, self.v_gap, 4,4)

        
        #print(self.posibles_movimientos)


    # dibuja las posibilidades de movimientos para una ficha en estado agresivo
    def dibujar_posibilidades_agresivas(self, screen):
        if self.tableto_movimientos == 1:
            resi = 0
            resj = 0
        elif self.tableto_movimientos == 2:
            resi = 0
            resj = -4
        elif self.tableto_movimientos == 3:
            resi = -4
            resj = 0
        else :
            resi = -4
            resj = -4
        
        
        i = self.pos_selection[0] + resi
        j = self.pos_selection[1] + resj
        si = i  +self.movimiento_reciente[0] 
        sj = j  +self.movimiento_reciente[1] 
        
        if self.validar_movimiento_agresivo(i,j,si,sj, self.obtener_tablero()):
            
            if self.tableto_movimientos == 1:
                self.dibujar_linea(screen,i,j, si, sj, 0, 0, 0, 0)

            elif self.tableto_movimientos == 2:
                self.dibujar_linea(screen,i,j, si, sj, self.h_gap, 0, 0, 4)

            elif self.tableto_movimientos == 3:
                self.dibujar_linea(screen,i,j, si, sj, 0, self.v_gap, 4, 0)

            elif self.tableto_movimientos == 4:
                self.dibujar_linea(screen,i,j, si, sj, self.h_gap, self.v_gap, 4, 4)
                



    # dibujar la 
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
        
        if self.pos_selection != None:
            if self.tipo_movimiento == 1:
                # movimiento pasivo
                self.dibujar_posibilidades_pasivas(screen)  
            else: 
                # movimiento agresivo
                
                self.dibujar_posibilidades_agresivas(screen)


    # dibuja la barra superior
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
        self.posibles_movimientos.clear()
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
        
        
    # seleccionar pieza pasivamente
    def iterar(self, x, y):

        limx = self.x_offset + self.h_gap + self.escala*8 - 6
        limy = self.y_offset + self.v_gap + self.escala*8 - 6

        rangoNX = self.x_offset + self.escala*4 - 6
        rangoNY = self.y_offset + self.escala*4 - 6


        # validar ejecucion solo en click para los tableros
        if ((x <= self.x_offset or y <= self.y_offset) or \
                (x > limx or y > limy)) or \
                (( x > rangoNX and x < rangoNX + self.h_gap +6)or \
                ( y > rangoNY and y < rangoNY + self.v_gap + 6)) :
            self.pos_selection = None
            self.posibles_movimientos.clear()
            return 0

        # determinar la posicion del selector 
        if x <= rangoNX:
            # tablero oscuro izquieda
            if y <= rangoNY:
                # arriba
                j = int((x - self.x_offset) // self.escala)
                i = int((y - self.y_offset) // self.escala)
                valor_selecionado = self.tns[i][j]
                self.tableto_movimientos = 1
            else:
                # abajo
                j = int((x - self.x_offset) // self.escala)
                i = int((y - self.y_offset - self.v_gap) // self.escala)
                valor_selecionado = self.tni[i-4][j]
                self.tableto_movimientos = 3

        else:
            # tablero claro derecha 
            if y <= rangoNY: 
                # arriba
                j = int((x - self.x_offset - self.h_gap) // self.escala)
                i = int((y - self.y_offset ) // self.escala)
                
                valor_selecionado = self.tbs[i][j-4]
                self.tableto_movimientos = 2

            else:
                # abajo
                j = int((x - self.x_offset - self.h_gap) // self.escala)
                i = int((y - self.y_offset - self.v_gap) // self.escala)
                
                valor_selecionado = self.tbi[i-4][j-4]
                self.tableto_movimientos = 4
            
        if valor_selecionado == 2 :
            
            # quiero moverme 
            if self.tipo_movimiento == 1:
                # si el movimiento esta en tipo pasivo, 
                # solo permitir selecionar los homeboards
                if self.tableto_movimientos == 3 or self.tableto_movimientos == 4:
                    self.pos_selection = (i,j)
            elif self.tipo_movimiento == 2:
                # el movimiento es agresivo
                if self.tableto_movimientos in self.tableros_obligatorios:
                    self.pos_selection = (i,j)

        else:
            # valido que se quiera colocar una nueva posicon para el moviento pasivo
            if self.pos_selection != None:
                if self.tipo_movimiento == 1:
                    # movimiento pasivo
                    
                    if self.tableto_movimientos == 1:
                        pos_ni = i   
                        pos_nj = j
                    elif self.tableto_movimientos == 2:
                        pos_ni = i   
                        pos_nj = j-4
                    elif self.tableto_movimientos == 3:
                        pos_ni = i-4
                        pos_nj = j

                        pos_rel_i = self.pos_selection[0] - 4
                        pos_rel_j = self.pos_selection[1] 
                    else:
                        pos_ni = i-4
                        pos_nj = j-4

                        pos_rel_i = self.pos_selection[0] - 4
                        pos_rel_j = self.pos_selection[1] - 4

                    
                    if (pos_ni,pos_nj) in self.posibles_movimientos:
                        # pasa a monimiento agresivo
                        self.tipo_movimiento = 2
                        # Mover la ficha de posición
                        if self.tableto_movimientos == 3:
                            # el tablero negro inferior
                            print("Mover en 3", (pos_rel_i, pos_rel_j), (pos_ni,pos_nj))
                            self.tni[pos_rel_i][pos_rel_j] = 0
                            self.tni[pos_ni][pos_nj] = 2
                            
                        elif self.tableto_movimientos == 4:
                            print("Mover en 4", (pos_rel_i, pos_rel_j), (pos_ni,pos_nj))
                            self.tbi[pos_rel_i][pos_rel_j] = 0
                            self.tbi[pos_ni][pos_nj] = 2
                            
                        self.pos_selection = None    
                        # guardar el movimiento agresivo
                        self.movimiento_reciente = (pos_ni- pos_rel_i, pos_nj- pos_rel_j)
                        # guardat tablero agresivo obligatorio
                        if self.tableto_movimientos == 3:
                            # juugue en negro. debo jugar en blanco 
                            self.tableros_obligatorios  = (2,4)
                        elif self.tableto_movimientos == 4:
                            self.tableros_obligatorios  = (1,3)

                        # limitar la interacción con el tablero contrario
                    else:
                        self.pos_selection = None
                        # reinicio posibles jugadas
                        self.posibles_movimientos.clear()
        
                else:
                    # movimiento agresivo
                   
                    if self.tableto_movimientos == 1:
                        pos_ni = i   
                        pos_nj = j

                        pos_rel_i = self.pos_selection[0] 
                        pos_rel_j = self.pos_selection[1] 
                    elif self.tableto_movimientos == 2:
                        pos_ni = i   
                        pos_nj = j-4

                        pos_rel_i = self.pos_selection[0] 
                        pos_rel_j = self.pos_selection[1] -4
                    elif self.tableto_movimientos == 3:
                        pos_ni = i-4
                        pos_nj = j

                        pos_rel_i = self.pos_selection[0] - 4
                        pos_rel_j = self.pos_selection[1] 
                    else:
                        pos_ni = i-4
                        pos_nj = j-4

                        pos_rel_i = self.pos_selection[0] - 4
                        pos_rel_j = self.pos_selection[1] - 4

                    # lo mexclo con el reciente
                    
                    
                    if (pos_ni , pos_nj ) == (pos_rel_i + self.movimiento_reciente[0], pos_rel_j + self.movimiento_reciente[1]):
                        # se puede realizar el movimiento agresivo
                        distancia_i = pos_ni - pos_rel_i
                        distancia_j = pos_nj - pos_rel_j

                        if distancia_i < 0:
                            #subiendo
                            aumentoI = -1
                        elif distancia_i > 0:
                            # bajando
                            aumentoI = 1
                        else:
                            #quieto
                            aumentoI = 0
                        
                        if distancia_j < 0:
                            #izquierda
                            aumentoJ = -1
                        elif distancia_j > 0:
                            #derecha
                            aumentoJ = 1
                        else:
                            #quieto
                            aumentoJ = 0
                        
                        piedras = 0
                        posi = pos_rel_i + aumentoI
                        posj = pos_rel_j + aumentoJ
                        tableroAgresivo = self.obtener_tablero()
                        # verifica que no hayan mas de 2 piedras en el camino
                        while True:

                            if tableroAgresivo[posi][posj] == 1:
                                piedras += 1
                                tableroAgresivo[posi][posj] = 0 # elimino la ficha rival
                            
                            if posi == pos_ni  and  posj == pos_nj :
                                break

                            if (posi > 0 and posi < 3) and posi != pos_ni:
                                posi += aumentoI
                            if (posj > 0 and posj < 3) and posj != pos_nj:
                                posj += aumentoJ

                        # movimiento interno
                        self.obtener_tablero()[pos_ni][pos_nj] = 2
                        self.obtener_tablero()[pos_rel_i][pos_rel_j] = 0

                        # verificar si se corre una piedra o se expulsa
                        posi += aumentoI
                        posj += aumentoJ
                        if (posi >= 0  and posi < 4) and (posj >= 0  and posj < 4):
                            if piedras == 1:
                                # puedo colocar la piedra enemiga de nuevo
                                self.obtener_tablero()[posi][posj] = 1
                        

                        # limpi rastros
                        self.pos_selection = None
                        # reinicio posibles jugadas
                        self.posibles_movimientos.clear()
                        print("Mover agresivammente")

                        # cambio el movimiento
                        self.tipo_movimiento = 1


        

            



            



