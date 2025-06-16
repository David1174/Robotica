#include <Servo.h>

Servo myservo;  

int pinServo = 9;
float pos = 0;    

void setup() {
  myservo.attach(pinServo);  
}


void loop() {
  for (pos = 8; pos <= 180; pos += 1) { 
    myservo.write(pos);              
    delay(5);                     
  }
  
  for (pos = 180; pos >= 8; pos -= 1) { 
    myservo.write(pos);              
    delay(5);                       
  }
  delay(600);
}
