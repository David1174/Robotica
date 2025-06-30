import tkinter as tk
import serial
import threading

# Cambia el puerto por el que corresponda a tu ESP32 (ejemplo: 'COM3' en Windows, '/dev/ttyUSB0' en Linux)
SERIAL_PORT = 'COM7'
BAUD_RATE = 115200

class PanelControlESP32(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Panel de control ESP32 (Serial)")
        self.configure(bg="#e0f7fa")
        self.geometry("400x250")
        self.resizable(False, False)

        self.frame = tk.Frame(self, bg="#ffffff", bd=4, relief="groove")
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=320, height=150)

        self.label = tk.Label(self.frame, text="Panel de control ESP32", font=("Arial", 14, "bold"), bg="#ffffff")
        self.label.pack(pady=10)

        self.led_on = False
        self.button = tk.Button(self.frame, text="Encender LED", width=18, command=self.toggle_led, bg="#4caf50", fg="white", font=("Arial", 12, "bold"))
        self.button.pack(pady=10)

        self.status = tk.Label(self.frame, text="", bg="#ffffff", fg="#333333", font=("Arial", 10))
        self.status.pack(pady=5)

        # Intentar abrir el puerto serie
        try:
            self.ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
            self.status.config(text=f"Conectado a {SERIAL_PORT}")
        except Exception as e:
            self.ser = None
            self.status.config(text=f"Error: {e}")

    def toggle_led(self):
        if not self.ser or not self.ser.is_open:
            self.status.config(text="Puerto serie no disponible")
            return

        def send_command(cmd):
            try:
                self.ser.write((cmd + '\n').encode())
                respuesta = self.ser.readline().decode().strip()
                self.status.config(text=respuesta)
            except Exception as e:
                self.status.config(text=f"Error: {e}")

        if not self.led_on:
            threading.Thread(target=send_command, args=("ON",), daemon=True).start()
            self.button.config(text="Apagar LED", bg="#f44336")
            self.led_on = True
        else:
            threading.Thread(target=send_command, args=("OFF",), daemon=True).start()
            self.button.config(text="Encender LED", bg="#4caf50")
            self.led_on = False

    def on_closing(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
        self.destroy()

if __name__ == "__main__":
    app = PanelControlESP32()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()