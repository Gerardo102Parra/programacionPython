class Cuenta:

    def __init__(self, saldo, tipo):
        self.__saldo = saldo
        self.__tipo = tipo

    def getSaldo(self):
        return self.__saldo

    def getTipo(self):
        return self.__tipo

    def retirar(self, cantidad):

        cantidad = float(input("¿Cuánto desea retirar? "))
        if cantidad > self.__saldo:
            print("Fondos insuficientes para retirar.")
            return False
        else:
            self.__saldo -= cantidad
            print(
                f"Has retirado ${cantidad:.2f}. Nuevo saldo: ${self.__saldo:.2f}")
            return True

    def depositar(self, cantidad):
        cantidad = int(input("Cuánto desea depositar? "))
        self.__saldo += cantidad
        print(
            f"Has depositado ${cantidad:.2f}. Nuevo saldo: ${self.__saldo:.2f}")

    def imprimirDetalles(self):
        print(f"Tipo de cuenta: {self.__tipo}")
        print(f"Saldo actual: ${self.__saldo:.2f}")

    def saldoActual(self):
        print(f"Saldo actual: ${self.__saldo:.2f}")

    def __str__(self):
        return f"Cuenta tipo: {self.__tipo}, Saldo: ${self.__saldo:.2f}"
