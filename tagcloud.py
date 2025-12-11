class TagCloud:
    def __init__(self):
        self.tag={}
    def add(self,tag):
        tag=tag.lower()
        self.tag[tag]=self.tag.get(tag,0)+1
    def __repr__(self):
        return f"tags={self.tag}"
    def __str__(self):
        return f"user not dev"
    def __iter__(self):
        return iter(self.tag)
    def __getitem__(self,key):
        return self.tag.get(key.lower(),0)

def main():
    count=TagCloud()
    bad_words=('hi','is',"was",'the')
    text="hi my name is kalidas kalidas"
    for i in text.split():
           if i not in bad_words:
            count.add(i)
    print(repr(count))
    print(count["kalidas"])
if __name__=="__main__":
    main()