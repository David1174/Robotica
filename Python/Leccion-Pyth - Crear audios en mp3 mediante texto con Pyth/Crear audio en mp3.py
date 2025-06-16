from gtts import gTTS
from playsound import playsound

# Define el texto que deseas convertir en audio
texto = "Bienvenidos a nuestra expo tecnica, le deseamos que pase un agradable experiencia."

# Configura el idioma (español en este caso)
idioma = "es"

# Genera y guarda el archivo de audio
tts = gTTS(text=texto, lang=idioma)
archivo_audio = "mensaje.mp3"
tts.save(archivo_audio)

# Reproduce el archivo de audio
playsound(archivo_audio)

print("Archivo de audio reproducido con éxito.")
