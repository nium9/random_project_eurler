first=1
second=2
even_total=0
while True:
    temp=first+second#perfroms the addition for the next term
    if second > 4000000:
        break
    if second%2==0: # check if the term is even
        even_total+=second #add it to the total
    first=second
    second=temp## switches the term

print (even_total)
