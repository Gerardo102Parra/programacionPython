# Autor: Luis Gerardo Parra Cayetano
# Versión: 1.1
# Resumen de la clase: Esta clase permite almacenar los datos del cliente.


class Cliente:
    def __init__(self, nombre, direccion, edad):  # Los datos del cliente.
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad

    # Creamos la función imprimirDetalles para mostrarnos un resumen del cliente
    def imprimirDetalles(self):
        print("Desde el metodo")
        print("nombre::", self.nombre)
        print("direccion::", self.direccion)
        print("edad::", self.edad)
