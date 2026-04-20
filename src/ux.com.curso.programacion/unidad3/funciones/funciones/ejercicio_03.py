import math

# =================================================================
# PROCEDIMIENTOS (Salida visual y organización)
# =================================================================

def mostrar_menu():
    """Procedimiento para mostrar las opciones disponibles."""
    print("\n" + "="*50)
    print("      CALCULADORA DE OPERACIONES MATH AVANZADAS")
    print("="*50)
    print("1. Análisis de Redondeo (ceil, floor, trunc, fabs)")
    print("2. Potencias y Raíces (pow, sqrt, cbrt)")
    print("3. Logaritmos (log, log10, exp)")
    print("4. Trigonometría y Ángulos (sin, cos, radians)")
    print("5. Salir")
    print("="*50)

def limpiar_pantalla():
    """Simula una limpieza de pantalla imprimiendo saltos de línea."""
    print("\n" * 2)

# =================================================================
# FUNCIONES (Lógica matemática y procesamiento)
# =================================================================

def ejecutar_redondeos(n):
    """Realiza operaciones de ajuste numérico."""
    print(f"\n--- Análisis para el número: {n} ---")
    print(f"Valor absoluto (fabs):  {math.fabs(n)}")
    print(f"Redondeo arriba (ceil): {math.ceil(n)}")
    print(f"Redondeo abajo (floor): {math.floor(n)}")
    print(f"Truncado (trunc):       {math.trunc(n)}")

def ejecutar_potencias(base, exp):
    """Calcula potencias y raíces comunes."""
    print(f"\n--- Potencias y Raíces ---")
    print(f"{base} elevado a {exp}: {math.pow(base, exp)}")
    if base >= 0:
        print(f"Raíz cuadrada de {base}: {math.sqrt(base)}")
    else:
        print("Raíz cuadrada: No definida para negativos.")
    # Raíz cúbica (disponible en versiones recientes de Python)
    print(f"Raíz cúbica de {base}: {math.pow(base, 1/3)}")

def ejecutar_logaritmos(valor):
    """Calcula logaritmos en base e y base 10."""
    if valor <= 0:
        print("Error: El logaritmo solo se define para números positivos.")
        return
    
    print(f"\n--- Logaritmos para {valor} ---")
    print(f"Logaritmo natural (ln): {math.log(valor)}")
    print(f"Logaritmo base 10:      {math.log10(valor)}")
    print(f"Exponencial (e^{valor}):  {math.exp(valor)}")

def ejecutar_trigonometria(grados):
    """Convierte grados a radianes y calcula funciones trigonométricas."""
    radianes = math.radians(grados)
    print(f"\n--- Trigonometría para {grados}° ---")
    print(f"Equivalente en radianes: {radianes:.4f}")
    print(f"Seno:   {math.sin(radianes):.4f}")
    print(f"Coseno: {math.cos(radianes):.4f}")

# =================================================================
# BLOQUE PRINCIPAL (Invocación y Control)
# =================================================================

def app():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            num = float(input("Ingrese un número decimal: "))
            ejecutar_redondeos(num)
        
        elif opcion == "2":
            b = float(input("Ingrese la base: "))
            e = float(input("Ingrese el exponente: "))
            ejecutar_potencias(b, e)
            
        elif opcion == "3":
            val = float(input("Ingrese valor positivo: "))
            ejecutar_logaritmos(val)
            
        elif opcion == "4":
            deg = float(input("Ingrese el ángulo en grados: "))
            ejecutar_trigonometria(deg)
            
        elif opcion == "5":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

# Punto de entrada del programa
if __name__ == "__main__":
    app()