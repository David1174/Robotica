#include <Keypad.h>

// Definir cantidad de filas y columnas
const byte FILAS = 4;
const byte COLUMNAS = 4;

// Mapa de teclas
char teclas[FILAS][COLUMNAS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

// Pines conectados a filas y columnas
byte pinesFilas[FILAS] = {13, 12, 14, 27};
byte pinesColumnas[COLUMNAS] = {26, 25, 33, 32};

// Crear objeto Keypad
Keypad teclado = Keypad(makeKeymap(teclas), pinesFilas, pinesColumnas, FILAS, COLUMNAS);

void setup() {
  Serial.begin(115200);
}

void loop() {
  char tecla = teclado.getKey();
  if (tecla) {
    Serial.println(tecla);
  }
}
