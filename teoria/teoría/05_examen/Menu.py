from CuentaDebito import CuentaDebito
from CuentaCredito import CuentaCredito
from MenuOperaciones import Menu2


class Menu:
    def __init__(self, mensaje):
        self.__mensajeBienvenida = mensaje

    def darBienvenida(self):
        print(self.__mensajeBienvenida)

    def menuCuentas(self):
        while True:
            print("\nSeleccione la cuenta:")
            print("1. Débito")
            print("2. Crédito")
            print("0. Salir")
            opcion = input("\nElija alguna opción: ")

            if opcion == "1":
                cuenta = CuentaDebito(450)
                Menu2(cuenta).realizarOperacion()
            elif opcion == "2":
                cuenta = CuentaCredito(200)
                Menu2(cuenta).realizarOperacion()
            elif opcion == "0":
                print("\nGracias por haber visitado Xavi´s Bank.")
                break
            else:
                print("\nOpción no válida.")
