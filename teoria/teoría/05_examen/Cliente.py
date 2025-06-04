from Cuenta import Cuenta


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

    def obtenerInfoCuentas(self):
        if not self.__cuentas:
            return "Este cliente no tiene cuentas."

        info = [f"Cuentas: {len(self.__cuentas)}"]
        for cuenta in self.__cuentas:
            tipo = cuenta.getTipo()
            saldo = cuenta.getSaldo()
            detalle = f"Cuenta tipo: {tipo}, Saldo: ${saldo:.2f}"
            if tipo.lower() == "crédito" and hasattr(cuenta, 'getLimiteCredito'):
                detalle += f", Límite de crédito: ${cuenta.getLimiteCredito():.2f}"
            info.append(detalle)
        return "\n".join(info)

    def __str__(self):
        return f"{self.__nombre} ({self.__edad} años) - {self.__direccion}"
