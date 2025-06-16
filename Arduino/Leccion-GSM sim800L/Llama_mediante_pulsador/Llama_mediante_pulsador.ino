#include <SoftwareSerial.h> //Incluir Libreria SoftwareSerial

SoftwareSerial MOD_SIM800L(8, 9); // pines del arduino uno D8 y D9  (TX, RX Del Módulo SIM800l)

int pulsad=3;
int led=13;

void setup(){
  Serial.begin(9600);
  MOD_SIM800L.begin(9600);
  pinMode(led,OUTPUT);
  pinMode(pulsad,INPUT);
}

void loop(){
  
 if(digitalRead(pulsad)) {  
   digitalWrite(led,1);
   MOD_SIM800L.println("ATD+543484687704;");
   delay(10000);
   digitalWrite(led,0);
   MOD_SIM800L.println("ATH");
   delay(1000);   
 }

} //fin Loop





