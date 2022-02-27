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

msglength = len(message)# msglen=1000 
result=""
temp= bin(msglength).replace("0b", "")#convert that msglen to  binary
result = pseudoFunction(temp,seed)#message seed
for i in range(0,msglength,256):
    result = bin(int(result) ^ int(message[i:i+255])).replace("0b","")
    result = pseudoFunction(str(result), seed)
print(result)
#left out string after dividing them in 256 blocks
result = bin(int(result) ^ int(message[i:len(message)-1])).replace("0b","")
result = pseudoFunction(str(result), seed)
print(result)
