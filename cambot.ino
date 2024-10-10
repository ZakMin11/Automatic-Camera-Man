#include <Servo.h>


Servo servo;
int pos;
int serData;
void setup() {
  servo.attach(7);
  Serial.begin(9600);
  servo.write(90);
  Serial.setTimeout(10);
}

void serialEvent() {
  int serData = Serial.parseInt();
  if (serData != 0) {
    int val = constrain(serData, 0,180);
    servo.write(val);
  }
}

void loop() { 

}
