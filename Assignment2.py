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
    for i in range(len(message)):#looping through length of seed size
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
message = rand_key(200)#10 #randomness increase 
seed = input()
print(len(pseudoFunction(message,seed)))#msg,key
#prf input n bit number output n bit number 

