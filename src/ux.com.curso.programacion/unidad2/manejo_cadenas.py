# ==========================================================
# DEMOSTRACIÓN DE MANEJO DE CADENAS (STRINGS) EN PYTHON
# ==========================================================

def demostrar_concatenacion():
    print("--- Concatenación ---")
    nombre = "Juan"
    apellido = "Pérez"
    
    # Uso del operador +
    nombre_completo = nombre + " " + apellido
    print("Unión con '+': " + nombre_completo)
    
    # Uso de join (más eficiente para listas largas)
    palabras = ["Python", "es", "genial"]
    frase = " ".join(palabras)
    print("Unión con join(): " + frase)
    print("\n")

def demostrar_interpolacion():
    print("--- Interpolación (Formateo) ---")
    usuario = "Alex"
    puntos = 150
    
    # f-strings (La forma moderna y recomendada)
    mensaje_f = f"Hola {usuario}, tienes {puntos} puntos acumulados."
    print("f-string: " + mensaje_f)
    
    # Método .format()
    mensaje_format = "Usuario: {}. Puntos: {}.".format(usuario, puntos)
    print(".format(): " + mensaje_format)
    print("\n")

def demostrar_slicing():
    print("--- Slicing (Rebanado) ---")
    texto = "Aprendiendo Python"
    
    # Sintaxis: [inicio:fin:paso]
    print(f"Texto original: '{texto}'")
    print(f"Primeros 11 caracteres: '{texto[:11]}'")
    print(f"Desde el índice 12 al final: '{texto[12:]}'")
    print(f"Invertir la cadena: '{texto[::-1]}'")
    print(f"Saltando de 2 en 2: '{texto[::2]}'")
    print("\n")

def demostrar_metodos_integrados():
    print("--- Métodos Integrados de Transformación ---")
    frase_sucia = "   hola a todos, esto es python   "
    
    # Transformaciones básicas
    print(f"Original: '{frase_sucia}'")
    print(f"Mayúsculas (upper): '{frase_sucia.upper()}'")
    print(f"Minúsculas (lower): '{frase_sucia.lower()}'")
    print(f"Limpiar espacios (strip): '{frase_sucia.strip()}'")
    
    # Split y Replace
    lista_palabras = frase_sucia.strip().split(" ")
    print(f"Separado por espacios (split): {lista_palabras}")
    
    reemplazo = frase_sucia.replace("python", "Java").strip()
    print(f"Reemplazo de texto: '{reemplazo}'")
    print("\n")

# Ejecución de las funciones
if __name__ == "__main__":
    demostrar_concatenacion()
    demostrar_interpolacion()
    demostrar_slicing()
    demostrar_metodos_integrados()