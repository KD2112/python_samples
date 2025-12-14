num=[1,2,3,4,5,6,7,23,23,2,3,2,444,5,555]
largest=0
for i in range(0,len(num)-1):
    if num[i]<num[i+1]:
        largest=num[i+1]

print("largest=",largest)