const int led1=11;  // Pin donde está conectado el LED
const int led2=12;
const int motor=13;


void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(motor, OUTPUT);
  Serial.begin(9600);  // Iniciar la comunicación serial
}

void loop() {
  if (Serial.available() > 0) {
    //String command = Serial.readStringUntil('\n');  // Leer el comando desde el puerto serial
    //command.trim();  // Eliminar espacios en blanco
    char command = Serial.read();
    
    if (command == '1') {
      digitalWrite(led1, 1);  // Encender el LED
    } 
    if (command == '4') {
      digitalWrite(led1, 0);  // Encender el LED
    } 
    
    if (command == '2') {
      digitalWrite(led2, 1);   // Apagar el LED
    }
    if (command == '5') {
      digitalWrite(led2, 0);   // Apagar el LED
    }
    
    if (command == '3') {
      digitalWrite(motor, 1);   // Apagar el LED
    }
    if (command == '6') {
      digitalWrite(motor, 0);   // Apagar el LED
    }
    if (command == '7') {
       digitalWrite(led1, 1);
       digitalWrite(led2, 1);
       digitalWrite(motor, 1);
    }

    if (command == '8') {
      digitalWrite(led1,0);
      digitalWrite(led2,0);
      digitalWrite(motor,0);
    }
  }
}
