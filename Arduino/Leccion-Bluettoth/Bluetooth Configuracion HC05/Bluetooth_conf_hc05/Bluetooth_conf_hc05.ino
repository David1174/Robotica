#include <SoftwareSerial.h>


SoftwareSerial mySerial(10, 11); // RX(10), TX(11)

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  mySerial.begin(38400);//38400 para HC-05(6 terminales)
  Serial.println("Configuracion");
 
  mySerial.println("Hello, world?");
}

void loop() { // run over and over
  if (mySerial.available()) {
    Serial.write(mySerial.read());
  }
  if (Serial.available()) {
    mySerial.write(Serial.read());
  }
}
