#Funcion para solicitar datos al usuario
def solicitar_datos():
    cantidad = int(input("Ingrese un número entero: "))
    return cantidad

def procesa_datos(cantidad):
    return cantidad * 2


def main():
    cantidad = solicitar_datos()
    resultado = procesa_datos(cantidad)
    print(f"El resultado es: {resultado}")

if __name__ == "__main__":
    main()  
