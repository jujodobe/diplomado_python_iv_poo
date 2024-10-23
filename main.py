# from Automovil import Automovil

# Toyota = Automovil("hatchback", "Toyota", "Rojo")
# Nissan = Automovil("Sedan", "Nissan", "Gris")
# Chevrolet = Automovil("Suv", "Chevrolet", "Blanco")
 
# Toyota.imprimir()
# print(Toyota.getTipo())
# Toyota.imprimir()

from Aereo import Aereo

Avion = Aereo("5000P", "Comercial", "Avion", 120, "Aire", "400 km/h", "500000 km")

print("El tipo de transporte ahora mismo es: " +  Avion.getTipoTransporte())

Avion.setTipoTransporte("")

print("El tipo Aereo es: " + Avion.getTipoAereo() + " El tipo de transporte es: " + Avion.getTipoTransporte())