import math
from datetime import datetime

#Crea un bloque llamado imprimir_encabezado.
#Este bloque no debe devolver ningún dato, solo debe imprimir en la consola 
# un diseño visual con el nombre "Sistema de Salud Inteligente" y la fecha actual.
def imprimir_encabezado():
    print("====================================")
    print("   Sistema de Salud Inteligente")
    #Obtener fecha dinamicamente
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    print("   Fecha:", fecha_actual)
    print("====================================")

#Crea un bloque llamado calcular_imc.
#Debe recibir dos valores: peso (kg) y estatura (metros).
#Este bloque debe devolver (return) el resultado de la fórmula: peso / (estatura ** 2).   
def calcular_imc(peso, estatura):
    if estatura <= 0:
        raise ValueError("La estatura debe ser mayor que cero.")
    imc = peso / (estatura ** 2)
    return imc

#Crea un bloque llamado evaluar_presion.
#Debe recibir la presion_sistolica (ej. 120).
#Si el valor es mayor a 140, debe devolver la palabra "Alta". De lo contrario, debe devolver "Normal".
def evaluar_presion(presion_sistolica):
    if presion_sistolica >= 140:
        return "Alta"
    else:
        return "Normal"

def main():
    imprimir_encabezado()

    print("Ingrese los datos del paciente:")
    print("Ingrese el nombre del paciente:")
    nombre = input()
    print("Ingrese el peso del paciente en kg:")
    peso = float(input())
    print("Ingrese la estatura del paciente en metros:")
    estatura = float(input())
    print("Ingrese la presión sistólica del paciente:")
    presion_sistolica = int(input())

    imc = calcular_imc(peso, estatura)
    presion_evaluada = evaluar_presion(presion_sistolica)

    print("====================================")
    print(" SISTEMA DE SALUD INTELIGENTE  ")
    print("====================================")
    print(f"Paciente: {nombre}")
    print(f"IMC Calculado:  {imc:.2f}")
    print(f"Estado de Presión: ({presion_evaluada})")

if __name__ == "__main__":
    main()