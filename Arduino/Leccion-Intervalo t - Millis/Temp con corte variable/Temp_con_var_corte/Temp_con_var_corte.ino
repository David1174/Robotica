
const int ledPin =  LED_BUILTIN;            
unsigned long prevMillis = 0;                
unsigned long varMillis;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);  
}

void loop() {  
  digitalWrite(ledPin,1);
  temporiz(1000);
  digitalWrite(ledPin,0);
  temporiz(1000);
}  

// procedimiento  //

void temporiz(unsigned long interval) {  
  char vchar;
  prevMillis=millis();
  do {  
     vchar=Serial.read();  
     varMillis = millis();
  }while (varMillis - prevMillis <= interval && vchar!='*'); 
}
