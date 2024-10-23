class Automovil(object):
        
    def __init__(self, _tipo, _marca, _color):
        self.__tipo = _tipo
        self.__Marca = _marca
        self.__Color = _color
    
    def getTipo(self):
        if(self.__tipo != ""):
            return self.__tipo
        else:
            return "Error, el automòvil no tiene un tipo, favor asignarlo."

    def setTipo(self, tipo):
        if(tipo != ""):
            self.__tipo = tipo
        else:
            return "Error: No puede asignar un valor nulo a la variable tipo"
       
    def imprimir(self):
        print("Este vehículo es de la marca: " + self.__Marca)