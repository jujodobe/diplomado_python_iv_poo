from Transporte import Transporte

class Terrestre(Transporte):

    def __init__(self, tipoDesplazamiento, tipo, capacidad, desplazamiento, velocidadMaxima, kilometraje):
        self.tipoDesplazamiento = tipoDesplazamiento
        super().__init__(tipo, capacidad, desplazamiento, velocidadMaxima, kilometraje)

    def arrancar(self):
        return "Arrancando..."
    
    def acelerar(self):
        return "Acelerando y rodando"
    
    def detener(self):
        return "Deteniendo"