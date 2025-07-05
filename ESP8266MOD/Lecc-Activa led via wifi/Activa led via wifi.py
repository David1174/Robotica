
import tkinter as tk
import requests

class ControlLEDApp:
    def __init__(self, master, esp_ip):
        self.master = master
        self.esp_ip = esp_ip
        self.led_encendido = False

        # Configuración de la ventana
        self.master.title("Control LED")
        self.master.geometry("300x200")
        self.master.configure(bg="#E0F7FA")  # Fondo celeste claro

        # Botón para encender/apagar LED
        self.boton_led = tk.Button(
            self.master,
            text="Encender LED",
            command=self.toggle_led,
            bg="#00838F",
            fg="white",
            font=("Arial", 14),
            width=20
        )
        self.boton_led.pack(pady=60)

    def toggle_led(self):
        try:
            if not self.led_encendido:
                requests.get(f"http://{self.esp_ip}/?LED=ON")
                self.boton_led.config(text="Apagar LED")
                self.led_encendido = True
            else:
                requests.get(f"http://{self.esp_ip}/?LED=OFF")
                self.boton_led.config(text="Encender LED")
                self.led_encendido = False
        except requests.exceptions.RequestException:
            print("No se pudo conectar con el ESP8266")

# IP que entrega el ESP8266 en modo AP por defecto
esp_ip = "192.168.4.1"

root = tk.Tk()
app = ControlLEDApp(root, esp_ip)
root.mainloop()
