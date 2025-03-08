# Autor: Luis Gerardo Parra Cayetano
# Versión: 1.1
# Resumen de la clase: Esta clase muestra al usurario un menu con una bienvenida, es lo primero que deberá ver el usuario.

from Cuenta import *
from Main import *


class Menu:
    def __init__(self, banco1):
        self.banco1 = Menu

    def bienvenida(self):
        print(f"Bienvenido a {self.banco1} ")

    def desplegarMenu(self):
        print("Elija una opción: \n 1. Retirar \n 2. Depositar \n 3. Salir ")


mainMenu = Menu("Xavis`s Bank")

mainMenu.bienvenida()
mainMenu.desplegarMenu()


operacion = int(input(" Elija una opción: "))

while True:
    mainMenu.desplegarMenu
    try:

        if operacion == 1:  # Si el cliente elige 1, entonces hará un retiro.
            retiro = int(input("¿ Cuánto desea retirar? "))
            cuenta1.retirar(retiro)
            print(
                f" Su nuevo saldo es:\n {cuenta1.saldo}.\n Muchas gracias por usar nuestro banco")
            break

        elif operacion == 2:
            deposito = int(input("¿ Cuánto desea depositar? "))
            cuenta1.depositar(deposito)
            print(
                f" Su nuevo saldo es: \n {cuenta1.saldo}. \n Muchas gracias por usar nuestro banco")
            break

        elif operacion == 3:
            print(" Gracias por usar nuestro banco, hasta luego. ")
            break

        else:
            print("Elija una opción válida, intentelo de nuevo")

    except ValueError:
        print("Elija un número válido: ")


# este es el que ando cambiando, metí todo esto:
