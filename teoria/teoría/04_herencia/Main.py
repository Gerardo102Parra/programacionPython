from Cliente import Cliente
from Cuenta import Cuenta
from Menu import Menu

if __name__ == "__main__":
    
    cliente1 = Cliente("Luis Gerardo Parra Cayetano", "Av acueducto 861", "21")
    cuenta1 = Cuenta(1, "Débito")
    cuenta2 = Cuenta(2000000, "Crédito")

    
    cliente1.agregarCuenta(cuenta1)
    cliente1.agregarCuenta(cuenta2)

    
    menu = Menu("Bienvenid@ a Xavi´s Bank", cliente1)
    menu.darBienvenida()
    menu.desplegarOpciones()
