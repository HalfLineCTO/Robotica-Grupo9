
#include <Servo.h>

Servo myservoH;  // create a servo object hombro
Servo myservoC; // create a servo object codo
Servo myservoG; // create a servo object garra

// iniciar variables mensaje serial
int y1=0;
int y2=0;
int y3=0;
int y4=0;
int suma_h = 90;
int suma_c = 180;
int suma_g = 0;

void setup() {
  Serial.begin(250000);
  Serial.setTimeout(1);
  myservoH.attach(7);// hombro
  myservoC.attach(2);// codo
  myservoG.attach(3);// garra
  myservoC.write(180);
  myservoG.write(0);
  delay(1000);
  myservoH.write(90);
  
  
}

void loop() {
  
   
  if (Serial.available() > 0) {

  String inputString = Serial.readString();
  
  int values[4]; // array to store the four parsed floats
  int valueIndex = 0; // index to keep track of which float is being parsed
  int commaIndex = 0; // index to keep track of the comma position

  while (commaIndex >= 0) {
    commaIndex = inputString.indexOf(","); // find the next comma in the input string
    if (commaIndex >= 0) {
      values[valueIndex] = atoi(inputString.substring(0, commaIndex).c_str()); // parse the float between the start of the string and the comma
      inputString = inputString.substring(commaIndex + 1); // remove the parsed float and the comma from the input string
      valueIndex++; // increment the index to parse the next float
    }
  }

  values[valueIndex] = atoi(inputString.c_str()); // parse the final float in the input string
  

  // destructure
  y1 = values[0]; //cual servo se mueve
  y2 = values[1]; //vel servo hombro
  y3 = values[2]; //vel servo codo
  y4 = values[3]; //vel servo garra
  
  }
  
  //hombro adelante
  if(y1==1) {
    if(suma_h<180){
    suma_h=suma_h+y2;
    delay(10);
    myservoH.write(suma_h);
    }
    
    
  }
  //hombro atras
  if(y1==2) {
    
    suma_h=suma_h-y2;
    delay(10);
    myservoH.write(suma_h);
    
  }
  //codo adelante
  if(y1==3) {
    
    suma_c = suma_c - y3;
    delay(10);
    myservoC.write(suma_c);
    
    
  }
  //codo atras
  if(y1==4) {
    suma_c=suma_c + y3;
    delay(10);
    myservoC.write(suma_c);
    
   
   //abrir 
  }
  if(y1==5) {
    suma_g= suma_g +y4;
    delay(10);
    myservoG.write(suma_g);
    
  }
//cerrar garra
  if(y1==6) {
    suma_g= suma_g - y4;
    delay(10);
    myservoG.write(suma_g);
    
  }
  
}
  // put your setup code here, to run once:
