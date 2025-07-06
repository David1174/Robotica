#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Dirección I2C del LCD (ajustar si es necesario)
LiquidCrystal_I2C lcd(0x27, 16, 2);  // 0x3F si no funciona con 0x27

void setup() {
  lcd.init();           // Inicializa el LCD
  lcd.backlight();      // Enciende la luz de fondo

  lcd.setCursor(0, 0);  // Columna 0, fila 0
  lcd.print("Hola ESP32!");

  lcd.setCursor(0, 1);  // Columna 0, fila 1
  lcd.print("LCD I2C OK!");
}

void loop() {
  // Podés agregar código aquí si querés actualizar el LCD
}
