seedSize=7
moduls = 929
generator = 159
def functionL(seedSize):
    return seedSize**2 - 2*seedSize +1
def functionH(firstHalf,secondHalf):
    #first convert firstHalfBinary to  number
    n = int(firstHalf,2)
    #to cal g^x % mod and convert it to binaryString
    p = bin(pow(generator,n) % moduls)
    p = p.replace('0b','')
    #now to fill the 0 from front
    fillSize = seedSize - len(p)
    for i in range(fillSize):
        p = '0'+p
    hard_core_bit = 0
    for i in range(len(firstHalf)):
        hard_core_bit = (hard_core_bit ^ (int(firstHalf[i]) & int(secondHalf[i]))) % 2
    return p + secondHalf + str(hard_core_bit)
def functionG(seed):
    result=''
    binaryString = seed
    for i in range(functionL(seedSize)):#looping functionL times
        index = int(len(binaryString)/2)
        firstHalf = binaryString[:index]
        secondHalf = binaryString[index:]
        binaryString = functionH(firstHalf,secondHalf) 
        result += binaryString[-1]#last bit
        binaryString = binaryString[:-1]#ignoring last bit
    return result
seed = input()
print(functionG(seed))


