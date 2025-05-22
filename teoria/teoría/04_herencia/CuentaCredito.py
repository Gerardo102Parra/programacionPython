from Cuenta import Cuenta


class CuentaCredito(Cuenta):
    def __init__(self, saldo, limite_credito=5000):
        super().__init__(saldo, "Crédito")
        self.__limite_credito = limite_credito

    def getLimiteCredito(self):
        return self.__limite_credito
