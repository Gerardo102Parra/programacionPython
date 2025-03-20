# Autor: Luis Gerardo Parra Cayetano
# Versión: 1.2
# Resumen de la clase: Esta clase cuenta lo que hace es almacenar los atributos que conforman una cuenta bancaria,
# además de definir operaciones bancarias típicas.

class Cuenta:
    def __init__(self, valor, tipo):  # Inicializamos.
        # Definimos nuestros parametros (no sé cómo decirlo).
        self.__saldo = valor
        self.__tipo = tipo

    # Definimos la función imprimirDetalles que nos otorgará un resumen del cliente.
    def imprimirDetallesCuenta(self):
        # print("Desde el metodo")
        print("Saldo del cliente: ", self.__saldo)
        print("Tipo de cuenta: ", self.__tipo)

    def retirar(self):
        # Definimos la operación retirar.
        cantidad = int(input("¿Cuánto desea retirar? "))
        self.__saldo -= cantidad
        print(
            f"Su nuevo saldo en su tarjeta de {self.__tipo} es: \n {self.__saldo}.\n Muchas gracias por usar nuestro banco")

    def depositar(self):  # Definimos la operación depositar.
        cantidad = int(input("Cuánto desea depositar? "))
        self.__saldo += cantidad
        print(
            f"Su nuevo saldo en su tarjeta de {self.__tipo} es: \n{self.__saldo}. \n Muchas gracias por usar nuestro banco")
