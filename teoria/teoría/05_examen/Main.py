from Menu import Menu


class PruebasCuentas:
    def __init__(self):
        self.menu_principal = Menu("\n¡Bienvenido a Xavi´s Bank!.")

    def iniciar(self):
        self.menu_principal.darBienvenida()
        self.menu_principal.menuCuentas()


if __name__ == "__main__":
    pruebas = PruebasCuentas()
    pruebas.iniciar()
