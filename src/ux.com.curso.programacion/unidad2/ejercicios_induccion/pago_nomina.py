#Ejercicio de pago de nomina semanal 
numero_horas = float(input("Introduce el número de horas trabajadas en la semana: "))
tarifa_hora = float(input("Introduce la tarifa por hora: "))
nombre_empleado = input("Introduce el nombre del empleado: ")  

# Las horas superiores a 35 se pagan como extras a 1.5 veces la tarifa normal
if numero_horas > 35:
    horas_extras = numero_horas - 35
    pago_bruto = (35 * tarifa_hora) + (horas_extras * tarifa_hora * 1.5)
else:
    pago_bruto = numero_horas * tarifa_hora

print(f"Pago bruto semanal calculado: ${pago_bruto:.2f}")    

#calculo de impuestos
if pago_bruto <=2000:
    impuestos =0
elif pago_bruto <= 2220:    
    impuestos = (pago_bruto - 2000) * 0.20
#el resto se paga al 30%
else:
    impuestos = (pago_bruto - 2220) * 0.30 +  220 * 0.20

pago_neto = pago_bruto - impuestos
# Mostrar el resultado
print(f"Empleado: {nombre_empleado}")
print(f"Pago bruto semanal: ${pago_bruto:.2f}")
print(f"Impuestos retenidos: ${impuestos:.2f}")
print(f"Pago neto semanal: ${pago_neto:.2f}")

