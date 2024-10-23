class Transporte:
    
    def __init__(self, tipo, capacidad, desplazamiento, velocidadMaxima, kilometraje):
        self.__TipoTransporte = tipo
        self.__Capacidad = capacidad
        self.__Desplazamiento = desplazamiento
        self.__VelocidadMaxima = velocidadMaxima
        self.__Kilometraje = kilometraje
    
    def imprimir(self):
        print("El tipo de transporte es: " + self.__TipoTransporte)
        
    def getTipoTransporte(self):
        if(self.__TipoTransporte != ""):
            return self.__TipoTransporte
        else:
            return "Error, el automòvil no tiene un tipo, favor asignarlo."

    def setTipoTransporte(self, tipo):
        if(tipo != ""):
            self.__TipoTransporte = tipo
        else:
            print("Error: No puede asignar un valor nulo a la variable tipo")