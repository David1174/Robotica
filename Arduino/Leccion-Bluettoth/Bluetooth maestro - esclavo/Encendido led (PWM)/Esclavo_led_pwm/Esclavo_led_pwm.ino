int led =13;
int dato = 0;
int Power5v=2;

void setup() {
   pinMode(Power5v,OUTPUT);
   digitalWrite(Power5v,HIGH);
   pinMode(led, OUTPUT);
   Serial.begin(9600);
}

void loop() {
   if(Serial.available()>0) {
      dato = Serial.read();      
      Serial.println(dato);
      analogWrite(led,dato);// 
   }
}
