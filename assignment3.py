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
#message =  str(secrets.randbits(1000))#1010 #randomness increase 
print("enter seed")
seed = input()
# print("enter message")
message = rand_key(192)
counter = secrets.randbits(64)#gives a number which binary conversion is 10 bits 
counter = bin(counter).replace("0b", "")#convert that 10 bits to binary

def incrementCounterOne(cntr):
   return bin(int(cntr)+1).replace("0b","")
i=0
msglength = len(message)#200
res=""
temp=0
accountLength  = len(counter)
for i in range(0,msglength,64):
    out = pseudoFunction(counter, seed)#,seed
    #64 bit output
    if(len(out)>64):#if output length greater than 256 take first take 256 bits
        out = out[0:64]
    else:
        out = out.zfill(64)#else prepand 0 

    counter = incrementCounterOne(counter)

    if(msglength < 64):
        # temp = int(out) ^ int(message[i:i+64-1])
        temp = xor(out,message[i:i+64-1])
    else:
        temp = xor(out,message[i:i+64]) 
        print(temp)

    temp = temp.zfill(64)
    # print("temp len",len(temp))
    res += str(temp)
    # print("res len",len(res))
print(res)