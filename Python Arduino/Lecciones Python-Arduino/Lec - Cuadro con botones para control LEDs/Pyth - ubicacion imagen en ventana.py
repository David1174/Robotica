import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
window = tk.Tk()
window.title("Ventana con Imagen en Coordenadas Específicas")
window.geometry("500x400")  # Ajustar el tamaño de la ventana según sea necesario

# Ruta de la imagen
image_path = r"D:\Robotica\Z-Imagenes\Escudo-Tec3.jpg"  # Asegúrate de colocar la ruta correcta aquí

# Cargar y mostrar la imagen
try:
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Cambia el tamaño según sea necesario
    tk_image = ImageTk.PhotoImage(image)  # Crear la imagen en un formato compatible con Tkinter

    # Colocar la imagen en un Label y ubicarlo en la ventana
    label_image = tk.Label(window, image=tk_image)
    label_image.image = tk_image  # Mantener una referencia a la imagen
    label_image.place(x=150, y=30)  # Ubicar en las coordenadas deseadas

except Exception as e:
    print("No se pudo cargar la imagen:", e)

# Ejecutar el bucle principal de la ventana
window.mainloop()
