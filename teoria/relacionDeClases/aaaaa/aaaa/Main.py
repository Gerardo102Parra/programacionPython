# Autor: Luis Gerardo Parra Cayetano
# Versión: 1.2
# Resumen de la clase: Aquí es donde se ejecuta el codigo y vemos errores. Es el producto final por así decir.

# Importamos todo lo que hemos hecho en Cuenta y Cliente.
from Cliente import *

# from Menu import *


class Main:
    pass


# Nuestros datos
cuenta1 = Cuenta(10000, "Débito")
cliente1 = Cliente("Luis Gerardo Parra Cayetano",
                   "Av. Acueducto 861. CDMX.", " 18 años")

# cuenta1.retirar(9500)
# print(cuenta1.saldo)
# cuenta1.depositar(100000)
# print(cuenta1.saldo)

cuenta1.retirar(923)  # Ejecutamos operaciones.

# Nos muestra nuestro resumen. Y ejecutando ve


# Aquí ejecuto ambas al mismo tiempo.
cuenta1.imprimirDetallesCuenta()
cliente1.imprimirDetallesCliente()
