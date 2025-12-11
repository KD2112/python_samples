
class Box:

    def __init__(self,name=None,value=None):
        self.items=[]
        if name is not None and value is not None:
            self.items.append((name,value))
    def __bool__(self):
        return bool(self.items)

i1 = Box("apple", 20)
i2 = Box()

print(bool(i1))  # True
print(bool(i2))  # False
