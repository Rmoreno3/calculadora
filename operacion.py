class Calculadora():
    def __init__(self, x, y):
        try:
            self.suma = x + y
            self.resta = x - y
            self.producto = x * y
            self.division = x // y
            self.elevacion = x ** y
        except:
            print("No se puede Dividir, Multiplicar ni Elevar por 0")
