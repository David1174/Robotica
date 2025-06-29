import tkinter as tk
import requests

ESP32_IP = "192.168.4.1"  # Cambia si tu ESP32 tiene otra IP

class PanelControlESP32(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Panel de control ESP32")
        self.configure(bg="#e0f7fa")
        self.geometry("350x200")
        self.resizable(False, False)

        self.frame = tk.Frame(self, bg="#ffffff", bd=4, relief="groove")
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=120)

        self.label = tk.Label(self.frame, text="Panel de control ESP32", font=("Arial", 14, "bold"), bg="#ffffff")
        self.label.pack(pady=10)

        self.led_on = False
        self.button = tk.Button(self.frame, text="Encender LED", width=18, command=self.toggle_led, bg="#4caf50", fg="white", font=("Arial", 12, "bold"))
        self.button.pack(pady=10)

    def toggle_led(self):
        try:
            if not self.led_on:
                requests.get(f"http://{ESP32_IP}/led/on", timeout=2)
                self.button.config(text="Apagar LED", bg="#f44336")
                self.led_on = True
            else:
                requests.get(f"http://{ESP32_IP}/led/off", timeout=2)
                self.button.config(text="Encender LED", bg="#4caf50")
                self.led_on = False
        except Exception as e:
            self.button.config(text="Error de conexión", bg="#9e9e9e")

if __name__ == "__main__":
    app = PanelControlESP32()
    app.mainloop()