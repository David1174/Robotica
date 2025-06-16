#include <DS1302.h>

DS1302 rtc(8,7,6); //8=RST; 7=DAT; 6=CLK

Time t;

void setup() {
  
  Serial.begin(9600);
  
  rtc.halt(false);
  rtc.writeProtect(false);
  
  rtc.setDOW(TUESDAY);
  
  rtc.setTime(21,03,00);
  
  rtc.setDate(4,3,2014);
  
  delay(1000);
  
  //Serial.print(
}

void loop() {
  t = rtc.getTime();
  
  Serial.print("hora:");
  Serial.print(t.hour);
  
  Serial.print(", min:");
  Serial.print(t.min);
  
  Serial.print(", seg:");
  Serial.println(t.sec);

  
  delay(1000);
  
}
