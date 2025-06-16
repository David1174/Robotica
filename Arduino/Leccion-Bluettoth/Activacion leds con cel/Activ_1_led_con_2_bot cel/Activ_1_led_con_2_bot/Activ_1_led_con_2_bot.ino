
int ledPin = 13; 
int state = 0; 
 
void setup() {
    Serial.begin(9600);
    pinMode(ledPin, OUTPUT);   
    digitalWrite(ledPin, LOW);  
}
 
void loop() {
  if(Serial.available() > 0){
     state = Serial.read();
     if (state == 'N') {
        digitalWrite(ledPin, LOW);   
     }

     if (state == 'S') {
        digitalWrite(ledPin, HIGH);    
     }
  }
}



