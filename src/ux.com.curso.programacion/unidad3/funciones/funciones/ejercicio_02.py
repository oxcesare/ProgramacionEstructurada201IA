import math

# =================================================================
# TEMA 4.1: DEFINICIÓN (MÓDULO MATH)
# =================================================================

# --- PROCEDIMIENTO ---
# Su objetivo es dar formato y mostrar resultados en la terminal.
def imprimir_reporte_circulo(radio):
    """
    Procedimiento que utiliza funciones de math para mostrar 
    información visual, pero no devuelve ningún valor.
    """
    area = math.pi * math.pow(radio, 2)
    perimetro = 2 * math.pi * radio
    
    print("-" * 30)
    print(f"REPORTE PARA RADIO: {radio}")
    print(f"Área: {area:.4f}")
    print(f"Perímetro: {perimetro:.4f}")
    print("-" * 30)

# --- FUNCIÓN ---
# Su objetivo es realizar un cálculo complejo y retornar el valor.
def calcular_hipotenusa(cateto_a, cateto_b):
    """
    Función que calcula la hipotenusa usando el Teorema de Pitágoras.
    Retorna el resultado numérico.
    """
    # math.sqrt calcula la raíz cuadrada
    # math.pow eleva a una potencia
    hipotenusa = math.sqrt(math.pow(cateto_a, 2) + math.pow(cateto_b, 2))
    return hipotenusa


# =================================================================
# TEMA 4.2: INVOCACIÓN
# =================================================================

# 1. Invocando el procedimiento
# Nota: No guardamos esto en una variable porque no retorna nada útil.
imprimir_reporte_circulo(5.5)

# 2. Invocando la función
# Nota: Guardamos el resultado para usarlo en lógica posterior.
lado_a = 3
lado_b = 4
resultado = calcular_hipotenusa(lado_a, lado_b)

print(f"La hipotenusa de un triángulo con catetos {lado_a} y {lado_b} es: {resultado}")

# Ejemplo de invocación anidada (usando el retorno de una función de math directamente)
angulo_grados = 45
# math.sin espera radianes, por lo que usamos math.radians para convertir
seno_valor = math.sin(math.radians(angulo_grados))
print(f"El seno de {angulo_grados}° es aproximadamente: {seno_valor:.4f}")