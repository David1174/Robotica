import pyttsx3

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

def text_to_speech(text):
    """
    Convierte texto a voz.
    :param text: Cadena de texto para convertir a voz.
    """
    try:
        engine.say(text)  # Configurar el texto para ser hablado
        engine.runAndWait()  # Ejecutar la conversión de texto a voz
    except Exception as e:
        print(f"Error al convertir texto a voz: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    while True:
        texto = input("Escribe un texto para convertir a voz (o 'salir' para terminar): ")
        if texto.lower() == "salir":
            print("Programa terminado.")
            break
        text_to_speech(texto)
