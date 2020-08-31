def check_palindrome(x):
    string=str(x)
    return string == string[::-1] #this check if the string is the same as reversed so it either return true or false

highest=0
for i in range(100,1000):
    for j in range(100,1000): # the 2 for loops go through all the possibiity of 3 digit number
        if (check_palindrome(i*j) == True) and i*j > highest: # it will then check if it a pallindrome which goes to the method
            highest=i*j
print(highest)
