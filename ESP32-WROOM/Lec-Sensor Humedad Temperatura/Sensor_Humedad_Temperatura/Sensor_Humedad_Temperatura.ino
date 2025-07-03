#include "DHT.h"

#define DHTPIN 4       // Pin GPIO donde está conectado el DATA del DHT
#define DHTTYPE DHT11  // Usa DHT22 si usás el otro modelo

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature(); // Celsius

  if (isnan(h) || isnan(t)) {
    Serial.println("Fallo en la lectura del sensor");
    return;
  }

  Serial.print("Humedad: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.println(" °C");

  delay(2000);
}
