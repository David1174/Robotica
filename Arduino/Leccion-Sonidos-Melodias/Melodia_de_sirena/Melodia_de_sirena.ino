int duracion=250; //Duración del sonido
int fMin=2000; //Frecuencia más baja que queremos emitir
int fMax=4000; //Frecuencia más alta que queremos emitir
int i=0;
int sir=9; 
void setup(){
 pinMode (sir, OUTPUT); //pin configurado como salida
}
 
void loop(){
  //sonido más agudo
  for (i=fMin;i<=fMax; i=i+2)
     tone(sir, i, duracion);    
  //sonido más grave
  for (i=fMax;i>=fMin; i=i-4)
    tone(sir, i, duracion);   
}
