#include <Servo.h>                           // Include servo library

Servo servoRight;
Servo servoLeft;

void moveKitty() {
  // Your Code Here
}

void stopKitty() {
  // Your Code Here
}

int leftWhisker = 5; 
int rightWhisker = 7;
int aAnalogPin = A0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
  pinMode(leftWhisker, INPUT);
  pinMode(rightWhisker, INPUT);
  
}



void loop() {
  // put your main code here, to run repeatedly:
  int leftWvalue = digitalRead(leftWhisker);
  int rightWvalue = digitalRead(rightWhisker);
  int aValue = analogRead(A0);
  
  Serial.print("Left: "); 
  Serial.print(leftWvalue);
  Serial.print("Right: ");
  Serial.print(rightWvalue);
  Serial.println("");
  delay(100);
  Serial.println(aValue);

  if (leftWvalue == 0 && rightWvalue == 0){
    Serial.println("Left and Right Whiskers pressed!");
  }
  else if (leftWvalue == 0){
    Serial.print("Left is pressed!");
  }
  else if (rightWvalue == 0){
    Serial.print ("Right is pressed!");
  }
   else {
    Serial.print ("No whiskers pressed!");
   }
  
}
