int motor = 12;  // Pin donde está conectado el MOTOR
char dato;        // Variable para recibir datos del puerto serie

void setup() {
  pinMode(motor, OUTPUT);       // Configura el pin 12 como salida
  digitalWrite(motor, LOW);     // Asegura que el MOTOR inicie apagado
  Serial.begin(115200);            // Inicia la comunicación serie
  Serial.println("Presione A para encender el MOTOR, B para apagarlo");
}

void loop() {
  // Verifica si hay datos disponibles en el puerto serie
  if (Serial.available() > 0) {
    dato = Serial.read();  // Lee el carácter enviado desde la PC
    
    if (dato == 'A' || dato == 'a') {   // Si presionan A o a
      digitalWrite(motor, HIGH);
      Serial.println("MOTOR ENCENDIDO");
    }
    else if (dato == 'D' || dato == 'd') { // Si presionan B o b
      digitalWrite(motor, LOW);
      Serial.println("MOTOR APAGADO");
    }
  }
}
