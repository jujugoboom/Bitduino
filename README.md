Bitduino
========

Generate Bitcoin Private Addresses Using Arduino

Setup
-----
1) Download all necesary files
2) Run Setup.sh if on Mac or linux or Setup.bat for Windows(not tested)
3) Copy the folder Entropy to your Arduino Libraries folder or in the Arduino IDE click sketch>import library>add library and find the True Random folder

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
This is a way to generate a Bitcoin private key which can then be used to send and recieve bitcoin. This way is not entirely secure. I would recomend using a computer that has never touched the internet or a raspberry pi that has never touched the internet. If anyone gets your private key they also get full control of your bitcoins. 

Disclaimer
----------
This is my first bitcoin code and I am new to python.

Update
------
Now using the Entropy library on Arduinos that support it (i.e. Arduino Uno and newer Arduino Megas). This library is tested to be random. It is useful in cryptographic situations, such as this one. If you find a better way, post on the forum, reddit link, or email me at jujugoboom@gmail.com. 
 
-------------------------------------------------------------------------------------------------------------------

If you have any questions or suggestions, please feel free to leave them in the github, or email me at jujugoboom@gmail.com. Thanks for trying this out. I hope you find it as fun and interesting as I.
