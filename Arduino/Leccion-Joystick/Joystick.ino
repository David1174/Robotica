const int pinJoyX = A0;
const int pinJoyY = A1;

void setup() {
   Serial.begin(9600);
}

void loop() {
  int Xvalue = 0;
  int Yvalue = 0;
  Xvalue = analogRead(pinJoyX); //delay(200); 
  Yvalue = analogRead(pinJoyY); //delay(200);
  Serial.print("X:" );
  Serial.print(Xvalue);
  Serial.print(" | Y: ");
  Serial.print(Yvalue); //delay(500);
  Serial.println();
}
