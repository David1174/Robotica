const int buttonPin = 2; // Pin donde está conectado el botón
int buttonState = 0; // Estado del botón anterior
int lastButtonState = 0; // Último estado del botón

void setup() {
  pinMode(buttonPin, INPUT);
  Serial.begin(9600); // Inicializar la comunicación serial
}

void loop() {
  buttonState = digitalRead(buttonPin);

  // Detectar cambio de estado del botón
  if (buttonState != lastButtonState) {
    if (buttonState == HIGH) { // Si se presiona el botón
      Serial.println("ButtonPressed"); // Enviar mensaje a Python
    }
    lastButtonState = buttonState; // Actualizar el estado del botón
    delay(50); // Pequeño retraso para evitar rebotes
  }
}
