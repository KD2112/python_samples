import math

class Vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return f'vector({self.x},{self.y})'
    def __abs__(self):
        return math.hypot(self.x,self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self,other):
        x=self.x+other.x
        y = self.y + other.y
        return Vector(x, y)
    def __mul__(self, other):
        if isinstance(other,(int,float)):
            return Vector(self.x*other,self.y*other)
        elif isinstance(other,Vector):
            return self.x*other.x+self.y*other.y

v=Vector(0,0)
print(v)

b=Vector(2,5)
kalidas=list(("kalidas","tuttu","anakha"))
print(kalidas)
c=v*b
print(c)

# kalidas=tuple("kalidas")
# print(kalidas)

kalidas=("kalidas")
print(kalidas)

if v:
    print("true")