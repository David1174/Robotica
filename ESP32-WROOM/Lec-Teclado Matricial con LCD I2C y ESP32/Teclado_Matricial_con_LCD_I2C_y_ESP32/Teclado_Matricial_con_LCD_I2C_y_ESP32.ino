#include <Keypad.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Configuración de la pantalla LCD 16x2 en dirección I2C 0x27
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Definición de filas y columnas del teclado 4x4
const byte FILAS = 4;
const byte COLUMNAS = 4;

// Mapa de teclas
char teclas[FILAS][COLUMNAS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

// Pines del ESP32 conectados al teclado (ajusta si usas otros)
byte pinesFilas[FILAS] = {13, 12, 14, 27};     // GPIOs para filas
byte pinesColumnas[COLUMNAS] = {26, 25, 33, 32}; // GPIOs para columnas

// Inicialización del teclado
Keypad teclado = Keypad(makeKeymap(teclas), pinesFilas, pinesColumnas, FILAS, COLUMNAS);

void setup() {
  lcd.init();            // Inicializa la pantalla LCD
  lcd.backlight();       // Enciende la luz de fondo
  lcd.setCursor(0, 0);
  lcd.print("Presiona tecla:");
}

void loop() {
  char tecla = teclado.getKey(); // Lee una tecla

  if (tecla) {
    lcd.setCursor(0, 1);
    lcd.print("Tecla: ");
    lcd.print(tecla);
    lcd.print("   "); // Espacios para limpiar caracteres anteriores
  }
}
