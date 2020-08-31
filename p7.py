array=[]
f=open("../tests/triangle.txt",'r')
line=f.readline()
while line:
    temp=[]
    for i in line.split(" "):
        temp.append(int(i))
    array.append(temp)
    line=f.readline()
f.close()
# the above is loading the file and storing in a 2d array/list
####################################
# print(array)
highest=0
total=0
################################################################################
## Greedy  not optimal
for i in range (0,len(array)):
    index=i
    for j in range(0,len(array[i])-1):
        value=j
        data=max(array[index][value+1], array[index][value])
        highest += data
print(highest)
################################################################################
#dynamic
memo=[-1 for i in range (len(array))]
memo[0]=array[0][0]
for a in range (1,len(memo)):
    for i in range (0,len(array)):
        index=i
        for j in range(0,len(array[i])-1):
            value=j
            temp= max(array[index][value+1], array[index][value])
            memo[a]= memo[a-1] + temp
            # highest += data
print(memo[len(memo)-1])
