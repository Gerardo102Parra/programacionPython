# Autor: Luis Gerardo Parra Cayetano
# Versión: 1.2
# Resumen de la clase: Esta clase permite almacenar los datos del cliente.

from TeoríaClasesYMetodos.Cuenta import *


class Cliente:
    # Los datos del cliente.
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
    # Creamos la función imprimirDetalles para mostrarnos un resumen del cliente

    def imprimirDetallesCliente(self):
        print("Desde el metodo")
        print("Nombre del cliente : ", self.nombre)
        print("Dirección del cliente : ", self.direccion)
        print("Edad del cliente: ", self.edad)
