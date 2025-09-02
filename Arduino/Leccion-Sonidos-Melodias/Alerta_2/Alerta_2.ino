int sonido = 9;

void setup()
{
  pinMode(sonido,OUTPUT);
}

void loop()
{
  tone(sonido,500); //1. do,  Que 
  delay(200);
  noTone(sonido);
 
  tone(sonido,900); //1. do,  Que 
  delay(200);
  noTone(sonido);
}

