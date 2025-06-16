 #include <Keypad.h>;
const byte ROWS = 4;
const byte COLS = 4;
char keys[ROWS][COLS] = {
 {'1','2','3','A'},
 {'4','5','6','B'},
 {'7','8','9','C'},
 {'*','0','#','D'}
};
byte rowPins[ROWS] = {9,8,7,6}; //Filas(pines del 9 al 6)
byte colPins[COLS] = {5,4,3,2}; //Columnas (pines del 5 al 2)
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );
char clave[5]={'A','9','2','2','3'};
char inclave[5]={0,0,0,0,0};
int maxind=4; 
int c;
int led = 13;
int sen1=0;
int i=0;
////////////////////////////////////////////////////////////////////VOID SETUP
void setup(){
Serial.begin (9600);
pinMode(led, OUTPUT);
}
////////////////////////////////////////////////////////////////////VOID LOOP
void loop(){
char key = keypad.getKey();//char
switch(key)
{
  case '1':
     c=0;
     Serial.println("Carga vector:");
     while(key!='#')
     {
       key = keypad.getKey();//char
       if(key && key!='#')
       {
          inclave[c]=key;
          Serial.println(key);
          c=c+1;
       }
      }
      Serial.println("salio del ciclo");
      //Serial.print(); 
      break;
  
   case '2':
     Serial.println("Control clave");
     i=0;
     while(sen1==0 && i<maxind)
     {
       if (inclave[i]!=clave[i])
       {
           //Serial.println("si sen1 =1");
           //delay(1500);
           sen1=1;
       }
       i=i+1;
     }
          
     if(sen1==1)
     { Serial.println("No coincide");  }
     else
     { Serial.println("Si coinciden"); }
     sen1=0;
     break;
     
}//Fin Estructura de casos
}//Fin Loop
 
