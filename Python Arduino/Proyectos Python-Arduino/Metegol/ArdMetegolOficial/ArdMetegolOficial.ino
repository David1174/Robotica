const int sensorGolEquipo1 = 2;  // Sensor del Equipo 1
const int sensorGolEquipo2 = 3;  // Sensor del Equipo 2

void setup() {
  Serial.begin(9600);  // Inicializa la comunicación serial
  pinMode(sensorGolEquipo1, INPUT);
  pinMode(sensorGolEquipo2, INPUT);
}

void loop() {
  if (digitalRead(sensorGolEquipo1) == LOW) {
    Serial.println("Gol Equipo 1");
    delay(400);  // Evita lecturas múltiples
  }

  if (digitalRead(sensorGolEquipo2) == LOW) {
    Serial.println("Gol Equipo 2");
    delay(400);
  }
}
