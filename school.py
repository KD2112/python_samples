class Schoolmem:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class teacher(Schoolmem):
    
    def __init__(self,name,age,salary):
        Schoolmem.__init__(self,name,age)
        self.salary=salary
    