#include <Servo.h>

int angulo;
int potenciometro;
int pinServo = 9;

Servo myServo;                        // crea el objeto servomotor

void setup(){
  Serial.begin(9600);
   myServo.attach(pinServo);                // asigna el pin 8 al servo
}

void loop(){

 if(analogRead(A0)){
   potenciometro=analogRead(A0);   // lee la señal del potenciómetro
   angulo=map(potenciometro, 0, 1023, 0, 180); // mapea la señal de 0 a 179
   myServo.write(angulo);          // mueve el servomotor
   //delay(15);
   Serial.println(angulo);
 }
}
