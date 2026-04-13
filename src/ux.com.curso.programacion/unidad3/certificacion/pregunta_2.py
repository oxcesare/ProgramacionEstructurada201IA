# Funcion que visualiza un triangulo  con asteriscos


def visualizar_triangulo(n):
    for i in range(1, n + 1):
        print(("*" * i).center(n))

def main():
    n = int(input("Ingrese el número de asteriscos en la base del triángulo: "))
    visualizar_triangulo(n)

if __name__ == "__main__":
    main()        