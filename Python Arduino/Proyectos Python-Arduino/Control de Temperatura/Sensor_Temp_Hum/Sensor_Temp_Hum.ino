#include <DHT.h>
 
// Definimos el pin digital donde se conecta el sensor
#define DHTPIN 2
#define Motor 3
#define LED 13
// Dependiendo del tipo de sensor
#define DHTTYPE DHT11
 
// Inicializamos el sensor DHT11
DHT dht(DHTPIN, DHTTYPE);
 
void setup() {
  // Inicializamos comunicación serie
  Serial.begin(9600);
  pinMode(Motor, OUTPUT);
  // Comenzamos el sensor DHT
  dht.begin(); 
}
 
void loop() {
  
  // Verificar si hay datos disponibles desde la serial
  if (Serial.available()) {
     char comando = Serial.read();  // Leer el comando

     // Encender el LED si se recibe 'H'
     if (comando == 'H') {
        digitalWrite(Motor, HIGH);
     }

     // Apagar el LED si se recibe 'L'
     if (comando == 'L') {
        digitalWrite(Motor, LOW);
     }
  }  
  
  // Esperamos 2 segundos entre medidas
  delay(2000);
 
  // Leemos la humedad relativa
  float h = dht.readHumidity();
  // Leemos la temperatura en grados centígrados (por defecto)
  float t = dht.readTemperature();  

  if(t>30){
    digitalWrite(LED, HIGH);
  }
 
  // Comprobamos si ha habido algún error en la lectura
  if (isnan(h) || isnan(t) /*|| isnan(f)*/) {
    Serial.println("Error obteniendo los datos del sensor DHT11");
    return;
  }
  
  Serial.print("Temp: ");
  Serial.print(t);
  Serial.print(" *C\t");
  Serial.print("Hum: ");
  Serial.print(h);
  Serial.println(" *%"); 
}
