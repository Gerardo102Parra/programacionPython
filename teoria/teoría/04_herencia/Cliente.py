class Cliente:
    def __init__(self, nombre, direccion, edad):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.__cuentas = []

    def agregarCuenta(self, cuenta):
        self.__cuentas.append(cuenta)

    def eliminarCuenta(self, cuenta):
        if cuenta in self.__cuentas:
            self.__cuentas.remove(cuenta)
        else:
            print("La cuenta no existe.")

    def infoDeCuentas(self):
        if len(self.__cuentas) == 0:
            print("Este cliente no tiene cuentas.")
        else:
            print(f"Cuentas: {len(self.__cuentas)}")
        for cuenta in self.__cuentas:
            tipo = cuenta.getTipo()
            saldo = cuenta.getSaldo()

            print(f"Cuenta tipo: {tipo}, Saldo: ${saldo:.2f}", end='')

            # Si es una cuenta de crédito, mostramos el límite
            if tipo.lower() == "crédito" and hasattr(cuenta, 'getLimiteCredito'):
                print(f", Límite de crédito: ${cuenta.getLimiteCredito():.2f}")
            else:
                print()
