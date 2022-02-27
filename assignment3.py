import secrets
seedSize=15
moduls1 = 929
moduls2 = 719
generator1 = 234
generator2 = 557
def functionH(firstHalf,secondHalf,flag):
    if flag==1:
        #first convert firstHalfBinary to  number
        n = int(firstHalf,2)
        #to cal g^x % mod and convert it to binaryString
        p = bin(pow(generator1,n) % moduls1)
        p = p.replace('0b','')
        #now to fill the 0 from front
        fillSize = seedSize - len(p)
        for i in range(fillSize):
            p = '0'+p
    else:
        #first convert firstHalfBinary to  number
        n = int(firstHalf,2)
        #to cal g^x % mod and convert it to binaryString
        p = bin(pow(generator2,n) % moduls2)
        p = p.replace('0b','')
        #now to fill the 0 from front
        fillSize = seedSize - len(p)
        for i in range(fillSize):
            p = '0'+p
    hard_core_bit = 0
    for i in range(len(firstHalf)):
        hard_core_bit = (hard_core_bit ^ (int(firstHalf[i]) & int(secondHalf[i]))) % 2
    return p + secondHalf + str(hard_core_bit)
def functionG(seed,flag):
    result=''
    binaryString = seed
    for i in range(seedSize):#looping through length of seed size
        index = int(len(binaryString)/2)
        firstHalf = binaryString[:index]
        secondHalf = binaryString[index:]
        binaryString = functionH(firstHalf,secondHalf,flag) 
        result += binaryString[-1]#last bit
        binaryString = binaryString[:-1]#ignoring last bit
    return result
def pseudoFunction(message,key):
    for i in range(len(message)-1,-1,-1):
        if(message[i] == '0'):
            key = functionG(key,0)
        else:
            key = functionG(key,1)
    return key
message =  str(secrets.randbits(1000))#1010 #randomness increase 
seed = input()
counter = secrets.randbits(10)#10 bits 
counter = bin(counter).replace("0b", "")#convert that 10 bits to binary

def incrementCounterOne(cntr):
   return bin(int(cntr)+1).replace("0b","")
i=0
msglength = len(message)#1000
res=""
temp=0
for i in range(0,len(message),256):
    out = pseudoFunction(counter, seed)#message,seed
    if(len(out)>256):#if output length greater than 256 take first take 256 bits
        out = out[0:255]
    else:
        out = out.zfill(256)#else prepand 0 

    ctr = incrementCounterOne(counter)

    if(msglength < 256):
        temp = int(out) ^ int(message[i:i+msglength-1])
    else:
        temp = int(out) ^ int(message[i:i+255])

    temp = bin(temp).replace("0b", "")
    res += str(out)

print (res)