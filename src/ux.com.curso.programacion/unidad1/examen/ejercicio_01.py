def Datos():
    Limite = 2500  
    VRAM = 0
    
    while VRAM < Limite:
        lotes = float(input("Ingrese el tamaño del lote (MB): "))
        if VRAM + lotes > Limite:
            print(f"Error, la carga de {lotes} MB superaría el límite de {Limite} MB.")
            break
        
        VRAM += lotes
        print("MegaBytes acumulados: ", VRAM)

def main():
    Datos()
    
if __name__ == "__main__":
    main()