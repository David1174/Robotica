int ledPin = 13; 
int state = 0; 
int senial;
int Power=2;
 
void setup() {
    Serial.begin(9600);
    pinMode(ledPin, OUTPUT);   
    digitalWrite(ledPin, LOW); 
    pinMode(Power,OUTPUT);
    digitalWrite(Power,1); 
    senial=1;
} 

void loop() {
  if(Serial.available() > 0){
     statecel = Serial.read();
     if (statecel == 'A' || statecel == 'a') {
        if(senial==1) {        
           digitalWrite(ledPin, HIGH); 
           Serial.println("Activo");
           senial=0;   
        }
        else {
           digitalWrite(ledPin,LOW ); 
           Serial.println("Apagado");
           senial=1;    
        }         
     }
  }
}
