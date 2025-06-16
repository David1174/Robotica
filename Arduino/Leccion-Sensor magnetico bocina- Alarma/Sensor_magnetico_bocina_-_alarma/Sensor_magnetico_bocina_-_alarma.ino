
int led=10;
int SenMag=7;
int pinTono=9;

void setup() {
  pinMode(led,OUTPUT);  
  pinMode(SenMag,INPUT);
}

void loop()
{
  bool valor = digitalRead (SenMag) ;
  digitalWrite( led, !valor) ;
  if (valor) {
    tone(pinTono,250);
    delay(4000);
    noTone(pinTono);
  }
}




