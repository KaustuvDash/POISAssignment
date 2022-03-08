from assignment4 import calculateMAC
from assignment3 import calculateCPA,rand_key
#lets generate 300 bit message 
message = rand_key(300)
print("enter the seed")
seedValue = input()
cpa = calculateCPA(seedValue, message)
mac = calculateMAC(seedValue, message)
print(cpa)
print(mac)
