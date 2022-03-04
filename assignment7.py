import assignment6 as collision
intialSeed = collision.rand_key(64)
message = collision.rand_key(300)
msglength = len(message)
result=intialSeed
for i in range(0,msglength,64):
    #print(len(result))
    if(msglength-i) < 64:
        result = collision.collisionResistant(message[i:i+64].zfill(64),result)
    else:
        result = collision.collisionResistant(message[i:i+64],result)
print(result)
print(len(result))