no_to_use=("hi","bye","is")
def count(text):
    text.lower()
    freq={}
    for i in text.split():
        if i not in no_to_use:
            if i in freq :
                freq[i]+=1
            else:
                freq[i]=1
    sort_item=sorted(freq.items(),key=lambda item:item[1],reverse=True)
    return print(sort_item)
count("hi my name is kalidas kalidas")