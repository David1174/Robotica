int pinaltavoz = 7;
int frecuencia;     // frecuencia correspondiente
int contador;       // variable para el contador
float m=1.059;      // constante para multiplicar frecuencias

void setup()
{
  pinMode(pinaltavoz,OUTPUT);
  
}

void loop(){
  for(contador=0,frecuencia=1000;contador<20;contador++)
    {
        frecuencia=frecuencia*m;     // actualiza la frecuencia
        tone(pinaltavoz,frecuencia); // emite el tono
        delay(70);                   // Pausa a elegir
        noTone(pinaltavoz);          // Detiene el tono
    }
}
