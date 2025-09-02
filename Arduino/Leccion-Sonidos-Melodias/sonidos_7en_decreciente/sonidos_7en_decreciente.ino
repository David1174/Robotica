
int f=500;
int sonido=9;
int t=200;
 
void setup(){
 pinMode (sonido, OUTPUT); //pin configurado como salida
}
 
void loop(){
  
  for (int i=7;i>0; i--){
      tone(sonido, f);
      delay(t);
      noTone(sonido);
      f=f-35;
  }
  f=500;
 }