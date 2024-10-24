# from Automovil import Automovil

# Toyota = Automovil("hatchback", "Toyota", "Rojo")
# Nissan = Automovil("Sedan", "Nissan", "Gris")
# Chevrolet = Automovil("Suv", "Chevrolet", "Blanco")
 
# Toyota.imprimir()
# print(Toyota.getTipo())
# Toyota.imprimir()

from Aereo import Aereo
from Terrestre import Terrestre

Avion = Aereo("5000P", "Comercial", "Avion", 120, "Aire", "400 km/h", "500000 km")

# print("El tipo de transporte ahora mismo es: " +  Avion.getTipoTransporte())

# Avion.setTipoTransporte("Avioneta")
# Avion.setTipoAereo("Privada")

# print("El tipo Aereo es: " + Avion.getTipoAereo() + " El tipo de transporte es: " + Avion.getTipoTransporte())
print(Avion.arrancar())
print(Avion.acelerar())
print(Avion.arrancar())
print(Avion.detener())
print(Avion.detener())

print("###################################################################################")
print("Trabajando con Coche")
print("###################################################################################")

Coche = Terrestre("4 Ruedas", "Avion", 120, "Aire", "400 km/h", "500000 km")

print(Coche.arrancar())
print(Coche.acelerar())
print(Coche.detener())
