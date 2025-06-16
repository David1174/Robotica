// Programa de control de Servo

#include <Servo.h>

int pinServo = 9;    //Pin a conectar el servo

Servo servo;   //Se crea un nuevo objeto del servo

void setup() {
  servo.attach(pinServo); //Inicializamos el servo con el pin declarado
}

void loop() {
  servo.write(10);
  delay(2000);
  servo.write(160);
  delay(2000);
}
