seedSize=7
moduls = 929
generator1 = 159
generator2 = 234
def functionH(firstHalf,secondHalf,flag):
    if flag==1:
        #first convert firstHalfBinary to  number
        n = int(firstHalf,2)
        #to cal g^x % mod and convert it to binaryString
        p = bin(pow(generator1,n) % moduls)
        p = p.replace('0b','')
        #now to fill the 0 from front
        fillSize = seedSize - len(p)
        for i in range(fillSize):
            p = '0'+p
    else:
        #first convert firstHalfBinary to  number
        n = int(firstHalf,2)
        #to cal g^x % mod and convert it to binaryString
        p = bin(pow(generator2,n) % moduls)
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
message = input()
seed = input()
print(pseudoFunction(message,seed))


