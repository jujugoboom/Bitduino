#include "Entropy.h"
#include "EEPROM.h"
int bitcount = 0;
int hexcount;
String privHex;
int privBin;
int address = 0;

void setup()
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
}

void loop()
{
  
}
