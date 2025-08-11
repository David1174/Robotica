#define LED_PIN 18

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();

    if (comando == "ON") {
      digitalWrite(LED_PIN, HIGH);
    } 
    else if (comando == "OFF") {
      digitalWrite(LED_PIN, LOW);
    }
  }
}

