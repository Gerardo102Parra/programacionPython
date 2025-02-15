# Luis Gerardo Parra Cayetano
# Versión: 1.1
# Esta clase permite almacenar los datos del cliente y hacer algunas operaciones.


class Cliente:
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad

    def imprimirDetalles(self):
        print("Desde el metodo")
        print("nombre::", self.nombre)
        print("direccion::", self.direccion)
        print("edad::", self.edad)
