#include <SoftwareSerial.h>    // Incluimos la libreria SoftwareSerial

SoftwareSerial MOD_SIM800L(8,9); // (8,9)Declaramos los pines RX(8) y TX(9)  que vamos a usar
 
void setup(){
Serial.begin(9600);         // Iniciamos la comunicacion serie
MOD_SIM800L.begin(9600);    // Iniciamos una segunda comunicacion serie
delay(1000);                // Pausa de 1 segundo
Llamar();                   // Llamada a la funcion que envia el SMS
}
 
void loop(){}
 
// Funcion para llamada a celular
void Llamar(){             
  MOD_SIM800L.println("ATD+543484687704;");
  delay(17000);
  MOD_SIM800L.println("ATH");
  delay(4000);   
}
