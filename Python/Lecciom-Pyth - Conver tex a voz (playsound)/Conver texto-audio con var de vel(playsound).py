from gtts import gTTS
from playsound import playsound
import tempfile
import os
import soundfile as sf
import numpy as np


# Define el texto que deseas convertir en voz
texto = "Bienvenidos a nuestra , que pasen un gran momento en familia junto a nuestros estudiantes."

# Convierte el texto a audio y guárdalo en un archivo temporal
tts = gTTS(text=texto, lang="es")
with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
    temp_path = fp.name
    tts.save(temp_path)

data, samplerate = sf.read(temp_path)
velocidad = 1.11  # Aumenta la velocidad en un 50%
new_data = np.interp(np.arange(0, len(data), velocidad), np.arange(0, len(data)), data)    
sf.write(temp_path, new_data, samplerate)

playsound(temp_path)

# Elimina el archivo temporal después de la reproducción
#os.remove(temp_path)
print("prueba")
