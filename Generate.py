import hashlib
import base58
import serial
import qrcode
import ecdsa
import ecdsa.der
import ecdsa.util
port = raw_input("Please enter port Arduino is connected to: ")
ser = serial.Serial(port, 9600)
start = ser.readline()
hexstart = "80" + start[0:64]
bytehex = str(bytearray.fromhex(hexstart))
hash1 = hashlib.sha256(bytehex).hexdigest()
bytehex2 = str(bytearray.fromhex(hash1))
hash2 = hashlib.sha256(bytehex2).hexdigest()
checksum = hash2[0:8]
hexfinal = hexstart + checksum
unencoded_final = str(bytearray.fromhex(hexfinal))
encoded_final = base58.b58encode(unencoded_final)
print(encoded_final)
img = qrcode.make(encoded_final)
img.save("Key.png")
sk = ecdsa.SigningKey.from_string(start[0:64].decode('hex'), curve=ecdsa.SECP256k1)
vk = sk.verifying_key
publicKey = ('\04' + sk.verifying_key.to_string()).encode('hex')
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(hashlib.sha256(publicKey.decode('hex')).digest())
address = base58.b58encode_check(chr(0) + ripemd160.digest())
print(address)
img2 = qrcode.make(address)
img2.save("Address.png")