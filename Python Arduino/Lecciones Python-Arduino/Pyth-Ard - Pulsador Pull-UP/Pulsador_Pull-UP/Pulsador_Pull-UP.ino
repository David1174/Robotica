const int buttonPin = 7;  // Pin al que está conectado el pulsador
int buttonState = 0;      // Variable para guardar el estado del botón

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);  // Configura el pin como entrada con resistencia interna pull-up
  Serial.begin(9600);                // Inicializa la comunicación serial
}

void loop() {
  buttonState = digitalRead(buttonPin);  // Lee el estado del botón

  if (buttonState == LOW) {  // Si el botón está presionado
    Serial.println("ON");    // Envía "ON" por serial
  } else {
    Serial.println("OFF");   // Envía "OFF" por serial
  }
  delay(100);  // Pequeño retardo para evitar rebotes
}
