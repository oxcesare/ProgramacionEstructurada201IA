"""
Algoritmo para validacion de ingreso de contraseña
"""

def solicitud_ingreso():
    intentos=0
    clave_correcta = "1234"

    while intentos < 3:
        contra = input("Ingrese su contraseña: ")
        if contra == clave_correcta:
            print("Contraseña correcta. Acceso concedido.")
            return True
        else:
            print("Contraseña incorrecta.")
            intentos += 1
            if intentos == 3:
                print("Cuenta bloqueada. ")
                return False

def main():
    solicitud_ingreso()

if __name__ == "__main__":
    main()                