#include <ESP32Servo.h>

Servo upperLid;
Servo lowerLid;

const int UPPER_PIN = 13;  // change this
const int LOWER_PIN = 12;  // change this

const int CLOSED = 90;
const int OPEN = 0;  // change direction if lid goes wrong way (try 180)

void setup() {
  upperLid.attach(UPPER_PIN);
  lowerLid.attach(LOWER_PIN);
  
  // start closed
  upperLid.write(CLOSED);
  lowerLid.write(CLOSED);
  delay(1000);
}

void loop() {
  // open
  upperLid.write(OPEN);
  lowerLid.write(OPEN);
  delay(2000);
  
  // close
  upperLid.write(CLOSED);
  lowerLid.write(CLOSED);
  delay(2000);
}