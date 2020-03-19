#include <Arduino.h>
#include "ServoEasing.h"
#include <Wire.h>
#define SLAVE_ADDRESS 0x08 

const int servo_x = 5;         // pan servo pin
const int servo_y = 6;         // tilt servo pin


int convert_x;
int convert_y;
String str_commands = "";

ServoEasing servo_pan;          // pan servo object
ServoEasing servo_tilt;          // tilt servo object

void setup()
{
  servo_pan.attach(servo_x);          //associate the pan servo object with the pan servo pin          
  servo_tilt.attach(servo_y);         //associate the tilt servo object with the tilt servo pin
  
  servo_pan.setEasingType(EASE_SINE_IN_OUT);          //sinusoidal easing mode on for the pan servo
  servo_tilt.setEasingType(EASE_SINE_IN_OUT);         //sinusoidal easing mode on for the tilt servo
  setSpeedForAllServos(45);         //speed setting
  
  Serial.begin(115200);      // serial initialization

  servo_pan.write(90);          // neutral 90 degrees initial position
  servo_tilt.write(45);          // neutral 45 degrees initial position
  Wire.begin(SLAVE_ADDRESS);          //begin I2C communication
  Wire.onReceive(receive_commands);
  Wire.onRequest(ardu_feedback);
  delay(2000);          //2 sec delay
}

void loop()
{
  
  //outputJoystick();
  
  //convert_x = ;
  //convert_x = map(convert_x, 0, 1023, 0, 180);          // convert joystick value to equivalent pan axis angular displacement value
  //servo_pan.startEaseTo(convert_x);          // pan servo movement
  
  //convert_y = ;
  //convert_y = map(convert_y, 0, 1023, 0, 100);          //tilt displacement conversion
  //servo_tilt.startEaseTo(convert_y);          //tilt servo movement
                                                                                                                                              
  //delay(675);
  
}
void cam_turn(String commands)
{
  
}
void receive_commands(int byteCount)
{
  
  while (Wire.available())
  {
    str_commands += (char)Wire.read();     //convert bytes data into a string
    
  }
  Serial.println(str_commands);
  str_commands = "";     //reset variable
  
}


void ardu_feedback()
{


  
}
