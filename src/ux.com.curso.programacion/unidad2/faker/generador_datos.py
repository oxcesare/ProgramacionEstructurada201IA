# Importamos la librería externa
from faker import Faker

# Creamos una instancia del generador en español
fake = Faker('es_MX')

print("--- GENERANDO IDENTIDAD SINTÉTICA ---")
print(f"Nombre: {fake.name()}")
print(f"Dirección: {fake.address()}")
print(f"Correo: {fake.email()}")
print(f"Perfil Profesional: {fake.job()}")
