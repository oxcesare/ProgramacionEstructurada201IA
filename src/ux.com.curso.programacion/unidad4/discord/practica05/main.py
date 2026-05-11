import discord
import os
import re
import datetime
from dotenv import load_dotenv


tareas = []  # Nuestra "base de datos" en memoria (lista)

def mostrar_ayuda():
    """Retorna la lista de comandos disponibles."""
    return (
        "📜 Comandos disponibles:\n"
        "  !add   - Agregar una tarea.\n"
        "  !list  -  Lista las tareas.\n"
        "  !del   -  Eliminar una tarea por su número.\n"
        "  !help  -  Mostrar esta ayuda.\n"
        "  !exit  -  Salir del gestor."
        
    )


# --- TU LÓGICA DE PROGRAMACIÓN (Integrada) ---
def agregar_tarea(lista_tareas, descripcion):
    """
    Agrega una tarea a la lista si cumple con los requisitos.
    Recibe la lista (paso por referencia) y la cadena de descripción.
    """
    if len(descripcion) < 3:
        return " Error: La descripción es muy corta (mínimo 3 caracteres)."
    
    # Creamos un formato de cadena simple para la tarea
    fecha = datetime.datetime.now().strftime("%H:%M")
    nueva_tarea = f"[{fecha}] {descripcion}"
    lista_tareas.append(nueva_tarea)
    return f" Tarea añadida con éxito."

def listar_tareas(lista_tareas):
    """
    Formatea la lista de tareas para su visualización.
    """
    if not lista_tareas:
        return " No hay tareas pendientes en la lista."
    
    resultado = " Listado de Tareas:\n"
    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"  {i}. {tarea}\n"
    return resultado

def eliminar_tarea(lista_tareas, indice_str):
    """
    Elimina una tarea por su número de índice.
    Realiza validaciones de tipo de dato y rango.
    """
    if not indice_str.isdigit():
        return "Error: Debes ingresar el número de la tarea (ej: !borrar 1)."
    
    indice = int(indice_str) - 1
    
    if 0 <= indice < len(lista_tareas):
        tarea_eliminada = lista_tareas.pop(indice)
        return f"🗑️ Tarea eliminada: {tarea_eliminada}"
    else:
        return " Error: El número de tarea no existe en la lista."


def main(entrada):
    
        PREFIJO = "!"
    
        print("=== Bot de Gestión de Tareas (Modo Estructurado) ===")
        print("Comandos: !add [texto], !list, !del [numero], !exit\n")
    
        
        if not entrada.startswith(PREFIJO):
            if entrada: print("Recuerda usar '!' para comandos.")
            
        # Procesamiento de la entrada
        cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""
        
        # Selección de acción (Estructura de control)
        if comando == "exit":
            print("Saliendo del gestor...")
            activa = False
            return "Saliendo del gestor..."
            
        elif comando == "add":
            print(agregar_tarea(tareas, argumento))
            return agregar_tarea(tareas, argumento)
            
        elif comando == "list":            
            print(listar_tareas(tareas))
            return listar_tareas(tareas)    
            
        elif comando == "help":
            print(mostrar_ayuda())
            return mostrar_ayuda()
            
        elif comando == "del":
            print(eliminar_tarea(tareas, argumento))
            return eliminar_tarea(tareas, argumento)
            
        else:
            print(f" Error: Comando '!{comando}' no reconocido.")
            return f" Error: Comando '!{comando}' no reconocido."
        
        print("-" * 20)


# --- CONFIGURACIÓN DE DISCORD ---

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Definir los "intents" (permisos) necesarios
intents = discord.Intents.default()
intents.message_content = True  # Necesario para leer el contenido de los mensajes

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Sincronizado como {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    # Evitar que el bot se responda a sí mismo
    if message.author == client.user:
        return
    
    print("Escribe '!help' para ver los comandos disponibles.\n")

    # 3. Procesamiento: Pasamos el contenido del mensaje a nuestra lógica
    print(f"Mensaje recibido de {message.author}: {message.content}")

      # Solo procesamos si el mensaje empieza con un prefijo (opcional, pero recomendado)
    if message.content.startswith('!'):
        resultado = main(message.content)

        print(f"Resultado del procesamiento: {resultado}")
        
        # 4. Respuesta: El bot escribe el resultado en el mismo canal
        await message.channel.send(f" **Bot Procesador:** {resultado}")
    
# Ejecutar el bot
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN en el archivo .env")