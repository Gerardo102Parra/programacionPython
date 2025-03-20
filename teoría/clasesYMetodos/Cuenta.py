# Autor: Luis Gerardo Parra Cayetano
# Versión: 1.2
# Resumen de la clase: Esta clase cuenta lo que hace es almacenar los atributos que conforman una cuenta bancaria,
# además de definir operaciones bancarias típicas.

from Main import cuenta1


class Cuenta:
    def __init__(self, valor, tipo):  # Inicializamos.
        # Definimos nuestros parametros (no sé cómo decirlo).
        self.saldo = valor
        self.tipo = tipo

    # Definimos la función imprimirDetalles que nos otorgará un resumen del cliente.
    def imprimirDetallesCuenta(self):
        # print("Desde el metodo")
        print("Saldo del cliente: ", self.saldo)
        print("Tipo de cuenta: ", self.tipo)

    def retirar(self, cantidad):
        # Definimos la operación retirar.
        cantidad = int(input("¿Cuánto desea retirar? "))
        self.saldo = self.saldo-cantidad
        print(
            f"Su nuevo saldo es: \n {cuenta1.saldo}.\n Muchas gracias por usar nuestro banco")

    def depositar(self, cantidad):  # Definimos la operación depositar.
        cantidad = int(input("Cuánto desea depositar? "))
        self.saldo = self.saldo + cantidad
        print(
            f"Su nuevo saldo es: \n{cuenta1.saldo}. \n Muchas gracias por usar nuestro banco")
