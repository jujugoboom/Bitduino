Bitduino
========

Generate Bitcoin Addresses Using Arduino

Setup
-----
1) Download all necesary files
2) Run Setup.sh if on Mac or linux or Setup.bat for Windows(not tested)
3) Copy the folder Entropy to your Arduino Libraries folder or in the Arduino IDE click sketch>import library>add library and find the Entropy folder

Usage
-----
1) Connect your Arduino
2) Open the file Random_Address.ino inside of the Random_Address folder in the download
3) Make note of where the Arduino IDE says your Arduino is connected (bottom right-hand corner)
4) Upload the sketch to your Arduino
6) In terminal run "cd ~/[PATH_TO_DOWNLOAD]" and then  "python generate.py"
7) When it asks what port arduino is connected to, type in the info from step 3
8) Choose whether you want to generate a new address (CANNOT BE UNDONE) or read out an existing address
8) If you chose to generate a new one, wait for it to generate, then you can readout either the Public Address or the Private key in WIF
9) It will show in the command line whichever one you chose and also make a QR code of it in the folder you are running it from

Security
--------
This is a way to generate a Bitcoin private key which can then be used to send and recieve bitcoin. This way is not entirely secure. I would recomend using a computer that has never touched the internet or a raspberry pi that has never touched the internet. If anyone gets your private key they also get full control of your bitcoins. 

Disclaimer
----------
This is my first bitcoin code and I am new to python.

Update
------
Now using the Entropy library on Arduinos that support it (i.e. Arduino Uno and newer Arduino Megas). This library is tested to be random. It is useful in cryptographic situations, such as this one.

Private keys are now written to the EEPROM on the arduino. Using the sketch Read_EEPROM.ino will readout the key that is stored on the arduino. You can see this in the arduino serial monitor in hex, or you can run it with generate.py to re-generate a compressed private key or a public address. IT ONLY STORES ONE PRIVATE KEY AT A TIME. EVERYTIME YOU RE-RUN THE RANDOM ADDRESS CODE, YOUR PRIVATE KEY WRITTEN ON THE ARDUINO IS OVERWRITTEN.
Everything is compressed into one arduino sketch and one python script.
 
-------------------------------------------------------------------------------------------------------------------

If you have any questions or suggestions, please feel free to leave them in the github, or email me at jujugoboom@gmail.com. Thanks for trying this out. I hope you find it as fun and interesting as I.
