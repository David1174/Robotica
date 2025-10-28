import tkinter as tk
import requests

ESP32_IP = "192.168.4.1"  # Cambia si tu ESP32 tiene otra IP
led_on = False  # Variable global para controlar el estado del LED

def toggle_led():
    global led_on
    try:
        if not led_on:
            requests.get(f"http://{ESP32_IP}/led/on", timeout=2)
            button.config(text="Apagar LED", bg="#f44336")
            led_on = True
        else:
            requests.get(f"http://{ESP32_IP}/led/off", timeout=2)
            button.config(text="Encender LED", bg="#4caf50")
            led_on = False
    except Exception as e:
        button.config(text="Error de conexión", bg="#9e9e9e")

# Crear la ventana principal
root = tk.Tk()
root.title("Panel de control ESP32")
root.configure(bg="#e0f7fa")
root.geometry("600x400")
root.resizable(False, False)

# Crear el frame central
frame = tk.Frame(root, bg="#ffffff", bd=4, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=120)

# Etiqueta
label = tk.Label(frame, text="Panel de control ESP32", font=("Arial", 14, "bold"), bg="#ffffff")
label.pack(pady=10)

# Botón para controlar el LED
button = tk.Button(frame, text="Encender LED", width=18, command=toggle_led, bg="#4caf50", fg="white", font=("Arial", 12, "bold"))
button.pack(pady=10)

# Iniciar el loop principal de la ventana
root.mainloop()
