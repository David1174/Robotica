#define POT A0

int ValorPot;

void setup(){
  Serial.begin(9600);
  pinMode (POT,INPUT);
}

void loop(){
  ValorPot= analogRead(POT);
  Serial.println(ValorPot);
  delay(500);
}
