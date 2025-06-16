#include <Servo.h>

Servo myservo; 

int pinServo = 9;
float pos = 0;    

void setup() {
  Serial.begin(9600);
  myservo.attach(pinServo);  
}

void loop() {
  while (pos < 160) { 
    pos=pos+1;   
    myservo.write(pos);  
    delay(3);                       
  }
  delay(1000);
  
  while (pos > 50) { 
    pos=pos-1;   
    myservo.write(pos);              
    delay(3);                      
  }
  delay(1000);
  
}
