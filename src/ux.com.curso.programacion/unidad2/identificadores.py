def imprimir_identificadores():
    # identificadores validos
    nombre_usuario ="Alumno" # Inicia con letra y tiene guión bajo
    sensor = "Temperatura" # inicia con letra
    _id_interno12 =12 # puee contener guión bajo y numeros

    print(nombre_usuario)
    print(sensor)
    print(_id_interno12)

# nombre correcto de funciones
def calcular_area():
    print("Calculando el área...")

def main():
    imprimir_identificadores()
    calcular_area()

if __name__ == "__main__":
    main()
