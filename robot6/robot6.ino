
#include <Servo.h>                           // Include servo library

Servo servoRight;
Servo servoLeft;


int leftWhisker = 5; 
int rightWhisker = 7;
int rightLED = 3;
int leftLED = 4;


void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600); 
  pinMode(leftWhisker, INPUT);
  pinMode(rightWhisker, INPUT);
  pinMode(rightLED, OUTPUT);
  pinMode(leftLED, OUTPUT);
  servoLeft.attach(13);
  servoRight.attach(12);
   servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
}

void loop() {
  // put your main code here, to run repeatedly:
  int leftWvalue = digitalRead(leftWhisker);
  int rightWvalue = digitalRead(rightWhisker);


  
 /* Serial.print("Left: "); 
  Serial.print(leftWvalue);
  Serial.print("Right: ");
  Serial.print(rightWvalue); */
  
  Serial.println("");
  delay(100);
  
  if (leftWvalue == 0 && rightWvalue == 0){
    digitalWrite(leftLED, HIGH);
    digitalWrite(rightLED, HIGH);
    Serial.println("Left and Right Whiskers pressed!");
    forward();
    delay(1000);
    still();
  }
  else if (leftWvalue == 0){
     digitalWrite(leftLED, HIGH);
    digitalWrite(rightLED, LOW);
    Serial.print("Left is pressed!");
    cw();
    delay(1000);
    still();
  }
  else if (rightWvalue == 0){
     digitalWrite(leftLED, LOW);
    digitalWrite(rightLED, HIGH);
    Serial.print ("Right is pressed!");
    ccw();
    delay(1000);
    still();
  }
   else {
     digitalWrite(leftLED, LOW);
    digitalWrite(rightLED, LOW);
    Serial.print ("No whiskers pressed!");
    backward();
    delay(1000);
    still();
   }
  
}

void forward() {
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
}

void backward(){
   servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
}

void ccw(){
   servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1300);
}

void cw(){
   servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1700);
}

void still(){
   servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
}
