class Menu2:
    def __init__(self, cuenta):
        self.cuenta = cuenta
        self.es_credito = hasattr(cuenta, "getLimiteCredito")

    def realizarOperacion(self):
        while True:
            print("\nOperaciones disponibles:\n")
            if self.es_credito:
                print("1. Pagar")
            else:
                print("1. Depositar")
            print("2. Retirar")
            print("3. Consultar saldo")
            print("0. Volver al menú principal")

            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                try:
                    cantidad = float(input("\nIngrese la cantidad: "))
                    if cantidad <= 0:
                        print("\nCantidad inválida.")
                        continue
                    if self.es_credito:
                        self.cuenta.pagar(cantidad)
                        print("\nPago realizado correctamente.")
                    else:
                        self.cuenta.depositar(cantidad)
                        print(
                            f"\nDepósito exitoso. Nuevo saldo: ${self.cuenta.getSaldo():.2f}")
                except ValueError:
                    print("\nEntrada inválida.")

            elif opcion == "2":
                try:
                    cantidad = float(
                        input("\nIngrese la cantidad a retirar: "))
                    if cantidad <= 0:
                        print("\nCantidad inválida.")
                        continue
                    if self.cuenta.retirar(cantidad):
                        print("\nRetiro exitoso.")
                    else:
                        print(
                            "\nFondos insuficientes o supera el crédito disponible.")
                except ValueError:
                    print("\nEntrada inválida.")

            elif opcion == "3":
                if self.es_credito:
                    print(f"\nDeuda actual: ${self.cuenta.getDeuda():.2f}")
                    print(
                        f"\nLímite de crédito: ${self.cuenta.getLimiteCredito():.2f}")
                    print(
                        f"\nCrédito disponible: ${self.cuenta.getCreditoDisponible():.2f}")
                else:
                    print(f"\nSaldo actual: ${self.cuenta.getSaldo():.2f}")

            elif opcion == "0":
                break
            else:
                print("\nOpción inválida.")
