/*
  Ejercicio: Control de brillo de un LED con potenciómetro
  Objetivo: Leer el valor del potenciómetro y usarlo para variar el brillo del LED.
  Aprendizaje: Entradas analógicas, salidas PWM y mapeo de valores.
*/

const int pinPot = A0;   // Pin del potenciómetro (terminal central)
const int pinLed = 9;    // Pin PWM del LED
int valorPot;            // Variable para guardar la lectura del potenciómetro
int brilloLed;           // Variable para guardar el valor de brillo

void setup() {
  Serial.begin(9600);    // Iniciar comunicación serie para ver valores
}

void loop() {
  // Leer el valor del potenciómetro (0 a 1023)
  valorPot = analogRead(pinPot);

  // Convertir ese valor a un rango de 0 a 255 para PWM
  brilloLed = map(valorPot, 0, 1023, 0, 255);

  // Aplicar ese valor al LED
  analogWrite(pinLed, brilloLed);

  // Mostrar en el monitor serie
  Serial.print("Potenciómetro: ");
  Serial.print(valorPot);
  Serial.print("  |  Brillo LED: ");
  Serial.println(brilloLed);

  delay(10); // Pequeña pausa para estabilidad
}
