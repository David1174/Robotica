#define LED_PIN 2  // Cambia por el pin que uses para el LED

void setup() {
  Serial.begin(115200);      // Inicia la comunicación serial
  pinMode(LED_PIN, OUTPUT);  // Configura el pin como salida
  digitalWrite(LED_PIN, LOW);
}

void loop() {
  if (Serial.available()) {
    String comando = Serial.readStringUntil('\n');
    comando.trim(); // Elimina espacios y saltos de línea

    if (comando == "ON") {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("LED encendido");
    } else if (comando == "OFF") {
      digitalWrite(LED_PIN, LOW);
      Serial.println("LED apagado");
    } else {
      Serial.println("Comando no reconocido");
    }
  }
}
