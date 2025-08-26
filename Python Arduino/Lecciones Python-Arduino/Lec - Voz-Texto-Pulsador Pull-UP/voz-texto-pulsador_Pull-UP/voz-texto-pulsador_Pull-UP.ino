const int buttonPin = 2; // Pin al que está conectado el pulsador

void setup() {
  pinMode(buttonPin, INPUT);
  Serial.begin(9600); // Inicia la comunicación serial
}

void loop() {  
   if (!digitalRead(buttonPin)){    
        delay(350);
        Serial.println("Activar voz"); // Envía mensaje al presionar el pulsador
   } 
     
}
