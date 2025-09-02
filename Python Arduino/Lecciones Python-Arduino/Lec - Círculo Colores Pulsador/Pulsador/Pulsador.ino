const int boton = 3;

void setup() {
  pinMode(boton, INPUT_PULLUP);  // Pulsador con resistencia interna
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(boton) == LOW) {  
    // Botón presionado (activo en LOW)
    Serial.println("PRESION");
    delay(300); // Anti-rebote
  }
}

