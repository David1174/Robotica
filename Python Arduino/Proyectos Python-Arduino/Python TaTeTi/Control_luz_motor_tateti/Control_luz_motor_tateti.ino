
// Definir los pines de los LEDs en un array
const int leds[] = {11, 12, 13};  // Pines de los LEDs
const int numLeds = 3;           // Número de LEDs
const int delayTiempo = 200;      //  ms para cada paso

int rep=0;

void setup() {
  //Configurar cada pin como salida
  for (int i = 0; i < numLeds; i++) {
     pinMode(leds[i], OUTPUT);
  }
  //Inicializar la comunicación serie a 9600 baudios
  Serial.begin(9600);
}

void loop() {
  // Verificar si hay datos disponibles en el puerto serie
  if (Serial.available() > 0) {
    // Leer el byte recibido
    char comando = Serial.read();
    Serial.print(comando);
    // Encender o apagar el LED según el comando recibido
    if (comando == '1') {
    
      for (rep = 0; rep < 4; rep++) {    
         // Encender los LEDs de uno en uno
         for (int i = 0; i < numLeds; i++) {
            // Apagar todos los LEDs antes de encender uno
            for (int j = 0; j < numLeds; j++) {
               digitalWrite(leds[j], LOW);
            }
            // Encender el LED actual
            digitalWrite(leds[i], HIGH);
            delay(delayTiempo);  // Esperar 500 ms
         }

         // Encender todos los LEDs a la vez
         for (int i = 0; i < numLeds; i++) {
            digitalWrite(leds[i], HIGH);
         }
         delay(delayTiempo);  // Esperar 500 ms

         // Apagar todos los LEDs
         for (int i = 0; i < numLeds; i++) {
            digitalWrite(leds[i], LOW);
         }
         delay(delayTiempo);  // Esperar 500 ms
      }
          
    } 
  }
}
