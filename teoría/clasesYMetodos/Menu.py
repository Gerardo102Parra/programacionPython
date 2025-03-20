# Autor: Luis Gerardo Parra Cayetano
# Versión: 1.2
# Resumen de la clase: Esta clase muestra al usurario un menu con una bienvenida, es lo primero que deberá ver el usuario.

from Cuenta import *
from Main import cuenta1


class Menu:
    def __init__(self, banco1):
        self.banco1 = banco1

    def bienvenida(self):
        print(f"Bienvenido a {self.banco1} ")

    def desplegarMenu(self):
        print("Elija una opción: \n 1. Retirar \n 2. Depositar \n 3. Salir ")


mainMenu = Menu("Xavis`s Bank")

mainMenu.bienvenida()


while True:

    mainMenu.desplegarMenu()

    try:
        operacion = int(input("$   "))

        if operacion == 1:  # Si el cliente elige 1, entonces hará un retiro.
            cuenta1.retirar()

        elif operacion == 2:
            cuenta1.depositar

        elif operacion == 3:
            print(" Gracias por usar nuestro banco, hasta luego. ")
            break

        else:
            print("Elija una opción válida, intentelo de nuevo")

    except ValueError:
        print("Elija un número válido: ")
