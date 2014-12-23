Bitduino
========

Generate Bitcoin Private Addresses Using Arduino

Setup
-----
1) Download all necesary files
2) Run Setup.sh if on Mac or linux or Setup.bat for Windows(not tested)
3) Copy the folder True Random to your Arduino Libraries folder or in the Arduino IDE click sketch>import library>add library and find the True Random folder

Usage
-----
1) Connect your Arduino
2) Open the file Random_Address.ino inside of the Random_Address folder in the download
3) Make note of where the Arduino IDE says your Arduino is connected (bottom right-hand corner)
4) Upload the sketch to your Arduino
5) In terminal run "cd ~/[PATH_TO_DOWNLOAD]" and then  "python GenerateKey.py"
6) When it asks what port arduino is connected to, type in the info from step 3
7) Let it work its magic
8) It will print out the private key in wallet import format and the public address also make a qr code of both inside the folder of the download.

Security
--------
This is a way to generate a Bitcoin private key which can then be used to send and recieve bitcoin. This way is not entirely secure. I would recomend using a computer that has never touched the internet or a raspberry pi that has never touched the internet. If anyone gets your private key they also get full control of your bitcoins. The TrueRandom library is plenty random for most people, but is not completly random. It has a tendency when generating the original binary to generate a 0 more than a 1. It uses static voltage in pin A0 so please do not connect anything to it. A better way would be to use a hardare random number generator, but I do not have one. If there is one that you would like to see implemented, email me.

Disclaimer
----------
This is my first bitcoin code and I am new to python.
 
-------------------------------------------------------------------------------------------------------------------

If you have any questions or suggestions, please feel free to leave them in the github, or email me at jujugoboom@gmail.com. Thanks for trying this out. I hope you find it as fun and interesting as I.
