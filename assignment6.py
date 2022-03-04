import random
#defining random function to generate random numbers
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
#here ans1 and ans2 are (gen1^x1)%mod and (gen2^x2)%mod
def collisionResistant(num1,num2):
    #generating a large prime of 64 bits
    mod = 11379284790137559833
    #its primitive roots
    gen1 = 3
    gen2 = 5
    x1 = num1
    x2 = num2
    ans1 = bin(pow(gen1, int(x1, 2), mod)).replace('0b', '')
    ans2 = bin(pow(gen2, int(x2, 2), mod)).replace('0b', '')
    #seeing if there bits are less than 64 if so prepand with 0
    if(len(ans1) < 64):
        ans1 = ans1.zfill(64)
    if(len(ans2) < 64):
        ans2 = ans2.zfill(64)
    #then xor that two valeus to find 64 bits and take mod
    ans = int(xor(ans1,ans2),2)%mod
    ans = bin(ans).replace("0b", "")
    if(len(ans)<64):
        ans = ans.zfill(64)
    return ans
x1 = rand_key(64)#64 bit 
x2 = rand_key(64)
#print(collisionResistant(x1,x2))