 // PWM LED Brightness y Bluetooth Serial Link Demo
 // Por keuwlsoft: www.keuwl.com 23 de agosto de 2015

 int Red_LED_Pin = 9 ;  // Pin PWM para LED rojo
 int Green_LED_Pin = 10 ;  // Pin PWM para LED verde
 int Blue_LED_Pin = 11 ;  // Pin PWM para LED azul
 const int BTPWR = 2;

 // Varibles para mantener valores de brillo que van desde 0 (apagado) a 255 (completamente encendido)
 int Red_value = 0 ;
 int Green_value = 0 ;
 int Blue_value = 0 ;

 char BluetoothData ;  // los datos recibidos del enlace serie bluetooth

 void setup ( ) {
  
  pinMode(BTPWR, OUTPUT); 
  digitalWrite(BTPWR, HIGH);
 
  // Inicializar pines LED como salidas
  pinMode ( Red_LED_Pin , OUTPUT ) ;
  pinMode ( Green_LED_Pin , OUTPUT ) ;
  pinMode ( Blue_LED_Pin , OUTPUT ) ;
  
  // comunicación serial initialsie
  Serial.begin ( 9600 ) ;
 }

 void loop ( ) {

  // procesar cualquier información proveniente del enlace serie bluetooth
  if ( Serial . available ( ) ) {
  BluetoothData = Serial.read ( ) ;  // Obtener el siguiente personaje de bluetooth
  if ( BluetoothData == 'R' ) Red_value = Serial.parseInt ( ) ;  // Leer valor rojo
  if ( BluetoothData == 'G' ) Green_value = Serial.parseInt ( ) ;  // Lee el valor verde
  if ( BluetoothData == 'B' ) Blue_value = Serial.parseInt ( ) ;  // Lee el valor azul
  }
 
  // actualizar brillo de LED
  analogWrite ( Red_LED_Pin , Red_value ) ;
  analogWrite ( Green_LED_Pin , Green_value ) ;
  analogWrite ( Blue_LED_Pin , Blue_value ) ;
   
 }
