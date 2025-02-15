# Luis Gerardo Parra Cayetano
# Versión: 1.1
# Aquí es donde se ejecuta el codigo y vemos errores. Es el producto final por así decir.

from Cuenta import *


class Main:
    pass


cuenta1 = Cuenta(10000, "Débito", "Luis Gerardo Parra Cayetano")
print(cuenta1.saldo, cuenta1.tipo, cuenta1.nombre)

# cuenta1.retirar(9500)
# print(cuenta1.saldo)
# cuenta1.depositar(100000)
# print(cuenta1.saldo)
cuenta1.retirar(9999)
cuenta1.imprimirDetalles()
