const int motor =10;  // led conectado al pin 3
const int pot =0; // el pot esta conectado al pin A0

int control;  //variable para el brillo

void setup ()  {
  pinMode (motor, OUTPUT);  // declaramos el led como salida 
  
}

void loop (){
  
  control = analogRead (pot) / 4; 
  
  analogWrite(motor, control);
  
}
