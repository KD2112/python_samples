# zoo = ('python', 'elephant', 'penguin')

# for i in zoo:
#     print("animals in zoo","",i)

# new_zoo="snake","giraffe"

# for i in new_zoo:
#     print("new zoo",i)
    
# print("after add")

# new_zoo+=zoo

# for i in new_zoo:
#     print("added zoo",i)



ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

for i in ab:
    print("elements in ab",i,"val in ab",ab[i])

ad={
    'Kalidas': 'swaroop@swaroopch.com',
    'Anakha': 'larry@wall.org',
    'mittu': 'matz@ruby-lang.org',
    'tuttu': 'spammer@hotmail.com'
}

for i in ad:
    print("key=",i,"value=",ad[i])

print("after addin")

ab.update(ad)

print(ab)