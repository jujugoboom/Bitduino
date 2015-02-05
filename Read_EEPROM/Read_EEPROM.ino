#include "EEPROM.h"
int address = 0;
int value;
String hex;

void setup()
{
  Serial.begin(9600);
  while(address < 32)
  {
   value = EEPROM.read(address);
   hex += String(value, HEX);
   address = address + 1;
   delay(10); 
  }
  Serial.print(hex);
  Serial.print("\n");
}
void loop()
{
  
}
