# Ejemplo del uso de raise en python, esta palabra clave se utiliza para lanzar una excepción de forma explícita.
# Ilustrar el ejemplo dejando un print en el bloque del if  para demostrar que el flujo continua, lo cual es 
# Incorrecto

def set_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    return edad

def main():
    try:
        edad = set_edad(-5)
        print(f"La edad es: {edad}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()