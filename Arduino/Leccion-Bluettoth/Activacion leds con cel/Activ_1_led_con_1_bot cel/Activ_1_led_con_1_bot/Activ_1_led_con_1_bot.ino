 
int led_rojo = 3; 
int led_amarillo = 4;
int led_verde = 5;
int senial_r=1;
int senial_a=1;
int senial_v=1;
int Power=2;
 
void setup() {
    Serial.begin(9600);
    pinMode(led_rojo, OUTPUT); 
    pinMode(led_amarillo, OUTPUT);
    pinMode(led_verde, OUTPUT);  
     
    pinMode(Power,OUTPUT);
    digitalWrite(Power,1); 
    
} 

void loop() { 
  if(Serial.available() > 0){ //Inicia Si principal
     char state;
     state = Serial.read();
     
     if (state == 'R' || state == 'r') { // Led rojo
        digitalWrite(led_amarillo,LOW);senial_a=1;
        digitalWrite(led_verde,LOW);senial_v=1;
        
        if(senial_r==1) {        
           digitalWrite(led_rojo, HIGH); 
           senial_r=0;   
        }
        else {
           digitalWrite(led_rojo,LOW ); 
           senial_r=1;    
        }         
     } // Fin Si Led rojo


     if (state == 'A' || state == 'a') { // Led amarillo
        digitalWrite(led_rojo,LOW);senial_r=1;
        digitalWrite(led_verde,LOW);senial_v=1;
        if(senial_a==1) {        
           digitalWrite(led_amarillo, HIGH); 
           senial_a=0;   
        }
        else {
           digitalWrite(led_amarillo,LOW ); 
           senial_a=1;    
        }         
      } // Fin Si Led amarillo

      if (state == 'V' || state == 'v') { // Led verde
         digitalWrite(led_rojo,LOW);senial_r=1;
         digitalWrite(led_amarillo,LOW);senial_a=1; 
         if(senial_v==1) {        
           digitalWrite(led_verde, HIGH); 
           senial_v=0;   
         }
         else {
           digitalWrite(led_verde,LOW ); 
           senial_v=1;    
         }         
      } // Fin Si Led verde

      if (state == 'T' || state == 't') { // Automatico
         state='N';
         digitalWrite(led_rojo,0);digitalWrite(led_amarillo,0);digitalWrite(led_verde,0);
         delay(1000);
         do {          
           digitalWrite(led_rojo,1); delay(1000);
           digitalWrite(led_rojo,0); //delay(500);
           digitalWrite(led_amarillo,1); delay(500);
           digitalWrite(led_amarillo,0); //delay(500);
           digitalWrite(led_verde,1); delay(1000);
           digitalWrite(led_verde,0); //delay(500);
           state=Serial.read();    
         }while(state!='T');   
         digitalWrite(led_rojo,0);digitalWrite(led_amarillo,0);digitalWrite(led_verde,0);   
      } // Fin Si automatico


     
  } // Fin Si principal  
} // Fin loop
