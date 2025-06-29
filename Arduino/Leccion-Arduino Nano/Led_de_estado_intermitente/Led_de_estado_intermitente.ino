void setup() {
  
  pinMode(LED_BUILTIN, OUTPUT); // Configura el LED integrado como salida
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // Enciende el LED
  delay(100);                      // Espera 500 ms
  digitalWrite(LED_BUILTIN, LOW);  // Apaga el LED
  delay(80);                      // Espera 500 ms
}
