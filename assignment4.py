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
def functionH(firstHalf,secondHalf,flag):
    if flag==1:
        #first convert firstHalfBinary to  number
        n = int(firstHalf,2)
        #to cal g^x % mod and convert it to binaryString
        p = bin(pow(generator1,n,moduls1))
        p = p.replace('0b','')
        #now to fill the 0 from front
        #print(len(p))
        fillSize = len(message) - len(p)
        for i in range(fillSize):
            p = '0'+p
    else:
        #first convert firstHalfBinary to  number
        n = int(firstHalf,2)
        #to cal g^x % mod and convert it to binaryString
        p = bin(pow(generator2,n,moduls2))
        p = p.replace('0b','')
        #now to fill the 0 from front
        fillSize = len(message) - len(p)
        for i in range(fillSize):
            p = '0'+p
    hard_core_bit = 0
    for i in range(len(firstHalf)):
        hard_core_bit = (hard_core_bit ^ (int(firstHalf[i]) & int(secondHalf[i]))) % 2
    return p + secondHalf + str(hard_core_bit)
def functionG(seed,flag):
    result=''
    binaryString = seed
    for i in range(accountLength):#looping through length of seed size
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
            #len key should be equal to lenght of message
        else:
            key = functionG(key,1)
    return key
message = rand_key(300)#1010 #randomness increase 
seed = input()
msglength = len(message)
result=""
temp= bin(msglength).replace("0b", "")#convert that msglen to  binary
accountLength = len(temp)
result = pseudoFunction(temp,seed)#message seed
result = result.zfill(64)
for i in range(0,msglength,64):
    #print(len(result))
    if(msglength-i) < 64:
        #temp = xor(out,message[i:msglength-1].zfill(64))
        result = xor(result,message[i:i+64].zfill(64))
    else:
        #temp = xor(out,message[i:i+64]) 
        result = xor(result,message[i:i+64])
    #result = xor(result,message[i:i+64])
    #result = bin(int(result) ^ int(message[i:i+64])).replace("0b","")
    accountLength = len(result)
    result = pseudoFunction(result, seed)
    #print(result)

print(result)
