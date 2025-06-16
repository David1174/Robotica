int valorLDR = 0;   
int pinLDR = A0;    

void setup() { 
  Serial.begin(9600); 
}

void loop() { 
  valorLDR = analogRead(pinLDR); 
  Serial.println(valorLDR);       
  delay(100);   
}
