#include "Entropy.h"
#include "EEPROM.h"
int bitcount = 0;
int hexcount;
String privHex;
int privBin;
String privBinFinal;
int address = 0;

void setup()
{
 Serial.begin(9600);
 Entropy.initialize();
 while(bitcount < 256){
   while(hexcount < 4)
   {
    int privBinTemp;
      while(hexcount < 4)
      {
    privBinTemp += (Entropy.random(2));
    hexcount = hexcount + 1;
    delay(10);
      }
      privBin = privBinTemp;
   }
   EEPROM.write(address, privBin);
   address = address + 1;
   privHex += String(privBin, HEX);
   bitcount = bitcount + 8;
   hexcount = 0;
  }
  Serial.print(privHex);
  Serial.print("\n");
}

void loop()
{
  
}
