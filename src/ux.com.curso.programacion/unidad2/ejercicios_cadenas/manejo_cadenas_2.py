#Manejo de Cadenas

def funcion_a(cadena):
    return cadena.upper()

def funcion_b(cadena):
    return cadena[0:8]

def funcion_c(cadena):
    return cadena.split()[0]

def funcion_d(cadena):
    return cadena.replace("o", "0").replace("a", "4")

def funcion_e(cadena):
    return cadena.count("o")


def main():
    cadena = "Hola  ooo Mundo"
    print(funcion_a(cadena))
    print(funcion_b(cadena))
    print(funcion_c(cadena))
    print(funcion_d(cadena))
    print(funcion_e(cadena))

if __name__ == "__main__":
    main()   