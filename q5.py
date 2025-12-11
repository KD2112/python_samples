class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        if not isinstance(other,Vector):
            raise TypeError("only vec can add")        
        return Vector(self.x+other.x,self.y+other.y)
    def __repr__(self):
        return f"vector({self.x,self.y})"
    def __mul__(self,other):
        if isinstance(other,Vector):
            raise TypeError("error vec to vec mul not supported")
        return Vector(self.x*other,self.y*other)
    def __rmul__(self,other):
        if isinstance(other,Vector):
            raise TypeError("error vec to vec mul not supported")
        return Vector(self.x*other,self.y*other)
def main():
    v1=Vector(10,20)
    v2=Vector(2,3)

    v3=v1+v2
    print(v3)
    v3=v3*v2
    print(v3)
    v3=3*v1
    print(v3)
if __name__=="__main__":
    main()