def dup_rm(nums):
    unique=[]
    for i in range(0,len(nums)):
        if nums[i] not in unique:
            unique.append(nums[i])
    return unique

numb=[1,2,3,4,4,5,5,6]
print(dup_rm(numb))
    
