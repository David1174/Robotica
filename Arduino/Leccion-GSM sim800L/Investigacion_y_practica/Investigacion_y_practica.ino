#include <SoftwareSerial.h> //Incluir Libreria SoftwareSerial

SoftwareSerial MOD_SIM800L(8, 9); // pines del arduino uno D8 y D9  (TX, RX Del Módulo SIM800l)

int led=3;

void setup(){
  Serial.begin(9600);
  MOD_SIM800L.begin(9600);
  pinMode(led,OUTPUT);
}

void loop(){
  /* Se obtiene el número de bytes (caracteres) disponibles para su
  lectura desde el puerto serie. */
  while (MOD_SIM800L.available()){
    digitalWrite(led,1);
    Serial.write(MOD_SIM800L.read());
  }
  //delay(3000);
  digitalWrite(led,0);

  MOD_SIM800L.println("ATD+543484687704;");

  delay(10000);

  MOD_SIM800L.println("ATH");
  delay(1000);


} //fin Loop


void EnviaSMS(){              
  MOD_SIM800L.println("AT+CMGF=1");              // Activamos la funcion de envio de SMS
  delay(100);                                    // Pequeña pausa
  MOD_SIM800L.println("AT+CMGS=\"+543484687704\"");  // Definimos el numero del destinatario en formato internacional
  delay(100);                                    // Pequeña pausa
  MOD_SIM800L.print("Hola Mundo!");                 // Definimos el cuerpo del mensaje
  delay(500);                                    // Pequeña pausa
  MOD_SIM800L.print(char(26));                      // Enviamos el equivalente a Control+Z 
  delay(100);                                    // Pequeña pausa
  MOD_SIM800L.println("");                          // Enviamos un fin de linea
  delay(100);                                    // Pequeña pausa
}


