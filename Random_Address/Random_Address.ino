#include "Entropy.h"
#include "EEPROM.h"
int bitcount = 0;
int hexcount;
String privHex;
int privBin;
String privBinFinal;
int address = 0;
int value;
String hex;
char incoming;

void read_address()
{
  while(address < 37)
  {
   value = EEPROM.read(address);
   hex += String(value, HEX);
   address = address + 1;
   delay(10); 
  }
  Serial.flush();
  Serial.print(hex);
  Serial.flush();
  Serial.print("\n");
}

void new_address()
{
 Entropy.initialize();
 while(bitcount < 256)
 {
   hexcount = 0;
   while(hexcount < 3)
   {
    privBin += (Entropy.random(2));
    hexcount = hexcount + 1;
   }
   privHex += String(privBin, HEX);
   bitcount = bitcount + 7;
   EEPROM.write(address, privBin);
   address = address + 1;
   }
   Serial.print("\n");
}
void setup()
{
 Serial.begin(9600);
 
}
void loop()
{
  if (Serial.available() != 0) {
 incoming = Serial.read();
 if(incoming == '1')
 {
   new_address();
 }
 if(incoming == '2')
 {
   delay(100);
   read_address();
 }
 
}
}
