int led = 2; // El LED incorporado del ESP32 suele estar en el pin GPIO 2

void setup() {
  pinMode(led, OUTPUT);   // Configura el pin como salida
}

void loop() {
  digitalWrite(led, HIGH); // Enciende el LED
  delay(1000);             // Espera 1 segundo
  digitalWrite(led, LOW);  // Apaga el LED
  delay(1000);             // Espera 1 segundo
}
