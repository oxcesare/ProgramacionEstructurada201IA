"""
EJEMPLOS DE ESTRUCTURAS DE SELECCIÓN MÚLTIPLE EN PYTHON
Este archivo muestra el uso de 'match-case' (Python 3.10+) y el tradicional 'if-elif-else'.
"""

def ejemplo_match_case(dia_numero):
    print(f"--- Usando MATCH-CASE (Entrada: {dia_numero}) ---")
    # El 'match' es la forma moderna de selección múltiple en Python
    match dia_numero:
        case 1:
            print("  Es Lunes.")
        case 2:
            print("  Es Martes.")
        case 3:
            print("  Es Miércoles.")
        case 4:
            print("  Es Jueves.")
        case 5:
            print("  Es Viernes.")
        case 6 | 7:  # El operador '|' permite agrupar múltiples casos
            print("  Es fin de semana.")
        case _:  # El guion bajo es el caso por defecto (default)
            print("  Número de día no válido.")
    print("\n")


def ejemplo_if_elif_else(rol):
    print(f"--- Usando IF-ELIF-ELSE (Entrada: '{rol}') ---")
    # Es la forma clásica de manejar múltiples condiciones
    if rol == "admin":
        print("  Acceso total al sistema.")
    elif rol == "editor":
        print("  Acceso para modificar contenido.")
    elif rol == "invitado":
        print("  Acceso solo de lectura.")
    else:
        print("  Rol no reconocido.")
    print("\n")


def ejemplo_match_avanzado(comando):
    print(f"--- MATCH-CASE con Patrones (Entrada: {comando}) ---")
    # 'match' también permite desestructurar datos
    match comando:
        case ["ir", donde]:
            print(f"  El personaje se mueve hacia: {donde}")
        case ["recoger", objeto]:
            print(f"  Has obtenido: {objeto}")
        case ["atacar"]:
            print("  ¡Ataque básico realizado!")
        case _:
            print("  Comando desconocido.")


def main():
    print("=== DEMOSTRACIÓN DE SELECCIÓN MÚLTIPLE EN PYTHON ===\n")
    
    # Probando match-case básico
    ejemplo_match_case(3)
    ejemplo_match_case(6)
    ejemplo_match_case(99)
    
    # Probando if-elif-else
    ejemplo_if_elif_else("admin")
    ejemplo_if_elif_else("desconocido")
    
    # Probando match-case con listas (Pattern Matching)
    ejemplo_match_avanzado(["ir", "la taberna"])
    ejemplo_match_avanzado(["recoger", "espada de hierro"])
    ejemplo_match_avanzado(["atacar"])

if __name__ == "__main__":
    main()