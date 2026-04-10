#Definiendo funciones

def print_lyrics():
    print("I'm a lumberjack and I'm okay.")
    print("I sleep all night and I work all day.")

# Funcion que toma un string como argumento y lo imprime dos veces
def print_twice(String):
    print(String)
    print(String)    

def main():
    print_twice('Dennis Moore,')
    print_lyrics()

if __name__ == "__main__":
    main()