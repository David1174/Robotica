int led =13;
int dato = 0;

void setup() {
   pinMode(led, OUTPUT);
   digitalWrite(led,LOW);
   Serial.begin(9600);
}

void loop() {
   if(Serial.available()>0) {
     dato = Serial.read();
   }

   if (dato == '0') {
     digitalWrite(led,LOW);
   }

   if (dato == '1') {
     digitalWrite(led,HIGH);
   }
}



