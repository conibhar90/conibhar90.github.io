#include <Servo.h>

const int servo_x = 5;         // pan servo pin
const int servo_y = 6;         // tilt servo pin
const int x_in = A0;          // horizontal joystick input
const int y_in = A1;          // vertical joystick input
const int sw_button = 2;          // joystick push button input

int convert_x;
int convert_y;

Servo servo_pan;          // pan servo object
Servo servo_tilt;          // tilt servo object

void setup(){
  servo_pan.attach(servo_x);          
  servo_tilt.attach(servo_y);
  pinMode(x_in, INPUT);
  pinMode(y_in, INPUT);
  
  Serial.begin(9600);      // serial initialization
  
}

void loop(){
  
  outputJoystick();
  
  //servo_pan.writeMicroseconds(1404);          // 90 degrees rotation
  //servo_tilt.writeMicroseconds(1010);          // 45 degrees rotation
  
  convert_x = analogRead(x_in);
  convert_x = map(convert_x, 0, 1023, 615, 2194);          // convert joystick value to equivalent PWM pan axis angular displacement value(microseconds)
  servo_pan.writeMicroseconds(convert_x);          // pan servo movement
  
  convert_y = analogRead(y_in);
  convert_y = map(convert_y, 0, 1023, 615, 1492);          //tilt PWM displacement conversion(microseconds)
  servo_tilt.writeMicroseconds(convert_y);          //tilt servo movement
                                                                                                                                              
 
  
}

void outputJoystick(){

    Serial.print(analogRead(x_in));
    Serial.print ("---"); 
    Serial.print(analogRead(y_in));
    Serial.println ("----------------");
}
