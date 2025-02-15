# Luis Gerardo Parra Cayetano
# Versión: 1.1
# Esta clase cuenta lo que hace es almacenar los atributos que conforman una cuenta de banco.

class Cuenta:
    def __init__(self, valor, tipo, nombre):
        self.saldo = valor
        self.tipo = tipo
        self.nombre = nombre


# Esto es lo de la tarea, pero no estoy seguro cómo se hace, ni como ejecutarlo, el lunes pregunto.
def retirar(self, cantidad):
    self.saldo = self.saldo-cantidad


def depositar(self, cantidad):
    self.saldo = self.saldo + cantidad
