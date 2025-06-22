
const int pinecho = 8;
const int pintrigger = 9;
const int pinled = 13;
 long tiempo, distancia;
 
void setup() {
  Serial.begin(9600);
  pinMode(pinecho, INPUT);
  pinMode(pintrigger, OUTPUT);
  pinMode(13, OUTPUT);
}
 
void loop() {
  digitalWrite(pintrigger, LOW);
  delayMicroseconds(2);
  digitalWrite(pintrigger, HIGH); 
  delayMicroseconds(10);
 
  tiempo = pulseIn(pinecho, HIGH); 
  distancia = tiempo / 58;
  Serial.print(distancia);
  Serial.println(" cm");
  delay(200);
}
