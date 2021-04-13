import numpy as np
from shobu import Tablero

class Nodo:

    def __init__(self, profundidad_padre, estado_heredado, tipo_padre, padre):
        # limitante de profundidad 
        self.profundidad = profundidad_padre -1
        
        # min o max
        if tipo_padre == "MIN":
            self.tipo = "MAX"
        else:
            self.tipo = "MIN"

        #matriz estado a revisar
        self.estado = estado_heredado # se propone como un talbero

        self.padre = padre

        self.valor_utilidad
        
    

    def minimizar(self):    
        pass

    def maximizar(self):
        
        pass

    def utilidad(self):
        return self.valor_utilidad
        pass

    def profundizar(self):

        if self.estado.estado_de_victoria() == "MAQUINA":
            self.valor_utilidad = 999999999
            return self.utilidad()
        elif self.estado.estado_de_victoria() == "HUMANO":
            self.valor_utilidad = -999999999
            return self.utilidad()

        if self.tipo == "MIN":
            self.minimizar()
        else:
            self.maximizar()



        
    