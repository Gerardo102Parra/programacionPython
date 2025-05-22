from Cliente import Cliente
from Cuenta import Cuenta
from Menu import Menu

if __name__ == "__main__":
    # Crear un cliente y cuentas
    cliente1 = Cliente("Luis Gerardo Parra Cayetano", "Av acueducto 861", "21")
    cuenta1 = Cuenta(1, "Débito")
    cuenta2 = Cuenta(2000000, "Crédito")

    # Agregar cuentas al cliente
    cliente1.agregarCuenta(cuenta1)
    cliente1.agregarCuenta(cuenta2)

    # Crear y mostrar el menú
    menu = Menu("Bienvenid@ a Xavi´s Bank", cliente1)
    menu.darBienvenida()
    menu.desplegarOpciones()
