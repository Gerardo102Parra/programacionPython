# Autor: Luis Gerardo Parra Cayetano
# Versión: 1.1
# Resumen de la clase: Aquí es donde se ejecuta el codigo y vemos errores. Es el producto final por así decir.

from Cuenta import *  # Importamos todo lo que hemos hecho en Cuenta.


class Main:
    pass


# Nuestros datos
cuenta1 = Cuenta(10000, "Débito", "Luis Gerardo Parra Cayetano")
print(cuenta1.saldo, cuenta1.tipo, cuenta1.nombre)

# cuenta1.retirar(9500)
# print(cuenta1.saldo)
# cuenta1.depositar(100000)
# print(cuenta1.saldo)

cuenta1.retirar(923)  # Ejecutamos operaciones.

# Nos muestra nuestro resumen. Y ejecutando vemos que la operación retirar funciona.
cuenta1.imprimirDetalles()
