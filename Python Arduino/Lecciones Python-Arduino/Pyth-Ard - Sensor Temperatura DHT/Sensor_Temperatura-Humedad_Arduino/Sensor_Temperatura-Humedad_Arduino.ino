#include <DHT.h>
 
// Definimos el pin digital donde se conecta el sensor
#define DHTPIN 2
// Dependiendo del tipo de sensor
#define DHTTYPE DHT11
 
// Inicializamos el sensor DHT11
DHT dht(DHTPIN, DHTTYPE);
 
void setup() {
  // Inicializamos comunicación serie
  Serial.begin(9600);
 
  // Comenzamos el sensor DHT
  dht.begin(); 
}
 
void loop() {
  // Esperamos 5 segundos entre medidas
  delay(1000);
 
  // Leemos la humedad relativa
  float h = dht.readHumidity();
  // Leemos la temperatura en grados centígrados (por defecto)
  float t = dht.readTemperature();  
 
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
