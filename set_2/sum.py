
def sum(*num): '''------>the argument is returning a tuple 
            so it should be iterated for i in num'''
    sum=0
    for i in num:
        sum+=i
    print(sum)


sum(10,6)