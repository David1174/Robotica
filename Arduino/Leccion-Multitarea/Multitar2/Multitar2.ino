int estado_led=0;
int bandera_tono=0;

int bocina=11;
int parlante=9;
int led=10;

int amplit_cte1=100;  //led
int amplit_cte2=1000;  //parlante

int amplit_var1=0;
int amplit_var2=0;
int avanza1=0;
int avanza2=0;
int inicio1=0;
int inicio2=0;

int amplit_fin_cte;
int amplit_fin_var;
int inicio_fin=0;
int avanza_fin=0;

char key;


void setup() {
  Serial.begin(9600);
  pinMode(parlante,OUTPUT);
  pinMode(led,OUTPUT);
  pinMode(bocina,OUTPUT);
}

void loop() {
  
  amplit_fin_cte=8000;
  inicio_fin=millis();
  
  do{
      avanza1=millis();
      amplit_var1=avanza1-inicio1;
      if(amplit_var1>=amplit_cte1) {
         inicio1=avanza1;
         if(estado_led==0) {
            estado_led=1; 
         }else {
            estado_led=0; 
         }          
         digitalWrite(led,estado_led);
      }
      
      avanza2=millis();
      amplit_var2=avanza2-inicio2;
      if(amplit_var2>=amplit_cte2) {
         inicio2=avanza2;
         if(bandera_tono==0) {
            tone(parlante,500);
            bandera_tono=1;
         }else {
            noTone(parlante);
            bandera_tono=0;
         }
      }

      avanza_fin=millis();
      amplit_fin_var=avanza_fin-inicio_fin; 
      //Serial.println(amplit_fin_var);   
      key=Serial.read();
      
  }while (key != '*' && amplit_fin_var<amplit_fin_cte );
  
  if(key!='*') {
     Serial.println("Alarma activa");
     digitalWrite(bocina,1);  
     noTone(parlante);
  }else{
     Serial.println("apague alarma");
     noTone(parlante);
  }
  
 /* digitalWrite(led,0);
  noTone(parlante);
  Serial.println("sali");
  delay(4000);*/
  
} // loop
