array=[[5,6,7,8,9,10,11],
[7,8,9,10,11,12,13],
[15,16,1,8,6,5,2],
[2,5,7,9,11,22,33]]
product=0
evensum=0
oddsum=0
for i in range(len(array)):
    for j in range(len(array[0])):
        if j%2==0:
            evensum+=array[i][j]
        else:
            oddsum+=array[i][j]
product=evensum*oddsum
print(product)