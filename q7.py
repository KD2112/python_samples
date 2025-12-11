text="Hi im kalidas kalidas"
splitted=text.split()
print(splitted)

count={}

for i in splitted:
    count[i]=count.get(i,0)+1
print(count)

sort_freq=dict(sorted(count.items(),key=lambda x:x[1],reverse=True))
print(sort_freq)

kalidas=[]

kalidas.append((10,20))
kalidas.append((2, 3))
kalidas.append((3, 10))

print(kalidas)

print(kalidas[0][1])

kalidas_dict=dict(kalidas)
# for i,pair in enumerate(kalidas):
#     kalidas_dict[i]=pair
print(kalidas_dict)