from operacion import Calculadora


def run():
    pass


print("""
B I E N V E N I D O  A  L A  C A L C U L A D O R A

Indice para operaciones:
    [1]Suma
    [2]Resta
    [3]Multiplicacion
    [4]Division
    [5]Elevacion
""")
try:
    x = int(input("Ingresa el primer valor: "))
    z = int(input("Por favor ingresa el numero de la operacion a realizar: "))
    y = int(input("Ingresa el segundo valor: "))

    operacion = Calculadora(x, y)

    if z == 1:
        print(operacion.suma)
    elif z == 2:
        print(operacion.resta)
    elif z == 3:
        print(operacion.producto)
    elif z == 4:
        print(operacion.division)
    elif z == 5:
        print(operacion.elevacion)
    else:
        print("Ese numero no corresponde al indice >:(")
except:
    print("Debes ingresar NUMEROS >:(")

if __name__ == '__main__':
    run()
