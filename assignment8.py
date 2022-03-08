from assignment6 import collisionResistant,xor,rand_key
ipad = "0011011000110110001101100011011000110110001101100011011000110110"
opad = "0101110001011100010111000101110001011100010111000101110001011100"
#generate 64 bit key
key = rand_key(64)
print("key",key)
randomNumber = rand_key(64)
print("random number",randomNumber)
key1 = xor(ipad,key)
#let message is 300 bits
message = rand_key(300)
msglength = len(message)
propagateVal1 = collisionResistant(key1,randomNumber)
for i in range(0,msglength,64):
    if(msglength- i >= 64):
        propagateVal1 = collisionResistant(message[i:i+64],propagateVal1)
    else:
        propagateVal1 = collisionResistant(message[i:msglength-1].zfill(64),propagateVal1)

key2 = xor(opad,key)
propagateVal2 = collisionResistant(key2,randomNumber)
output = collisionResistant(propagateVal1, propagateVal2)
print(output)
print(len(output))