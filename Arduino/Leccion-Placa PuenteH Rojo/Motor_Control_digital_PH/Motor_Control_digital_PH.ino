int M1a=8; 
int M1b=9;
int state = 0; 
int senial;
int Power=2;
 
void setup() {
    Serial.begin(9600);
    pinMode(M1a, OUTPUT);   
    pinMode(M1b, OUTPUT); 
    pinMode(Power,OUTPUT);
    digitalWrite(Power,1); 
    senial=1;
} 

void loop() {
  if(Serial.available() > 0){
     state = Serial.read();
     if (state == 'A' || state == 'a') {
        digitalWrite(M1b, LOW);
        digitalWrite(M1a, HIGH); 
     }
     if (state == 'B' || state == 'b') {
        digitalWrite(M1a,LOW);
        digitalWrite(M1b, HIGH);
     }  
  } 
}
