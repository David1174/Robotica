// Código en Arduino
const int ledPins[] = {11, 12, 13}; // Pinos donde conectaremos los LEDs
const int numLeds = sizeof(ledPins) / sizeof(ledPins[0]);
bool gameRunning = false;

void setup() {
  Serial.begin(9600); // Inicializa la comunicación serial
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT); // Configura cada LED como salida
  }
}

void loop() {
  // Revisa si hay comandos disponibles desde el puerto serial
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      gameRunning = true; // Inicia el juego de luces
    } else if (command == '0') {
      gameRunning = false; // Detiene el juego de luces
      turnOffLeds(); // Asegúrate de apagar todos los LEDs al detener
    }
  }

  // Ejecuta el juego de luces si está en marcha
  if (gameRunning) {
    for (int i = 0; i < numLeds; i++) {
      digitalWrite(ledPins[i], HIGH);
      delay(200);
      digitalWrite(ledPins[i], LOW);
    }
  }
}

void turnOffLeds() {
  for (int i = 0; i < numLeds; i++) {
    digitalWrite(ledPins[i], LOW);
  }
}
