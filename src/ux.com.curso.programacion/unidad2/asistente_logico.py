""""
Clasificador de Intenciones
"""
def clasificar_intencion(texto):

    nombre_asistente = "IA-UX"
    print(f"Hola, soy {nombre_asistente}. ¿En qué puedo ayudarte hoy?")
    texto = texto.lower()
    if "hola" in texto or "buenos días" in texto:
        return "¡Hola! Soy tu asistente. Es un gusto saludarte."
    elif "clima" in texto or "temperatura" in texto:
        return "Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado."
    elif "gracias" in texto:
        return "agradecimiento"
    elif "ayuda" in texto:
        return "solicitud de ayuda"
    else:
        return "intención desconocida"

def main():
    while True:
        entrada = input("Escribe un mensaje (o 'salir' para terminar): ")
        if entrada.lower() == "salir":
            print("¡Hasta luego!")
            break
        intencion = clasificar_intencion(entrada)
        print(f"Intención clasificada: {intencion}")

if __name__ == "__main__":
    main()