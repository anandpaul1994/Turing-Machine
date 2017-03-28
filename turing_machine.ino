#include <Stepper.h>
#include<Servo.h>

// initialize the stepper library on pins 8 through 11:
Stepper roll(200, 8, 9, 10, 11);
Servo servoz,servoy,servor;
int i,pos,pos1;
char c;
void setup() {
  roll.setSpeed(25);
  servoy.attach(3);
  servoz.attach(5);
  servor.attach(6);
  pinMode(2,OUTPUT);
  pinMode(4,OUTPUT);
  // initialize the serial port:
  Serial.begin(9600);

    servor.write(0);              // tell servo to go to position in variable 'pos'

    servoy.write(35);              // tell servo to go to position in variable 'pos'

    servoz.write(100);              // tell servo to go to position in variable 'pos'

}

void right()
{
  roll.step(-100);
}

void left()
{
  roll.step(100);
}


void one()
{
  
  roll.step(-50);
  for (pos = 100; pos >= 0; pos -= 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    servoz.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 35; pos <= 125; pos += 1) { // goes from 180 degrees to 0 degrees
    servoy.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15); 
  }
  for (pos = 125; pos >= 35; pos -= 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    servoy.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 0; pos <= 100; pos += 1) { // goes from 180 degrees to 0 degrees
    servoz.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15); 
  }
  roll.step(50);
  
}

void zero()
{
  roll.step(-25);
  for (pos = 100; pos >= 0; pos -= 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    servoz.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 35; pos <= 125; pos += 1) { // goes from 180 degrees to 0 degrees
    servoy.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15); 
  }
  
  roll.step(-50);
  
  for (pos = 125; pos >= 35; pos -= 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    servoy.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }

  roll.step(50);
  
  for (pos = 0; pos <= 100; pos += 1) { // goes from 180 degrees to 0 degrees
    servoz.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15); 
  }
  
  roll.step(25);  
}

void rubb()
{
  roll.step(-400);
  digitalWrite(4,HIGH);
  digitalWrite(2,LOW);
  for (pos = 0; pos <= 100; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    servor.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for(pos=0;pos<7;pos+=1){

    for (pos1 = 100; pos1 >= 0; pos1 -= 1) { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      servor.write(pos1);              // tell servo to go to position in variable 'pos'
      delay(15);}
   roll.step(15);
    for (pos1 = 0; pos1 <= 100; pos1 += 1) { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      servor.write(pos1);              // tell servo to go to position in variable 'pos'
      delay(15); }                      // waits 15ms for the servo to reach the position
  }

  
  for (pos = 100; pos >= 0; pos -= 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    servor.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  digitalWrite(2,LOW);
  digitalWrite(4,LOW);
  roll.step(295);
  
}
void loop()
{
  c=Serial.read();
  if(c=='0')
  {
  zero();
  Serial.print(c);
  }
  else if(c=='1')
  {
  one();
  Serial.print(c);
  }
  else if((c=='2')||(c==' '))
  {
  rubb();
  Serial.print(c);
  }
  else if(c=='3')
  {
  right();
  Serial.print(c);
  }
  else if(c=='4')
  {
  left();
  Serial.print(c);
  }
}

