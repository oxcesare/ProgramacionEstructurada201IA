import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# --- UNIDAD 4.4: CARGA DE CONFIGURACIONES EXTERNAS ---
# Cargamos las variables de entorno desde el archivo .env por seguridad
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# --- CONFIGURACIÓN DE INTENTS (UNIDAD 2.2) ---
# Definimos los permisos necesarios que activamos en el Developer Portal
intents = discord.Intents.default()
intents.message_content = True  # Permite al bot leer el contenido de los mensajes

# --- INSTANCIACIÓN DEL BOT ---
# Definimos el prefijo '!' para identificar los comandos
bot = commands.Bot(command_prefix='!', intents=intents)

# --- EVENTO DE CONEXIÓN (UNIDAD 4.1) ---
@bot.event
async def on_ready():
    """
    Evento que se dispara cuando el bot se conecta exitosamente.
    Sirve para confirmar que el intérprete de Python y la API están vinculados.
    """
    print(f'✅ Sistema en línea. Conectado como: {bot.user.name}')
    print('--- Esperando instrucciones en Discord ---')

# --- COMANDO DE PRUEBA (UNIDAD 4.4.2) ---
@bot.command()
async def ping(ctx):
    """
    Comando simple para verificar la latencia de respuesta.
    """
    latencia = round(bot.latency * 1000)
    await ctx.send(f'🏓 ¡Pong! Latencia del agente: {latencia}ms')

# --- EJECUCIÓN DEL PROGRAMA (UNIDAD 1.4) ---
if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("❌ ERROR: No se encontró el TOKEN. Revisa tu archivo .env")