#include "DHT.h"

#define DHTPIN 4          // Pin conectado al sensor DHT
#define DHTTYPE DHT11     // Cambia a DHT11 si usás ese modelo

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  float humedad = dht.readHumidity();
  float temperatura = dht.readTemperature();  // En °C

  // Validar si la lectura fue exitosa
  if (isnan(humedad) || isnan(temperatura)) {
    Serial.println("Error leyendo el sensor DHT");
    delay(2000);
    return;
  }

  // Enviar los datos en formato compatible con Python
  Serial.print("HUMEDAD:");
  Serial.print(humedad, 1);  // un decimal
  Serial.print(",TEMP:");
  Serial.println(temperatura, 1);  // un decimal

  delay(1000);  // Esperar 1 segundo
}

