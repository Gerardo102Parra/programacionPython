# Luis Gerardo Parra Cayetano
# Versión: 1.1
# Esta clase cuenta lo que hace es almacenar los atributos que conforman una cuenta de banco.

class Cuenta:
    def __init__(self, valor, tipo, nombre):
        self.saldo = valor
        self.tipo = tipo
        self.nombre = nombre

    def imprimirDetalles(self):
        print("Desde el metodo")
        print("saldo::", self.saldo)
        print("tipo::", self.tipo)
        print("nombre::", self.nombre)

    def retirar(self, cantidad):
        self.saldo = self.saldo-cantidad

    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
