class person:
    def __init__(self, name, height, weight) -> None:
        self.name=name
        self.height=height
        self.weight=weight

    def eat(self):
        print('something')
    
    def move(self):
        raise NotImplementedError
    

class cricketer(person):
    def __init__(self, name, height, weight, team) -> None:
        self.team=team
        super().__init__(name, height, weight)

    def eat(self):
        print('something to eat')
    
    def move(self):
        print('now ok')

    # + sign operator overload
    def __add__(self, other):
        return self.height+ other.height
    
    # * sign overload
    def __mul__(self, other):
        return self.height*other.height
    
    # len overload
    def __len__(self):
        return self.height
    
    # >sign overload
    def __gt__(self, other):
        return self.weight>other.weight

        
person=cricketer('s',64,30,'BD')
perons2=cricketer('m',40, 25, 'BD')
person.eat()
person.move()
print(person+perons2)
print(person*perons2)
print(len(person))
print(person<perons2)