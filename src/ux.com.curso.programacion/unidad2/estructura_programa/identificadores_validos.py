# 1. IDENTIFICADORES VÁLIDOS (Siguen las reglas de nombres)
nombre_usuario = "Alex"       # Empieza con letra y usa guion bajo
_id_interno = 101             # Puede empezar con guion bajo
puntuacion2 = 50              # Puede contener números (pero no al inicio)

def procesar_datos():         # Nombre de función válido
    pass

# 2. IDENTIFICADORES INVÁLIDOS (Generarían SyntaxError si se descomentan)
# 1er_puesto = "Oro"          # ERROR: Empieza con número
# nombre usuario = "Juan"     # ERROR: Contiene espacios
# precio$ = 10.5              # ERROR: Contiene caracteres especiales ($)

# 3. PALABRAS RESERVADAS (Uso exclusivo del lenguaje)
# No podemos llamar a una variable 'if', 'class' o 'return'
# if = 10                     # ERROR: 'if' es para control de flujo

if puntuacion2 > 40:          # Uso correcto de la palabra reservada 'if'
    resultado = "Aprobado"    # 'resultado' es el identificador de la variable
    print(resultado)          # 'print' es una función integrada

# 4. LISTADO DE PALABRAS RESERVADAS (Ejemplos comunes)
# help("keywords")            # Comando para ver todas en la consola
