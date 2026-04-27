
import discord
import asyncio
import os
from dotenv import load_dotenv

# --- Unidad 2: Definición de Identificadores ---
load_dotenv()
TOKEN = os.getenv('TOKEN')
CANAL_ID = 123456789012345678  # Reemplaza con el ID de tu canal (sin comillas)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    # Unidad 1.1: Importancia de los lenguajes
    # Aquí el bot ya está "compilado" y conectado al servidor de Discord
    print(f'Conectado exitosamente como {client.user}')
    
    # Unidad 3.3: Aplicación de algoritmo para enviar mensaje inicial
    channel = client.get_channel(CANAL_ID)
    if channel:
        await channel.send("🚀 ¡Hola Mundo! Bot de Programación Estructurada inicializado.")
    else:
        print("Error: No se encontró el canal. Revisa el ID.")

# Ejecutar el cliente
client.run(TOKEN)