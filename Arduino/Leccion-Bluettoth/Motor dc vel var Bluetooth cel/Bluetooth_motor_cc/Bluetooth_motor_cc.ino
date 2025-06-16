
int Motor_Pin = 9 ; 
const int BTPWR = 2;
int Control_motor;
char BluetoothData ;  // los datos recibidos del enlace serie bluetooth

void setup ( ) {
  Serial.begin ( 9600 ) ;
  pinMode(BTPWR, OUTPUT); 
  digitalWrite(BTPWR, HIGH);
  pinMode (Motor_Pin , OUTPUT ) ;
}

void loop ( ) {
if ( Serial . available ( ) ) {
  BluetoothData = Serial.read ( ) ;  
  if ( BluetoothData == 'R' ) {
      Control_motor = Serial.parseInt ( ) ;  
      analogWrite ( Motor_Pin , Control_motor ) ;
  }
}
}
