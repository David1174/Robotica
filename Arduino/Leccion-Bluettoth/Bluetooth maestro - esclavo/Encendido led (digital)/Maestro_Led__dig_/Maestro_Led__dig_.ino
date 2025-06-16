#include <SoftwareSerial.h>

SoftwareSerial mySerial(19, 18); // 10 11 - RX, TX

void setup() {  
  mySerial.begin(9600);
  Serial.begin(9600);
}

void loop() { 
  
  mySerial.write(Serial.read()); 
  
}


