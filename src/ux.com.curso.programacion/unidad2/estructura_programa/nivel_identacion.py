# Ejemplo para visualizar cómo la identación define la jerarquía

def explicar_identacion():
    # Nivel 1: Dentro de la función
    mensaje = "Iniciando demostración..."
    print(mensaje)

    puntos = 10
    
    if puntos > 5:
        # Nivel 2: Dentro del bloque 'if'
        # Todo lo que esté alineado aquí pertenece al 'if'
        print("¡Felicidades!")
        print("Has pasado el nivel.")
        
        if puntos == 10:
            # Nivel 3: Dentro de un 'if' anidado
            print("Puntuación perfecta.")
    
    # Volvemos al Nivel 1 (fuera del if)
    print("Fin de la explicación.")

# Nivel 0: Código principal (Global)
if __name__ == "__main__":
    explicar_identacion()