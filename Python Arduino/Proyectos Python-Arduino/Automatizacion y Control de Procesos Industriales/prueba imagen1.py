import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import serial
import time

# Configuración de conexión con Arduino (ajusta el puerto y la velocidad)
try:
    arduino = serial.Serial('COM3', 9600)  # Cambia 'COM3' al puerto de tu Arduino
    time.sleep(2)  # Espera para asegurar la conexión
except:
    arduino = None
    print("No se pudo conectar con Arduino")

# Función para encender o apagar un LED
def toggle_led(led_num):
    if arduino:
        arduino.write(f"{led_num}".encode())  # Enviar comando al Arduino
        print(f"LED {led_num} activado")
    else:
        print("Arduino no conectado")

# Función para convertir texto a audio
def text_to_audio():
    engine = pyttsx3.init()
    engine.say("Bienvenidos al programa de control de LEDs con Arduino")
    engine.runAndWait()

# Configuración de la ventana general de tkinter
window = tk.Tk()
window.title("Control de LEDs con Arduino")
window.geometry("400x300")

# Título
title = tk.Label(window, text="Bienvenidos", font=("Arial", 20))
title.grid(row=0, column=0, columnspan=2, pady=10)

# Cargar e insertar imagen
try:
    image = Image.open(r"D:\Robotica\Z-Imagenes\Naturaleza-1.jpg")  # Reemplaza con la ruta de tu imagen
    image = image.resize((100, 100), Image.LANCZOS)
    img = ImageTk.PhotoImage(image) 
except Exception as e:
    print("No se pudo cargar la imagen:", e)


# Crear un Frame para controlar el layout de la imagen
frame = tk.Frame(window, width=400, height=400)  # Tamaño del Frame
frame.grid(row=0, column=4, pady=10)

# Colocar el Label con la imagen en el Frame y alinearla a la derecha
img_label = tk.Label(frame, image=img)  # 'e' para alinearlo a la derecha(anchor="e")
img_label.pack(side="right", padx=10)  # Empujar la imagen hacia la derecha dentro del Frame




# Botones para activar LEDs en una cuadrícula 2x2
for i in range(1, 5):
    button = tk.Button(window, text=f"LED {i}", command=lambda i=i: toggle_led(i))
    row = (i - 1) // 2 + 2  # Ajusta la fila en función de `i`
    col = (i - 1) % 2       # Ajusta la columna en función de `i`
    button.grid(row=row, column=col, padx=10, pady=10)

# Botón para convertir texto a audio
audio_button = tk.Button(window, text="Convertir texto a audio", command=text_to_audio)
audio_button.grid(row=4, column=0, columnspan=2, pady=10)

# Ejecutar la interfaz gráfica
window.mainloop()

# Cierra la conexión con Arduino al cerrar la ventana
if arduino:
    arduino.close()
