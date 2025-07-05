#include <ESP8266WiFi.h>

const char* ssid = "ESP8266_LED";
const char* password = "12345678";

WiFiServer server(80);
bool ledState = false;
const int ledPin = LED_BUILTIN;  // Usualmente GPIO2

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH); // LED apagado (activo en bajo)

  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  server.begin();

  Serial.println("Access Point iniciado");
  Serial.print("IP: ");
  Serial.println(WiFi.softAPIP());
}

void loop() {
  WiFiClient client = server.available();
  if (!client) return;

  while (client.connected() && !client.available()) delay(1);
  String request = client.readStringUntil('\r');
  client.flush();

  if (request.indexOf("LED=ON") != -1) {
    digitalWrite(ledPin, LOW);  // Enciende LED
    ledState = true;
  } else if (request.indexOf("LED=OFF") != -1) {
    digitalWrite(ledPin, HIGH); // Apaga LED
    ledState = false;
  }

  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/plain");
  client.println("Connection: close");
  client.println();
  client.print("LED is ");
  client.print(ledState ? "ON" : "OFF");
}
