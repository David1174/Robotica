// Configurar el pin del LED (en este caso, el pin 13)
const int ledPin = 13;

void setup() {
  // Configurar el pin del LED como salida
  pinMode(ledPin, OUTPUT);
  
  // Inicializar la comunicación serie a 9600 baudios
  Serial.begin(9600);
}

void loop() {
  // Verificar si hay datos disponibles en el puerto serie
  if (Serial.available() > 0) {
    // Leer el byte recibido
    char comando = Serial.read();
    
    // Encender o apagar el LED según el comando recibido
    if (comando == '1') {
      digitalWrite(ledPin, HIGH); // Encender el LED
    } else if (comando == '0') {
      digitalWrite(ledPin, LOW); // Apagar el LED
    }
  }
}
