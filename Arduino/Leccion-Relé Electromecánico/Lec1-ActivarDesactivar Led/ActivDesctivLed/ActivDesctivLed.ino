int ledPin = 12;  // Pin donde está conectado el LED
char dato;        // Variable para recibir datos del puerto serie

void setup() {
  pinMode(ledPin, OUTPUT);       // Configura el pin 12 como salida
  digitalWrite(ledPin, LOW);     // Asegura que el LED inicie apagado
  Serial.begin(115200);            // Inicia la comunicación serie
  Serial.println("Presione A para encender el LED, B para apagarlo");
}

void loop() {
  // Verifica si hay datos disponibles en el puerto serie
  if (Serial.available() > 0) {
    dato = Serial.read();  // Lee el carácter enviado desde la PC
    
    if (dato == 'A' || dato == 'a') {   // Si presionan A o a
      digitalWrite(ledPin, HIGH);
      Serial.println("LED ENCENDIDO");
    }
    else if (dato == 'D' || dato == 'd') { // Si presionan B o b
      digitalWrite(ledPin, LOW);
      Serial.println("LED APAGADO");
    }
  }
}
