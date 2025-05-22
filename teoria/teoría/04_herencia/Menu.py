from CuentaCredito import CuentaCredito
from Cliente import Cliente
from Cuenta import *
from CuentaCredito import *
from CuentaDebito import *

from CuentaDebito import CuentaDebito
from CuentaCredito import CuentaCredito


class Menu:

    def __init__(self, mensajeBienvenida, cliente):
        self.mensajeBienvenida = mensajeBienvenida
        self.cliente = cliente

    def darBienvenida(self):
        print(self.mensajeBienvenida)

    def desplegarOpciones(self):
        while True:
            print("\nSelecciona una opción:")
            print("1. Gestionar cuentas")
            print("0. Salir")

            opcion = input("Ingresa tu opción: ")

            if opcion == '1':
                self.menuGestionarCuentas()
            elif opcion == '0':
                self.menuSalir()
                break
            else:
                print("Opción no válida. Por favor, selecciona 1 o 0.")

    def menuGestionarCuentas(self):
        while True:
            print("\nSubmenú de Cuentas:")
            print("1. Agregar cuenta")
            print("2. Eliminar cuenta")
            print("3. Mostrar todas las cuentas")
            print("0. Volver al menú principal")

            opcion = input("Ingresa tu opción: ")

            if opcion == "1":
                self.menuAgregarCuenta()
            elif opcion == "2":
                self.menuEliminarCuenta()
            elif opcion == "3":
                self.menuMostrarCuentas()
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Por favor, selecciona 1, 2, 3 o 0.")

    def menuAgregarCuenta(self):
        try:
            tipo = input(
                "Ingresa el tipo de la cuenta (Débito o Crédito): ").strip().lower()
            saldo = float(input("Ingresa el saldo inicial de la cuenta: "))

            if tipo == "débito":
                cuenta = CuentaDebito(saldo)
            elif tipo == "crédito":
                cuenta = CuentaCredito(saldo)
            else:
                print("Tipo de cuenta no reconocido.")
                return

            self.cliente.agregarCuenta(cuenta)
            print(f"Cuenta de tipo '{cuenta.getTipo()}' agregada con éxito.")
            self.menuMostrarCuentas()
        except ValueError:
            print("Por favor, ingresa un valor numérico válido para el saldo.")

    def menuEliminarCuenta(self):
        print("\nEstas son las cuentas disponibles para eliminar:")
        self.cliente.infoDeCuentas()

        if len(self.cliente._Cliente__cuentas) == 0:
            print("No hay cuentas disponibles para eliminar.")
            return

        try:
            tipo = input(
                "\nIngresa el tipo de la cuenta que deseas eliminar: ")
            cuenta_a_eliminar = None

            for cuenta in self.cliente._Cliente__cuentas:
                if cuenta.getTipo().lower() == tipo.lower():
                    cuenta_a_eliminar = cuenta
                    break

            if cuenta_a_eliminar:
                self.cliente.eliminarCuenta(cuenta_a_eliminar)
                print(f"Cuenta de tipo '{tipo}' eliminada con éxito.")
            else:
                print(f"No se encontró una cuenta con el tipo '{tipo}'.")
            self.menuMostrarCuentas()
        except Exception as e:
            print(f"Ocurrió un error al eliminar la cuenta: {e}")

    def menuMostrarCuentas(self):
        print("\nInformación de las cuentas del cliente:")
        self.cliente.infoDeCuentas()

    def menuSalir(self):
        print("Saliendo del sistema. Gracias por usar nuestros servicios.")
