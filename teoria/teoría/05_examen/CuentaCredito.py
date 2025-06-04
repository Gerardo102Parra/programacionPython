from Cuenta import Cuenta


class CuentaCredito(Cuenta):
    def __init__(self, saldo=0, limite_credito=5000):
        super().__init__(saldo, "Crédito")
        self.__limite_credito = limite_credito

    def getLimiteCredito(self):
        return self.__limite_credito

    def getDeuda(self):
        # Si el saldo es negativo, representa deuda
        return abs(self._saldo) if self._saldo < 0 else 0

    def getCreditoDisponible(self):
        return self.__limite_credito + self._saldo if self._saldo < 0 else self.__limite_credito

    def retirar(self, cantidad):
        disponible = self.getCreditoDisponible()
        if cantidad > disponible:
            return False
        self._saldo -= cantidad  # saldo disminuye (más negativo)
        return True

    def pagar(self, cantidad):
        self._saldo += cantidad  # reducir deuda
        if self._saldo > 0:
            self._saldo = 0  # no puede haber saldo a favor
        return True

    def __str__(self):
        return (
            f"{self.getTipo()} - Deuda actual: ${self.getDeuda():.2f}, "
            f"Límite de crédito: ${self.__limite_credito:.2f}, "
            f"Crédito disponible: ${self.getCreditoDisponible():.2f}"
        )
