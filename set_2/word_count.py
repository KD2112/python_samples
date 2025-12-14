def count(nums):
    num_count={}

    for i in nums:
        num_count[i]=num_count.get(i,0)+1
    top=max(num_count.items(),key=lambda x: x[0])
    print(top)



numbers=[2,3,4,4,4,4,5,5]

count(numbers)

# print(num_count)