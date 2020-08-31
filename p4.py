def check_divisible(x):
    for i in range(1,21):
        if (x%i) != 0:
            return False
    return True

prediction=1
while (check_divisible(prediction) == False):
        prediction+=1 # this while loop keep running and increment our prediction untill get true from check_divisible
print(prediction)
# works in 2 minuets
