
const int ledPin =  LED_BUILTIN;            
unsigned long prevMillis = 0;       
const long interval = 4000;           
unsigned long varMillis;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  temp();
  
}

void loop() {}  

// procedimiento  //
void temp() {  
  digitalWrite(ledPin,1);
  prevMillis=millis();
  do {    
     varMillis = millis();
  }while (varMillis - prevMillis <= interval);
  digitalWrite(ledPin,0);  
}
