#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

//Crear el objeto lcd  dirección  0x3F y 16 columnas x 2 filas
LiquidCrystal_I2C lcd(0x27,16,2);  //

void setup() {
  // Inicializar el LCD
  lcd.init();  //opcion : lcd.init() // lcd.begin()
  //Encender la luz de fondo.
  lcd.backlight();
  
  // Escribimos el Mensaje en el LCD.
  lcd.setCursor(0, 0);
  lcd.print("Aula 9");
}

void loop() {

}
