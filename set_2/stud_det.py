student={}
name=["kalidas","anakha","mittu","tuttu"]
mark=[1,100,10,150]
for i,j in zip(name,mark):
    student[i]=j

print(student)
def highest_score(stud):
    largest=0
    name=""
    for i in stud:
        if stud[i]>largest:
            name=i
            largest=stud[i]
    print(name)                     
    print(largest)

highest_score(student)