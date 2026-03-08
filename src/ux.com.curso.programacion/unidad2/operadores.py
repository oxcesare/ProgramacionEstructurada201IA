# ==========================================================
# DEMOSTRACIÓN DE OPERADORES EN PYTHON
# ==========================================================

def demostrar_aritmeticos():
    print("--- Operadores Aritméticos ---")
    a = 10
    b = 3
    
    print(f"Suma: {a} + {b} = {a + b}")
    print(f"Resta: {a} - {b} = {a - b}")
    print(f"Multiplicación: {a} * {b} = {a * b}")
    print(f"División (float): {a} / {b} = {a / b}")
    print(f"División Entera (suelo): {a} // {b} = {a // b}")
    print(f"Módulo (resto de la división): {a} % {b} = {a % b}")
    print(f"Exponente: {a} ** {b} = {a ** b}")
    print("\n")

def demostrar_logicos():
    print("--- Operadores Lógicos ---")
    es_adulto = True
    tiene_licencia = False
    
    # AND: Verdadero si ambos son verdaderos
    print(f"¿Puede conducir? (adulto Y licencia): {es_adulto and tiene_licencia}")
    
    # OR: Verdadero si al menos uno es verdadero
    print(f"¿Necesita transporte? (no es adulto O no tiene licencia): {(not es_adulto) or (not tiene_licencia)}")
    
    # NOT: Invierte el valor booleano
    print(f"Inverso de es_adulto: {not es_adulto}")
    print("\n")

def demostrar_condicionales():
    print("--- Operadores de Comparación (Condicionales) ---")
    x = 15
    y = 20
    
    print(f"¿{x} es igual a {y}?: {x == y}")
    print(f"¿{x} es diferente de {y}?: {x != y}")
    print(f"¿{x} es mayor que {y}?: {x > y}")
    print(f"¿{x} es menor que {y}?: {x < y}")
    print(f"¿{x} es mayor o igual a 15?: {x >= 15}")
    
    print("\nEjemplo de estructura if-elif-else:")
    nota = 85
    if nota >= 90:
        print("Resultado: Excelente")
    elif nota >= 70:
        print("Resultado: Aprobado")
    else:
        print("Resultado: Reprobado")

# Ejecución de las funciones
if __name__ == "__main__":
    demostrar_aritmeticos()
    demostrar_logicos()
    demostrar_condicionales()