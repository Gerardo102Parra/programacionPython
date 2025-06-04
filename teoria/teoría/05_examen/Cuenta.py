class Cuenta:
    def __init__(self, saldo, tipo):
        self._saldo = saldo
        self._tipo = tipo

    def getSaldo(self):
        return self._saldo

    def getTipo(self):
        return self._tipo

    def retirar(self, cantidad):
        if cantidad > self._saldo:
            return False
        self._saldo -= cantidad
        return True

    def depositar(self, cantidad):
        self._saldo += cantidad
        return True

    def __str__(self):
        return f"{self._tipo} - Saldo: ${self._saldo:.2f}"
