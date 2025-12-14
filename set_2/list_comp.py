# def sq_rt(nums):
#     sqrt=[]
#     for i in nums:
#         if i%3==0:
#             sqrt.append(i*i)
#     print(sqrt)
# nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# sq_rt(nums)
#  equivalent compr
sqrt_list=[i*i for i in range(1,20) if i%3==0]
print("sqr of number from 1-20 and  div by 3",sqrt_list)

only_even=[i for i in range(2,20,2)]
print("even no from 1-20",only_even)

text="sdfdsf65465465asfasdsd46564"
dig=[i for i in text if i.isdigit()]
print(dig)