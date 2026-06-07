import os
import doctest

def funciones_generales():
    for i in range(3):
        print(i, end=' ')

    for letter in 'Gadsby':
        print(letter, end=' ')

    print("*****************")        
    for letter in "Gadebe":
        if letter == 'E' or letter == 'e':
            print('This word has an "e"')

def has_e():
    for letter in "Gadebe":
        if letter == 'E' or letter == 'e':
            print('This word has an "e"')

def leer_archivo():
    nombre_archivo = 'words.txt'
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script, nombre_archivo)
    file_object = open(ruta_archivo)
    file_object.readline()
    print(file_object.readline())   
    file_object.close()

def leer_archivo_con_with():
    print("Leyendo el archivo con 'with'...")
    nombre_archivo = 'words.txt'
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script, nombre_archivo)
    file_object = open(ruta_archivo)
    
    for line in open(ruta_archivo):
        word = line.strip()
        print(word)
    
    file_object.close()
        
def uses_any(word, letters):
    """Checks if a word uses any of a list of letters.
    
    >>> uses_any('banana', 'aeiou')
    True
    >>> uses_any('apple', 'xyz')
    False
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False

def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.
    
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    """
    for letter in word.lower():
        if letter in forbidden:
            return False
    return True


def main():
    print("Bienvenido al programa de tareas.")
    has_e()
    leer_archivo()
    leer_archivo_con_with()
    funciones_generales()
    print(uses_any('banana', 'aeiou'))
    doctest.testmod()

if __name__ == "__main__":
    main()