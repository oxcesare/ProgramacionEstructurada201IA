import math

#Create a variable named x with this value. 
x = 42
# Then use math.cos and math.sin to compute the sine and cosine of ,
seno_x = math.sin(x)
conseno_x = math.cos(x)
#and the sum of their squared.
resultado = seno_x**2 + conseno_x**2
resultado_2 = math.pow(seno_x, 2) + math.pow(conseno_x, 2)
print("La suma del seno y coseno de", x,"es:", math.sqrt(resultado))
print("La suma del seno y coseno de", x,"es:", math.sqrt(resultado_2))





