#include <SoftwareSerial.h>

SoftwareSerial mySerial(19, 18); // 10 11 - RX, TX
int val;
int pot=A0;

void setup() {  
  mySerial.begin(9600);
  Serial.begin(9600);

}

void loop() { 
  val=analogRead(pot);
  val = map(val, 0, 1023, 35, 200); 
  Serial.println(val);
  mySerial.write(val); 
  delay(20);
}


