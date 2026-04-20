# =================================================================
# TEMA 4.1: DEFINICIÓN DE PROCEDIMIENTOS Y FUNCIONES
# =================================================================

# --- PROCEDIMIENTO ---
# Un procedimiento realiza una acción pero no devuelve un valor
# En Python, si no hay un 'return', la función devuelve 'None' por defecto.
def mostrar_bienvenida(nombre):
    """
    Este es un procedimiento que imprime un saludo en la consola.
    No realiza cálculos para devolver resultados al programa.
    """
    print(f"--- Bienvenida ---")
    print(f"Hola, {nombre}. ¡Bienvenido al sistema!")
    print("------------------")

# --- FUNCIÓN ---
# Una función realiza un proceso o cálculo y devuelve un resultado
# mediante la palabra reservada 'return'.
def calcular_area_rectangulo(base, altura):
    """
    Esta es una función que calcula el área.
    Devuelve el resultado numérico al punto donde fue llamada.
    """
    area = base * altura
    return area


# =================================================================
# TEMA 4.2: INVOCACIÓN DE PROCEDIMIENTOS Y FUNCIONES
# =================================================================

# 1. Invocación de un procedimiento:
# Simplemente se llama por su nombre y se pasan los argumentos.
mostrar_bienvenida("Carlos")

# 2. Invocación de una función:
# Como devuelve un valor, generalmente guardamos el resultado en una variable
# o lo usamos directamente en una expresión.
base_input = 10
altura_input = 5

resultado_area = calcular_area_rectangulo(base_input, altura_input)

# Demostración del uso del valor retornado
print(f"El área calculada para el rectángulo es: {resultado_area} unidades cuadradas.")

# Diferencia visual en la ejecución:
# Intentar imprimir el retorno de un procedimiento resultará en 'None'
valor_procedimiento = mostrar_bienvenida("Ana")
print(f"Valor devuelto por el procedimiento: {valor_procedimiento}") # Imprime None

# Intentar imprimir el retorno de la función mostrará el cálculo
valor_funcion = calcular_area_rectangulo(2, 3)
print(f"Valor devuelto por la función: {valor_funcion}") # Imprime 6