#include <Servo.h>
int pul1=3;
int pul2=4;
int grados=90;
int pinServo=9;
Servo servo;

void setup() {
  pinMode(pul1,INPUT);
  pinMode(pul2,INPUT);
  servo.attach(pinServo);
  servo.write(grados);
}

void loop() {
  if(digitalRead(pul1)){
    if(grados<=180){
       grados=grados+1;
       servo.write(grados);
       delay(5);       
    }   
  } else {
    if(digitalRead(pul2)) {
       if(grados>0) {
          grados=grados-1;
          servo.write(grados);
          delay(5);  
       }        
    }               
  }
}
