void setup() {
  Serial.begin(9600); // Configura la comunicación serie
  pinMode(10,OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); // Lee el comando
    //Serial.println(command);
    int separator = command.indexOf(','); 
    
    if (separator > 0) {
      int pin = command.substring(0, separator).toInt(); // Número del pin
      String action = command.substring(separator+1);  // Acción (ON/OFF)
      Serial.println(action);
      pinMode(pin, OUTPUT);
      if (pin==8) {
        digitalWrite(pin, HIGH); 
        delay(1000);
        digitalWrite(pin,0);
        delay(1000);
        digitalWrite(pin, HIGH); 
        delay(1000);
        digitalWrite(pin,0);
        delay(1000);
      }
      Serial.println(action);

      if (action == "ON") {
        digitalWrite(pin, HIGH); // Enciende el pin
        digitalWrite(10, 0); // Enciende el p
        delay(2000);
      } else if (action == "OFF") {
        digitalWrite(pin, LOW); // Apaga el pin
      }
    }
  }
}
