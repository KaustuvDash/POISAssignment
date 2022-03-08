import secrets
import random
moduls1 = 19
moduls2 = 29
generator1 = 2
generator2 = 2
def rand_key(p):
    key1 = ""
    for i in range(p):
        temp = str(random.randint(0, 1))
        key1 += temp
    return(key1)
def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    return ans
def functionH(firstHalf,secondHalf,flag,msglength):
    if flag==1:
        #first convert firstHalfBinary to  number
        n = int(firstHalf,2)
        #to cal g^x % mod and convert it to binaryString
        p = bin(pow(generator1,n,moduls1))
        p = p.replace('0b','')
        #now to fill the 0 from front
        fillSize = msglength - len(p)
        for i in range(fillSize):
            p = '0'+p
    else:
        #first convert firstHalfBinary to  number
        n = int(firstHalf,2)
        #to cal g^x % mod and convert it to binaryString
        p = bin(pow(generator2,n,moduls2))
        p = p.replace('0b','')
        #now to fill the 0 from front
        fillSize = msglength - len(p)
        for i in range(fillSize):
            p = '0'+p
    hard_core_bit = 0
    for i in range(len(firstHalf)):
        hard_core_bit = (hard_core_bit ^ (int(firstHalf[i]) & int(secondHalf[i]))) % 2
    return p + secondHalf + str(hard_core_bit)
def functionG(seed,flag,msglength):
    result=''
    binaryString = seed
    for i in range(64):#looping through length of seed size
        index = int(len(binaryString)/2)
        firstHalf = binaryString[:index]
        secondHalf = binaryString[index:]
        binaryString = functionH(firstHalf,secondHalf,flag,msglength) 
        result += binaryString[-1]#last bit
        binaryString = binaryString[:-1]#ignoring last bit
    return result
def pseudoFunction(message,key):
    for i in range(len(message)-1,-1,-1):
        if(message[i] == '0'):
            key = functionG(key,0,len(message))
            #len key should be equal to lenght of message
        else:
            key = functionG(key,1,len(message))
    return key
def calculateMAC(seedBinary,messagebinary):
    message = messagebinary
    #message = "10010101111001010111100000000000000000000000000000000000000000000000000000000000000000"
    seed = seedBinary
    msglength = len(message)
    result=""
    temp= bin(msglength).replace("0b", "")#convert that msglen to  binary
    result = pseudoFunction(temp,seed)#message seed
    result = result.zfill(64)
    for i in range(0,msglength,64):
        if(msglength-i) < 64:
            result = xor(result,message[i:i+64].zfill(64))
        else:
            result = xor(result,message[i:i+64])
        result = pseudoFunction(result, seed)
    return result
