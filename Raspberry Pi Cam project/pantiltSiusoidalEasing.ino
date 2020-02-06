#include <Arduino.h>
#include "ServoEasing.h"

const int servo_x = 5;         // pan servo pin
const int servo_y = 6;         // tilt servo pin
const int x_in = A0;          // horizontal joystick input
const int y_in = A1;          // vertical joystick input
const int sw_button = 2;          // joystick push button input

int convert_x;
int convert_y;

ServoEasing servo_pan;          // pan servo object
ServoEasing servo_tilt;          // tilt servo object

void setup(){
  servo_pan.attach(servo_x);          
  servo_tilt.attach(servo_y);
  pinMode(x_in, INPUT);
  pinMode(y_in, INPUT);
  servo_pan.setEasingType(EASE_SINE_IN_OUT);
  servo_tilt.setEasingType(EASE_SINE_IN_OUT);
  setSpeedForAllServos(45);
  
  Serial.begin(115200);      // serial initialization

  servo_pan.write(90);          // neutral 90 degrees initial position
  servo_tilt.write(45);          // neutral 45 degrees initial position
  delay(2000);
}

void loop(){
  
  outputJoystick();
  
  convert_x = analogRead(x_in);
  convert_x = map(convert_x, 0, 1023, 0, 180);          // convert joystick value to equivalent pan axis angular displacement value
  servo_pan.startEaseTo(convert_x);          // pan servo movement
  
  convert_y = analogRead(y_in);
  convert_y = map(convert_y, 0, 1023, 0, 100);          //tilt displacement conversion
  servo_tilt.startEaseTo(convert_y);          //tilt servo movement
                                                                                                                                              
  delay(675);
  
}

void outputJoystick(){

    Serial.print(analogRead(x_in));
    Serial.print ("---"); 
    Serial.print(analogRead(y_in));
    Serial.println ("----------------");
}
