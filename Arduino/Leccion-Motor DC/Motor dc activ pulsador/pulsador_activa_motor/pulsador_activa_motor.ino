
int motor=10;
int pulsad=7;

void setup() {
  pinMode(motor,OUTPUT);  
  pinMode(pulsad,INPUT);
}

void loop(){
  bool valor = digitalRead (pulsad) ;
  digitalWrite( motor, valor) ;
}
