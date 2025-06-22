from PIL import Image, ImageTk
import tkinter as tk

# Crear la ventana principal
window = tk.Tk()
window.title("Ventana con Imagen y Botones")
window.geometry("400x300")

# Cargar la imagen
try:
    image = Image.open("D:/Robotica/Z-Imagenes/Escudo-Tec3.jpg")  # Asegúrate de que la ruta es correcta
    image = image.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen (opcional)
    img = ImageTk.PhotoImage(image)
except Exception as e:
    print("No se pudo cargar la imagen:", e)
    img = None  # Si la imagen no se carga, img se establece en None

# Crear una etiqueta de bienvenida
label_welcome = tk.Label(window, text="¡Bienvenidos!", font=("Arial", 16))
label_welcome.grid(row=0, column=0, columnspan=2, pady=20)

# Crear botones para controlar los LEDs
def toggle_led(i):
    print(f"LED {i} activado")

# Crear los botones para activar los LEDs
for i in range(1, 5):
    button = tk.Button(window, text=f"LED {i}", command=lambda i=i: toggle_led(i))
    button.grid(row=i, column=0, pady=5, padx=10, sticky="w")

# Crear un botón para convertir texto a audio
def text_to_audio():
    print("Texto convertido a audio")

audio_button = tk.Button(window, text="Convertir Texto a Audio", command=text_to_audio)
audio_button.grid(row=5, column=0, pady=10, sticky="w")

# Colocar la imagen en una columna separada (costado derecho)
if img is not None:
    img_label = tk.Label(window, image=img)
    img_label.grid(row=0, column=1, rowspan=5, padx=(5, 10), pady=10, sticky="e")  # sticky="e" para alinear a la derecha

# Configurar las columnas para que la imagen esté a la derecha
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=0)

# Iniciar el bucle principal para la interfaz
window.mainloop()
