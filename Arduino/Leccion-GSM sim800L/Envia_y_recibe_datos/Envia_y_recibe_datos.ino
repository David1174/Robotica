#include <SoftwareSerial.h> //Incluir Libreria SoftwareSerial
SoftwareSerial MOD_SIM800L(8, 9); // pines del arduino uno D8 y D9
 //(RX, TX Del Módulo SIM800l)
int led=3;

void setup(){
  Serial.begin(9600);
  MOD_SIM800L.begin(9600);
  pinMode(led,OUTPUT);
}
void loop(){
/* Se obtiene el número de bytes (caracteres) disponibles para su
lectura desde el puerto serie. */
if (MOD_SIM800L.available()){
  digitalWrite(led,1);
  delay(1000);
  Serial.write(MOD_SIM800L.read());
}

digitalWrite(led,0);
delay(200);

if (Serial.available()){
  while(Serial.available()) {
    MOD_SIM800L.write(Serial.read());
  }
  MOD_SIM800L.println();
}

}

