int sonido = 9;


void setup()
{
  pinMode(sonido,OUTPUT);
}

void loop()
{
  tone(sonido,261.63); //1. do,  Que 
  delay(350);
  noTone(sonido);
  
  tone(sonido,261.63);  //2. do,  los
  delay(250);
  noTone(sonido);

  tone(sonido,293.67);  //3. re,  cum
  delay(500);
  noTone(sonido);
  
  tone(sonido,261.63);   //4. do,  pla
  delay(450);
  noTone(sonido);

  tone(sonido,349.23);  //5. fa,  fe
  delay(500);
  noTone(sonido);

  tone(sonido,329.63);  //6. mi,  liz
  delay(450);
  noTone(sonido);

  delay(800);

  tone(sonido,261.63); //7. do,  Que
  delay(300);
  noTone(sonido);
  
  tone(sonido,261.63);  //8. do, los 
  delay(250);
  noTone(sonido);

  tone(sonido,293.67);  //9. re,  cum
  delay(500);
  noTone(sonido);
  
  tone(sonido,261.63);   //10. do,  pla
  delay(450);
  noTone(sonido);

  tone(sonido,392);  //11. sol,  fe
  delay(500);
  noTone(sonido);

  tone(sonido,349.23);  //12. fa,  liz
  delay(500);
  noTone(sonido);

  delay(800);   // Pausa

  tone(sonido,261.63);  //13. do,  que 
  delay(300);
  noTone(sonido);

  tone(sonido,261.63);  //14. do,  los
  delay(250);
  noTone(sonido);

  tone(sonido,523.25);  //15. do(8+),  cum
  delay(500);
  noTone(sonido);

  tone(sonido,440);  //16. la,  pla
  delay(500);
  noTone(sonido);

  tone(sonido,349.23);  //17. fa ...
  delay(450);
  noTone(sonido);

  tone(sonido,329.63);  //18. mi ...
  delay(500);
  noTone(sonido);

  tone(sonido,293.67);  //19. re ...
  delay(600);
  noTone(sonido);

  delay(600);  // pausa 

  tone(sonido,466.16);  //20. la#,  que
  delay(300);
  noTone(sonido);

  tone(sonido,466.16);  //21. la#,  los
  delay(300);
  noTone(sonido);

  tone(sonido,440);  //22.  la,  cum
  delay(500);
  noTone(sonido);

  tone(sonido,349.23);  //23. fa,  pla 
  delay(500);
  noTone(sonido);

  tone(sonido,392);  //24. sol,  fe 
  delay(500);
  noTone(sonido);

  tone(sonido,349.23);  //25. fa,  liz
  delay(600);
  noTone(sonido);

  delay(600); // Pausa
  
  
}
