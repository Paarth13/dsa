class Person():
    def __init__(self,name,age) -> object:
        self.name=name
        self.age=int(age)
    def __repr__(self) -> str:
        return repr("".join(["Name is : ",self.name," Age is : ",str(self.age)]))
    
def main():
    person=Person("Paarth",25)
    print(person)
if __name__=="__main__":
    main()
