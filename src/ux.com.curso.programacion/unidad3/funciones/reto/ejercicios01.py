"""
Tabla de multiplicar
"""

def mostrar_tabla():
    # Encabezado de columnas
    print("    ", end="")
    for j in range(1, 11):
        print(f"{j:4}", end="")
    print()
    print("   " + "****" * 10)
    # Filas de la tabla
    for i in range(1, 11):
        print(f"{i:2}*", end="")
        for j in range(1, 11):
            print(f"{i*j:4}", end="")
        print()


def main():
    print("=== Tabla de Multiplicar del 1 al 10 ===")
    mostrar_tabla()

if __name__ == "__main__":
    main()