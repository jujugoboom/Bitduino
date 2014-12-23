#include "TrueRandom.h"
int bitcount = 0;
int hexcount;
String privHex;
int privBin;
String privBinFinal;

void setup()
{
 Serial.begin(9600);
 while(bitcount < 256){
   while(hexcount < 4)
   {
    int privBinTemp;
      while(hexcount < 4)
      {
    privBinTemp += (TrueRandom.randomBit());
    hexcount = hexcount + 1;
    delay(10);
      }
      privBin = privBinTemp;
   }
   privHex += String(privBin, HEX);
   bitcount = bitcount + 8;
   hexcount = 0;
  }
  Serial.print(privHex);
  delay(100);
  Serial.print("\n");
}

void loop()
{
  ;
}
