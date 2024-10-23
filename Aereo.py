from Transporte import Transporte

class Aereo(Transporte):
    
    def __init__(self, alturaMaxima, tipoAereo, tipoTransporte, capacidad, desplazamiento, velocidadMaxima, kilometraje):
        self.__alturaMaxima = alturaMaxima
        self.__tipoAereo = tipoAereo
        super().__init__(tipoTransporte, capacidad, desplazamiento, velocidadMaxima, kilometraje)
        self.imprimir()
        
    def getTipoAereo(self):
        return self.__tipoAereo