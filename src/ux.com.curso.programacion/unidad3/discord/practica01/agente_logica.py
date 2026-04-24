def procesar_pregunta(mensaje_usuario):
    """
    Función que recibe un texto y decide qué responder.
    Implementa Programación Estructurada pura.
    """
    # 1. Normalización (Paso fundamental en IA)
    mensaje = mensaje_usuario.lower().strip()
    
    # 2. Base de conocimientos (Diccionario)
    conocimiento = {
         # Conceptos de Estructura de Control
        "if": "La sentencia 'if' es un condicional. Permite que el programa tome decisiones basándose en una condición booleana.",
        "else": "Se usa junto al 'if' para ejecutar un bloque de código cuando la condición principal es falsa.",
        "elif": "Es la abreviatura de 'else if'. Permite verificar múltiples condiciones de forma secuencial.",
        "while": "Es un bucle que se repite 'mientras' una condición sea verdadera. ¡Cuidado con los bucles infinitos!",
        "for": "En Python, el bucle 'for' es un iterador que recorre elementos de una secuencia (lista, rango, cadena).",
        
        # Tipos de Datos
        "int": "Representa números enteros (ej. 5, -10, 0). No tienen parte decimal.",
        "float": "Representa números de punto flotante o decimales (ej. 3.1416, 2.0).",
        "str": "Cadenas de texto o 'strings'. Se definen entre comillas simples '' o dobles \"\".",
        "bool": "Tipo de dato booleano: solo puede ser True (Verdadero) o False (Falso).",
        "list": "Una lista es una colección ordenada y mutable de elementos. Se definen con corchetes [].",
        "dict": "Un diccionario es una colección de pares clave-valor. Se definen con llaves {}.",
        
        # Funciones y Modularidad
        "def": "Es la palabra reservada para definir una función en Python.",
        "return": "Se utiliza dentro de una función para devolver un resultado al llamador y finalizar la ejecución de la función.",
        "argumentos": "Son los valores que le pasas a una función para que trabaje con ellos.",
        "scope": "O 'alcance', se refiere a la visibilidad de las variables (locales vs globales).",
        
        # Operadores y Sintaxis
        "print": "Función que muestra información en la consola o salida estándar.",
        "input": "Función que permite al usuario ingresar datos desde el teclado como texto (string).",
        "len": "Devuelve la longitud o número de elementos de un objeto (como una lista o un string).",
        "range": "Genera una secuencia de números, muy útil en los bucles 'for'.",
        "import": "Se usa para traer módulos o librerías externas a tu código actual.",
        
        # Conceptos de Programación Estructurada
        "algoritmo": "Es una serie de pasos ordenados y finitos para resolver un problema.",
        "identacion": "En Python es obligatoria. Define qué bloques de código pertenecen a qué estructura (if, for, def).",
        "comentarios": "Se crean con el símbolo #. Sirven para explicar el código y son ignorados por el intérprete."
    }
    
    # 3. Lógica de búsqueda
    for clave in conocimiento:
        if clave in mensaje:
            return conocimiento[clave]
    
    return "Lo siento, aún no sé qué es eso. ¡Pregúntame sobre variables, funciones o bucles!"

def mmain():
    print("¡Hola! Soy tu asistente de programación. Pregúntame sobre variables, funciones o bucles.")
    while True:
        user_input = input("Alumno -> ")
        if user_input.lower() == "salir": break
        
        respuesta = procesar_pregunta(user_input)
        print(f"Bot -> {respuesta}")
    

# Prueba local (Offline)
if __name__ == "__main__":
    mmain()
    