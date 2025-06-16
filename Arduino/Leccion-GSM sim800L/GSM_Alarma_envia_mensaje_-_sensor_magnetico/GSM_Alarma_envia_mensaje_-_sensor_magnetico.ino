#include <SoftwareSerial.h> 
SoftwareSerial MOD_SIM800L(8, 9);  //(RX, TX Del Módulo SIM800l)

int led = 3;
int SenMag = 7;
int Sirena = 12;
int senial = 0;
char key;
int activar;
boolean Magnetic;
unsigned long interval; 
unsigned long previousMillis = 0;
unsigned long currentMillis;

int aux1 = 5;

char clave[6] = {"tartus"};

void setup() {
  Serial.begin(9600);
  MOD_SIM800L.begin(9600);
  pinMode(SenMag,INPUT);
  pinMode(Sirena,OUTPUT);
  pinMode(led,OUTPUT);

  pinMode(aux1,OUTPUT);
}

void loop() {  
 do {    
   key = Serial.read();
   switch(key) {
   case '1':
     if (!ControlMagnetic()) {
       ActivAlarm();
     } else {
       NegativTone();         
     }     
     break;  
      
   case '2':
     //digitalWrite(aux1,0);
     break;   
   } // Fin estructura de casos   
 } while (key!='9');  
 key = '*'; 
  
} //fin Loop


// ----------- Funciones y Procedimientos  ----------- //


void NegativTone() {
  tone(Sirena,250);
  delay(300);
  noTone(Sirena);
}


boolean ControlMagnetic() {
  if (digitalRead(SenMag)==0) {
    Magnetic = false;    
  } else {
    Magnetic =true;
  }
  return Magnetic;
}

void ActivAlarm() { 
  digitalWrite(aux1,1); 
  do {  
    key = Serial.read();
    if (digitalRead(SenMag)==1 && senial==0) {
      DisparoAlarm();  
    }    
  } while(key!='9' && senial == 0);
  digitalWrite(aux1,0);
  key = '9';
  senial = 0;  
}

void DisparoAlarm() {
    digitalWrite( led, 1) ;  
    tone(Sirena,250);  
    //EnviaSMS_Linfa();      
    //LlamaSergio();  // a procedimiento   
    //EnviaSMS_Sergio();
    //LlamaLinfa();
    senial=1;    
    interval=millis()+4000;
    while ( currentMillis <= interval && key!='9') {       
       currentMillis = millis();       
       key=Serial.read();  
    } 
    digitalWrite (led,0);
    noTone(Sirena); 
}

void LlamaSergio() {
  MOD_SIM800L.println("ATD+543484687704;");
  delay(15000);
  MOD_SIM800L.println("ATH");
  delay(4000);
}

void LlamaLinfa() {  
  MOD_SIM800L.println("ATD+543484355863;");
  delay(15000);
  MOD_SIM800L.println("ATH");
  delay(4000);
}

void EnviaSMS_Sergio(){              
  MOD_SIM800L.println("AT+CMGF=1");                 // Activamos la funcion de envio de SMS
  delay(500);                                       // Pequeña pausa
  MOD_SIM800L.println("AT+CMGS=\"+543484687704\""); // Definimos el numero del destinatario en formato internacional
  delay(500);                                       // Pequeña pausa
  MOD_SIM800L.print("Alarma Activada!");            // Definimos el cuerpo del mensaje
  delay(500);                                       // Pequeña pausa
  MOD_SIM800L.print(char(26));                      // Enviamos el equivalente a Control+Z 
  delay(1000);                                      // Pequeña pausa
  MOD_SIM800L.println("");                          // Enviamos un fin de linea
  delay(3000);                                      // Pequeña pausa
}

void EnviaSMS_Linfa(){              
  MOD_SIM800L.println("AT+CMGF=1");                 // Activamos la funcion de envio de SMS
  delay(500);                                       // Pequeña pausa
  MOD_SIM800L.println("AT+CMGS=\"+543484355863\"");  // Definimos el numero del destinatario en formato internacional
  delay(500);                                       // Pequeña pausa
  MOD_SIM800L.print("Alarma Activada");                 // Definimos el cuerpo del mensaje
  delay(500);                                       // Pequeña pausa
  MOD_SIM800L.print(char(26));                      // Enviamos el equivalente a Control+Z 
  delay(1000);                                      // Pequeña pausa
  MOD_SIM800L.println("");                          // Enviamos un fin de linea
  delay(3000);                                    // Pequeña pausa
}




