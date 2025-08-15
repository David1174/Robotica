volatile bool golpe = false;

void isrRuido() {  // flanco de bajada: LM393 suele “tirar a GND” al disparar
  golpe = true;
}

void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT);           // DO en D2
  attachInterrupt(digitalPinToInterrupt(2), isrRuido, FALLING);
}

void loop() {


  // Evento de golpe/ruido
  if (golpe) {
    Serial.print("  |  DO: DISPARO");
    golpe = false;
  }
  Serial.println();
  delay(20);
}
