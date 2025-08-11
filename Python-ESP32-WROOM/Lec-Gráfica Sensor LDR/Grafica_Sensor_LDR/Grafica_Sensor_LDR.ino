void setup() {
  Serial.begin(115200);
}

void loop() {
  int valor = analogRead(34);  // GPIO 34 o el pin que uses
  Serial.println(valor);
  delay(100);  // cada 100 ms
}
