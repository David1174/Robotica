
// Definir los pines de los LEDs en un array
const int motor=11;
const int ventilador=12;
const int luz=13;
const int numLeds = 3;           // Número de LEDs
const int delayTiempo = 200;      //  ms para cada paso

int rep=0;

void setup() {
  //Configurar cada pin como salida
  pinMode(motor,OUTPUT);
  pinMode(ventilador,OUTPUT);  
  pinMode(luz, OUTPUT);
  //Inicializar la comunicación serie a 9600 baudios
  Serial.begin(9600);
}

void loop() {
  // Verificar si hay datos disponibles en el puerto serie
  if (Serial.available() > 0) {
     // Leer el byte recibido
     char comando = Serial.read();
     //Serial.print(comando);    
     if (comando == '1') {    
        digitalWrite(motor,1);
     }
     if (comando == '0') {    
        digitalWrite(motor,0);
     }
     if (comando == '2') {    
        digitalWrite(ventilador,1);
     }
     if (comando == '0') {    
        digitalWrite(ventilador,0);
     }
     
  }
}
