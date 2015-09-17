#! python2

import hashlib
import base58
import serial
import qrcode
import ecdsa
import ecdsa.der
import ecdsa.util
import time

def privateKeyGenerator():
    hexstart = "80" + start[0:64]
    bytehex = str(bytearray.fromhex(hexstart))
    hash1 = hashlib.sha256(bytehex).hexdigest()
    bytehex2 = str(bytearray.fromhex(hash1))
    hash2 = hashlib.sha256(bytehex2).hexdigest()
    checksum = hash2[0:8]
    hexfinal = hexstart + checksum
    unencoded_final = str(bytearray.fromhex(hexfinal))
    encoded_final = base58.b58encode(unencoded_final)
    privFile = encoded_final[-8:]
    print("Private Key: " + encoded_final)
    img = qrcode.make(encoded_final)
    img.save("Key_" + privFile + ".png")
    return

def publicKeyGenerator():
    sk = ecdsa.SigningKey.from_string(start[0:64].decode('hex'), curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    publicKey = ('\04' + sk.verifying_key.to_string()).encode('hex')
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(publicKey.decode('hex')).digest())
    address = base58.b58encode_check(chr(0) + ripemd160.digest())
    print("Public Address: " + address)
    addrFile = address[-8:]
    img2 = qrcode.make(address)
    img2.save("Address_" + addrFile + ".png")

def read_selection():
    while True:
        selection = raw_input("Generate (Pri)vate Key or (Pub)lic Key or E(x)it: ")
        if selection.lower() == "pri":
            privateKeyGenerator()
        elif selection.lower() == "pub":
            publicKeyGenerator()
        elif selection.lower() == "x":
            break
        else:
            print("Please Choose Pri or Pub")

port = raw_input("Please enter port Arduino is connected to: ")
ser = serial.Serial(port, 9600)
while True:
    selection = raw_input("Do you want to (Gen)erate a new address or (Re)ad out an existing one or E(x)it: ")
    if selection.lower() == "gen":
        confirmation = raw_input("Are you sure? THIS WILL OVERWRITE ANY EXITSTING ADDRESS AND IT CAN NEVER EVER BE RECOVERED (Y/N): ")
        if confirmation.lower() == "y":
            ser.write(b'1')
            print("Generating...")
            ser.readline()
            print("Done")
            ser.close()
            ser.open()
        else:
            break
    elif selection.lower() == "re":
        ser.write(b'2')
        start = ser.readline()
        read_selection()
    elif selection.lower() == "x":
        break
    else:
        print("Please choose Gen or Re")


