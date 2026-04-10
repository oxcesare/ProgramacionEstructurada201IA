"""
    Algoritmo para el calculo del Fondo de Ahorro
"""
def fondos():
    saldo =0
    meta =1000
    while saldo < meta:
        deposito = int(input("Ingrese el deposito: "))
        saldo += deposito
    return saldo

def main():
    resultado = fondos()
    print("Meta Superada $", resultado)

if __name__ == "__main__":    
    main()
