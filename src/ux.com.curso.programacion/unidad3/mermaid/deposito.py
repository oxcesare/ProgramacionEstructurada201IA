def calcular_deposito():
    saldo =0
    meta =1000

    while saldo < meta and saldo >= 0:
        depposito = float(input("Ingrese el monto del depósito: "))
        saldo += depposito

    print(f"Metda Superada. Saldo: {saldo}")


def main():
    calcular_deposito()

if __name__ == "__main__":
    main()    




