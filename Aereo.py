from Transporte import Transporte

class Aereo(Transporte):
    
    def __init__(self, alturaMaxima, tipoAereo, tipoTransporte, capacidad, desplazamiento, velocidadMaxima, kilometraje):
        self.__alturaMaxima = alturaMaxima
        self.__tipoAereo = tipoAereo
        self.motor = ""
        super().__init__(tipoTransporte, capacidad, desplazamiento, velocidadMaxima, kilometraje)
        self.imprimir()
        
    def getTipoAereo(self):
        return self.__tipoAereo
    
    def setTipoAereo(self, tipoAereo):
        self.__tipoAereo = tipoAereo

    def arrancar(self):
        if(self.motor == "Encendido"):
            return "El motor ya está encendido"
        else:
            self.motor = "Encendido"
            return "Arrancando el motor"
    
    def acelerar(self):
        if(self.motor == "Encendido"):
            return "Acelerando y despegando"
        else:
            return "Primero debes arrancar el motor..."
        
    def detener(self):
        if(self.motor == "Encendido"):
            self.motor == "Apagado"
            return "Apagando el motor"
        else:
            return "El motor ya está apagado" 