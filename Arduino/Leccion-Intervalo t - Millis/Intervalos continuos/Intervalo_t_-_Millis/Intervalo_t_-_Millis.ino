
const int ledPin =  LED_BUILTIN;
int ledState = LOW;             
unsigned long previousMillis = 0;       
const long interval = 1000;           
unsigned long currentMillis;
void setup() {
  
  pinMode(ledPin, OUTPUT);
}

void loop() {
  
  currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {    
    previousMillis = currentMillis;   
    if (ledState == LOW) {
      ledState = HIGH;
    } else {
      ledState = LOW;
    }    
    digitalWrite(ledPin, ledState);
  }
}

