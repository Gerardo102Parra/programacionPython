# Autor: Luis Gerardo Parra Cayetano
# Versión: 1.2
# Resumen de la clase: Esta clase permite almacenar los datos del cliente.

from Cuenta import *


class Cliente:
    # Los datos del cliente.
    def __init__(self, nombre, direccion, edad, Cuenta):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.cuenta = Cuenta
    # Creamos la función imprimirDetalles para mostrarnos un resumen del cliente


#    def imprimirDetallesCliente(self):
# print("\nDetalles del Cliente: \n")
# print("Nombre del cliente : ", self.nombre)
# print("Dirección del cliente : ", self.direccion)
# print("Edad del cliente: ", self.edad)
# print("\nCuenta del cliente : \n")
# self.cuenta.imprimirDetallesCuenta()

def __str__(self):
    return "Nombre del cliente::"+str(self.nombre) + "\n" + "Dirección del cliente::"+str(self.direccion) + "\n" + "Edad del cliente::"+str(self.edad) + "Cuenta del cliente::" + str(self.Cuenta)
