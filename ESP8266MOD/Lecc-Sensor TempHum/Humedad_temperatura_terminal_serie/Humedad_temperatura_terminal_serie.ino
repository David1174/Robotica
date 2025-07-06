#include <DHT.h>

// Configuración del sensor
#define DHTPIN D2          // Pin de datos del sensor conectado a D2 (GPIO4)
#define DHTTYPE DHT22      // Cambiar a DHT11 si usás ese modelo

DHT dht(DHTPIN, DHTTYPE);  // Inicializar el sensor

void setup() {
  Serial.begin(115200);
  dht.begin();
  Serial.println("Lectura de temperatura y humedad con ESP8266");
}

void loop() {
  delay(1500); // Esperar 2 segundos entre lecturas

  float humedad = dht.readHumidity();
  float temperatura = dht.readTemperature(); // °C

  // Verificar si la lectura fue exitosa
  if (isnan(humedad) || isnan(temperatura)) {
    Serial.println("Error al leer el sensor DHT!");
    return;
  }

  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.print(" °C\tHumedad: ");
  Serial.print(humedad);
  Serial.println(" %");
}
