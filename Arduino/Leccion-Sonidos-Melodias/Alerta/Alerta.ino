int sonido = 9;

void setup()
{
  pinMode(sonido,OUTPUT);
}

void loop()
{
  tone(sonido,900,250); 

  tone(sonido,200,250);
  //delay(200);
  //noTone(sonido);
}

