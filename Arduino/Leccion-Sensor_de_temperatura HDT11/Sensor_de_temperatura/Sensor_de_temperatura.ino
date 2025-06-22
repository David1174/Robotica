#include <DHT.h>

DHT dht(10, DHT11); // O DHT22 según el sensor que usemos.

void setup()
{
  Serial.begin(9600); 
  Serial.println("Prueba DHT11:");
  dht.begin();
}

void loop()
{
  // Se lee la humedad y la temperatura del sensor:
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // Si los valores leídos no son números se advierte de ello, de lo contrario se imprimen los resultados:
  if(isnan(t) || isnan(h))
  {
    Serial.println("Fallo de lectura del DHT");
  }
  else
  {
    Serial.print("Humedad: ");     Serial.print(h); Serial.print(" %\t");
    Serial.print("Temperatura: "); Serial.print(t); Serial.print(" *C\n");
  }
  delay(1000);
}
