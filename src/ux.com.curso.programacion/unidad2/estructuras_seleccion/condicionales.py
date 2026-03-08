# ==========================================================
# DEMOSTRACIÓN DE ESTRUCTURAS CONDICIONALES EN PYTHON
# ==========================================================

def evaluar_acceso(edad, tiene_invitacion):
    """
    Función que demuestra el uso de if, if/else e if/elif/else.
    """
    
    print(f"--- Evaluando para Edad: {edad} e Invitación: {tiene_invitacion} ---")

    # 1. Uso de 'if' simple
    # Solo se ejecuta si la condición es verdadera
    if tiene_invitacion:
        print("Aviso: El usuario posee un pase especial.")

    # 2. Uso de 'if / else'
    # Define dos caminos posibles
    if edad >= 18:
        print("Estado: Mayor de edad.")
    else:
        print("Estado: Menor de edad.")

    # 3. Uso de 'if / elif / else'
    # Permite evaluar múltiples condiciones en orden
    print("Categoría de acceso:")
    if edad < 0:
        print("Error: La edad no puede ser negativa.")
    elif edad < 13:
        print("- Acceso restringido: Categoría Infantil.")
    elif edad < 18:
        print("- Acceso parcial: Categoría Juvenil.")
    elif edad < 65:
        print("- Acceso total: Categoría Adulto.")
    else:
        print("- Acceso total: Categoría Adulto Mayor (Prioritario).")
    
    print("-" * 40)

# Pruebas con diferentes escenarios
if __name__ == "__main__":
    # Caso 1: Solo cumple el if/elif de menores
    evaluar_acceso(10, False)
    
    # Caso 2: Cumple el if simple de invitación y el if/else de adultos
    evaluar_acceso(25, True)
    
    # Caso 3: Evaluación de adulto mayor
    evaluar_acceso(70, False)
    
    # Caso 4: Caso de error
    evaluar_acceso(-5, False)