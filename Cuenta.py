# Autor: Luis Gerardo Parra Cayetano
# Versión: 1.1
# Resumen de la clase: Esta clase cuenta lo que hace es almacenar los atributos que conforman una cuenta bancaria,
# además de definir operaciones bancarias típicas.

class Cuenta:
    def __init__(self, valor, tipo, nombre):  # Inicializamos.
        # Definimos nuestros parametros (no sé cómo decirlo).
        self.saldo = valor
        self.tipo = tipo
        self.nombre = nombre

    # Definimos la función imprimirDetalles que nos otorgará un resumen del cliente.
    def imprimirDetalles(self):
        print("Desde el metodo")
        print("saldo::", self.saldo)
        print("tipo::", self.tipo)
        print("nombre::", self.nombre)

    def retirar(self, cantidad):  # Definimos la operación retirar.
        self.saldo = self.saldo-cantidad

    def depositar(self, cantidad):  # Definimos la operación depositar.
        self.saldo = self.saldo + cantidad
