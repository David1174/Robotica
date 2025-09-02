const int LedPin1 = 10;
const int LedPin2 = 9;

void setup()
 {
  Serial.begin(9600);
  pinMode(LedPin1,OUTPUT);
  pinMode(LedPin2,OUTPUT);
 }

 void loop() {
   byte dato;
   char* mensaje;
   if (Serial.available()) {
     dato=Serial.read();
     switch(dato)  {
      
       case 'a':           
           digitalWrite(LedPin1, HIGH);
           mensaje="Avanzar";               
       break;
         
       case 'd': 
           digitalWrite(LedPin2, HIGH);
           mensaje="Retrocede";                         
       break;    

       case 'z': 
           apaga();           
           mensaje="Apagado";                         
       break;    
             
     } // cierra la estructura de casos     
     Serial.println(mensaje);
   }// cierra if Serial.available   
 }// cierra loop
 
void apaga() {
   digitalWrite(LedPin1, LOW);
   digitalWrite(LedPin2, LOW);
}

