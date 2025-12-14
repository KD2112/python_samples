def sum(num):
    sum=0
    for i in range(0,len(num)):
        sum=sum+num[i]
    return sum

nums=[1,2,3,4,5]

print(sum(nums))
