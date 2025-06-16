int ENABLE_b = 7 ; 
const int BTPWR = 2;
int Control_ENA_b;
char BluetoothData ;  // los datos recibidos del enlace serie bluetooth
int M2a=8;
int M2b=9;

void setup ( ) {
  Serial.begin ( 9600 ) ;
  pinMode(BTPWR, OUTPUT); 
  digitalWrite(BTPWR, HIGH);
  pinMode (ENABLE_b , OUTPUT ) ;
  digitalWrite(M2a,1);
  digitalWrite(M2b,0);
  
}

void loop ( ) {
if ( Serial . available ( ) ) {
  BluetoothData = Serial.read ( ) ;  
  if ( BluetoothData == 'R' ) {
      Control_ENA_b = Serial.parseInt ( ) ;  
      analogWrite (ENABLE_b , Control_ENA_b) ;
      delay(15);
  }
}
}
