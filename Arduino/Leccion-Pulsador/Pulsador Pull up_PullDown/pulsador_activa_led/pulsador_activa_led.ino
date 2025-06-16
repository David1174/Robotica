int led=13;
int pulsad=3;

void setup() {
  Serial.begin(9600);
  pinMode(led,OUTPUT);  
  pinMode(pulsad,INPUT);
}

void loop()
{

   bool valor = digitalRead (pulsad) ;  
   digitalWrite( led, valor) ;
}
