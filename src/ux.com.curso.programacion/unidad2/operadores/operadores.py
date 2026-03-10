"""
DEMOSTRACIÓN DE OPERADORES EN PYTHON
Este script ejemplifica el uso de operadores aritméticos, lógicos y relacionales.
Cada grupo de operadores está encapsulado en su propia función.
"""

def demostrar_aritmeticos(a, b):
    print(f"--- Operadores Aritméticos con {a} y {b} ---")
    print(f"Suma (+):           {a + b}")
    print(f"Resta (-):          {a - b}")
    print(f"Multiplicación (*): {a * b}")
    print(f"División (/):       {a / b}")
    print(f"División Entera (//): {a // b}")
    print(f"Residuo/Módulo (%):   {a % b}")
    print(f"Exponente (**):      {a ** b}")
    print("\n")

def demostrar_relacionales(a, b):
    print(f"--- Operadores Condicionales (Relacionales) con {a} y {b} ---")
    print(f"Igualdad (==):      {a == b}")
    print(f"Diferente (!=):     {a != b}")
    print(f"Mayor que (>):      {a > b}")
    print(f"Menor que (<):      {a < b}")
    print(f"Mayor o igual (>=): {a >= b}")
    print(f"Menor o igual (<=): {a <= b}")
    print("\n")

def demostrar_logicos(p, q):
    print(f"--- Operadores Lógicos con {p} y {q} ---")
    # AND: True si ambos son verdaderos
    print(f"AND (y):  {p} and {q} = {p and q}")
    # OR: True si al menos uno es verdadero
    print(f"OR (o):   {p} or {q}  = {p or q}")
    # NOT: Invierte el valor booleano
    print(f"NOT (no): not {p}     = {not p}")
    print("\n")

def main():
    print("=== EJEMPLO DE OPERADORES EN PYTHON ===\n")
    
    # 1. Pruebas Aritméticas
    demostrar_aritmeticos(10, 3)
    
    # 2. Pruebas Relacionales
    demostrar_relacionales(15, 20)
    
    # 3. Pruebas Lógicas
    demostrar_logicos(True, False)

if __name__ == "__main__":
    main()