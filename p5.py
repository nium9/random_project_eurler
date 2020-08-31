def check_prime(x):
    for i in range (2,x//2):
        if (x%i==0): # we check the prime by halfing our prediction and then check from 0 - our prediction/2
                    #and if it a factor of thr prediction we know it not prime
            return False
    return True

prediction=0
term=1
while(True):
    if (term==10001 and check_prime(prediction)):
        break
    if prediction%2 !=0: # since we know a prime can't be divisiable by 2 we can use this to filter out prediction ie we are looking at only odd numbers
                            # in the check prime method
        if (check_prime(prediction)==True):
                term+=1
    prediction+=1

    # print ("prediction {} - term - {} - isPrime -{} " .format(prediction,term , check_prime(prediction)))
print(prediction)
# takes around a 1/2 a min
