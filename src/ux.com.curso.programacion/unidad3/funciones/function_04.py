# Calcular el volumen de una esfera
# radio en centímetros
radius = 5  # cm
volume = (4/3) * 3.141592653589793 * (radius ** 3)  # volumen en cm^3
print("El volumen de la esfera es:", volume, "cm cubicos")

# Verificar la identidad trigonométrica: sin^2(x) + cos^2(x) = 1 para x = 42 grados
# En Python, las funciones trigonométricas trabajan con radianes, 
# por lo que primero convertimos los grados a radianes. 
# Luego calculamos sin^2(x) y cos^2(x) y sumamos ambos resultados para verificar la identidad.
import math
x = 42  # grados
x_rad = math.radians(x)  # convertir a radianes
sin2 = math.sin(x_rad) ** 2
cos2 = math.cos(x_rad) ** 2
identidad = sin2 + cos2

print(f"Para x = {x} grados: (sin x)2 + (cos x)2 = {identidad}")

# Parte 3: Cálculo de e^2 de tres formas diferentes
# 1. Usando math.e y el operador de exponenciación
e_pow_2_op = math.e ** 2

# 2. Usando math.pow
e_pow_2_pow = math.pow(math.e, 2)

# 3. Usando math.exp
e_pow_2_exp = math.exp(2)


print("\nCálculo de e^2 de tres formas:")
print("math.e ** 2 =", e_pow_2_op)
print("math.pow(math.e, 2) =", e_pow_2_pow)
print("math.exp(2) =", e_pow_2_exp)

# Comprobación de cuál es más preciso (comparando diferencias)
print("\nDiferencias entre resultados:")
print("|math.e ** 2 - math.pow(math.e, 2)| =", abs(e_pow_2_op - e_pow_2_pow))
print("|math.e ** 2 - math.exp(2)| =", abs(e_pow_2_op - e_pow_2_exp))
print("|math.pow(math.e, 2) - math.exp(2)| =", abs(e_pow_2_pow - e_pow_2_exp))

# Parte 3 