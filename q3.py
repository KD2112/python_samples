class Person:
    def __init__(self, name, age):
        # self.per=(name,age)
        self.per={}
        self.per[name]=age
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

    def __str__(self):
        return f"{self.name} ({self.age} years old)"

class pop:
    def __init__(self):
        self.people=[]
    def add(self, person):
        self.people.append((person))

def main():
    p1 = Person("kalidas", 20)    # standalone
    p2 = Person("anakha", 19)     # standalone

    population = Pop()
    population.add(p1)           # reuse Person
    population.add(p2)

    print("Standalone person:")
    print(p1)

    print("\nPopulation:")
    print(population)


if __name__ == "__main__":
    main()
