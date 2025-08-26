int ldrPin = A0;  // Pin analógico donde está conectado el divisor con el LDR
int valorLDR = 0;

void setup() {
  Serial.begin(9600);  // Inicializa la comunicación serie
}

void loop() {
  valorLDR = analogRead(ldrPin);  // Lee el valor del LDR (0 - 1023 en Arduino Uno)

  Serial.println(valorLDR);  // Envía el valor al puerto serie
  
  delay(150);  // Pequeño retardo para no saturar el puerto
}
