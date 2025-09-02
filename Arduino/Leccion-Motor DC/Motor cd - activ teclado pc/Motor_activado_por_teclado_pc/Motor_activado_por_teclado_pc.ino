int motor=8;

void setup() {
  Serial.begin(9600);
  pinMode(motor,OUTPUT);
  Serial.println("a: Activar Motor");
  Serial.println("d: Desactivar Motor");
  Serial.println();
}

void loop() {
  char boton = Serial.read();  
  if (boton=='a') {
    digitalWrite(motor,1);
    Serial.println("Motor Activado");
  }  
  if (boton=='d') {
    digitalWrite(motor,0);
    Serial.println("Motor Desactivado");
  }  
}


