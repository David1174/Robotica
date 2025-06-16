 const int LedPin = 13;
const int LedPin2=11;

int sen1=1;
int sen2=1;


void setup()
 {
  Serial.begin(9600);
  pinMode(LedPin, OUTPUT);
  pinMode(LedPin2,OUTPUT);
 
 }

 void loop() {
   char dato;
   char* mensaje;
   
   if (Serial.available()) {
    
     dato=Serial.read();
     switch(dato) {
      
       case '1': 
         if(sen1==1) 
         {
           digitalWrite(LedPin, HIGH);
           mensaje="Avanzar";
           sen1=0;
         }  
         else
         {
           digitalWrite(LedPin, LOW);
           mensaje="Stop";
           sen1=1;
         }  
         break;
         
       case '2': 
         if(sen2==1) 
         {
           digitalWrite(LedPin2, HIGH);
           mensaje="Retrocede";
           sen2=0;
         }  
         else
         {
           digitalWrite(LedPin2, LOW);
           mensaje="Stop";
           sen2=1;
         }                  
         break; 
                 
     } // cierra la estructura de casos
     
     Serial.println(mensaje);
   }// cierra if Serial.available
   
 }// cierra loop
 

