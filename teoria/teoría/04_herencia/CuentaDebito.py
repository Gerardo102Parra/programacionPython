from Cuenta import Cuenta


class CuentaDebito(Cuenta):
    def __init__(self, saldo):
        super().__init__(saldo, "Débito")
