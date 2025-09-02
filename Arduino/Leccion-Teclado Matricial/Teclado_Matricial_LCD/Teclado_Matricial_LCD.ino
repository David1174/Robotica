#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <Keypad.h>

//Crear el objeto lcd  dirección  0x3F y 16 columnas x 2 filas
LiquidCrystal_I2C lcd(0x27,16,2);  

const byte filas = 4;
const byte columnas = 4;
byte pinesF[filas] = {9,8,7,6};
byte pinesC[columnas] = {5,4,3,2};
 
char teclas[filas][columnas] = {
 
 {'1','2','3','A'},
 {'4','5','6','B'},
 {'7','8','9','C'},
 {'*','0','#','D'}
};
 
Keypad teclado = Keypad(makeKeymap(teclas), pinesF, pinesC, filas, columnas);
 
char tecla;

void setup() {
  // Inicializar el LCD
  lcd.init();  //opcion : lcd.begin / lcd.init 
  //Encender la luz de fondo.
  lcd.backlight();  
  // Escribimos el Mensaje en el LCD.
  lcd.setCursor(0, 0);  
}

void loop() {
  tecla = teclado.getKey();
  if (tecla) lcd.print(tecla);
  if (tecla == '#')  lcd.clear();   
}
