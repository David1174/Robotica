#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "ESP32_RED";
const char* password = "12345678";

WebServer server(80);
#define LED_BUILTIN 2

void handleLedOn() {
  digitalWrite(LED_BUILTIN, HIGH);
  server.send(200, "text/plain", "LED encendido");
}

void handleLedOff() {
  digitalWrite(LED_BUILTIN, LOW);
  server.send(200, "text/plain", "LED apagado");
}

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  delay(100);
  Serial.print("IP: ");
  Serial.println(WiFi.softAPIP());
  server.on("/led/on", handleLedOn);
  server.on("/led/off", handleLedOff);
  server.begin();
}

void loop() {
  server.handleClient();
}
