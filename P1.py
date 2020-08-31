total=0
for i in range(1,1000): # this is done from 1 onwards as 0 is not natural
    if (i % 3==0 or i%5==0): # i check the modulus to see if they are multiple of each other.
        total+=i
print (total)
