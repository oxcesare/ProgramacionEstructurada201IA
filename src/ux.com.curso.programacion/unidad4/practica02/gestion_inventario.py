import numpy as np

def gestion_inventario(precios, cantidades):
    # 1. DEFINICIÓN DE UN VECTOR
    # Precios de los productos: [Poción, Espada, Escudo]
    precios = np.array([50, 150, 100])

    # 2. DEFINICIÓN DE UNA MATRIZ 
    # Cantidades que tienen 3 usuarios diferentes
    # Fila 0: Usuario A, Fila 1: Usuario B, Fila 2: Usuario C
    inventarios = np.array([
        [5, 1, 0],  # Usuario A: 5 pociones, 1 espada, 0 escudos
        [2, 0, 1],  # Usuario B
        [10, 2, 2]  # Usuario C
    ])

def calculo_inventario(inventarios, precios):
        # 3. OPERACIONES SOBRE ARREGLOS
        # Calcular cuánto dinero tiene cada usuario en objetos (Matriz x Vector)
        riqueza_total = np.dot(inventarios, precios)

        print("=== REPORTE DE ECONOMÍA DEL SERVIDOR ===")
        print(f"Precios unitarios: {precios}")
        print(f"Riqueza por usuario: {riqueza_total}")
        print(f"El usuario más rico tiene: {np.max(riqueza_total)} monedas.")

        #Axis = 0 = columna 
        #Axis = 1 = fila
        #suma de inventarios por producto
        total_pociones = np.sum(inventarios[:, 0])
        total_espadas = np.sum(inventarios[:, 1])
        total_escudos = np.sum(inventarios[:, 2])

        print(f"Total de pociones: {total_pociones}")
        print(f"Total de espadas: {total_espadas}")
        print(f"Total de escudos: {total_escudos}")

def main():
    precios = np.array([50, 150, 100])
    inventarios = np.array([
        [5, 1, 0],  # Usuario A
        [2, 0, 1],  # Usuario B
        [10, 2, 2]  # Usuario C
    ])
    calculo_inventario(inventarios, precios)

if __name__ == "__main__":
    main()   
