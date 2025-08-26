import pyttsx3

# Inicializa el motor de pyttsx3
engine = pyttsx3.init()

# Función para configurar la velocidad y volumen de la voz
def configurar_voz(velocidad, volumen):
    # Cambiar la velocidad (default es 200)
    engine.setProperty('rate', velocidad)
    # Cambiar el volumen (default es 1.0, que es el máximo)
    engine.setProperty('volume', volumen)  

# Configuración opcional de voz (ajustar la velocidad o volumen)
configurar_voz(160, 1.0)  

#Obtiene la lista de voces del sistema
voices = engine.getProperty('voices')

# Cambia a una voz diferente (prueba con otras si es necesario)
engine.setProperty('voice', voices[2].id)  # Cambia '0' por otro índice para elegir una voz diferente

#engine.setProperty('voice', engine.getProperty('voices')[2].id) # Se puede hacer en un una linea sola

engine.say("Atención, usted está en la Escuela Técnica Nº 3 Eva Perón de Maquinista Sávio")
engine.runAndWait()

