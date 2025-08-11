import tkinter as tk
import serial

class ControlLED:
    def __init__(self, master, puerto, baudrate=115200):
        self.master = master
        self.master.title("Control LED ESP32")
        self.master.geometry("400x200")

        # Conexión serie con el ESP32
        self.esp32 = serial.Serial(puerto, baudrate, timeout=1)

        # Estado inicial del LED (False = apagado)
        self.led_encendido = False

        # Botón para encender/apagar
        self.boton_led = tk.Button(master, text="Encender LED", width=20, command=self.toggle_led)
        self.boton_led.place(x=100, y=60, width=100, height=30)

    def toggle_led(self):
        """Alterna el estado del LED entre encendido y apagado."""
        if self.led_encendido:
            self.esp32.write(b"OFF\n")
            self.boton_led.config(text="Encender LED", bg="SystemButtonFace")
            self.led_encendido = False
        else:
            self.esp32.write(b"ON\n")
            self.boton_led.config(text="Apagar LED", bg="yellow")
            self.led_encendido = True

if __name__ == "__main__":
    # Cambia "COM3" por tu puerto
    root = tk.Tk()
    app = ControlLED(root, puerto="COM7")
    root.mainloop()
