class Animal:
    def __init__(self,name) -> None:
        self.name=name
    
    def make_sound(self):
        print('Animal Can Make Sound')

class cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('meu meu')

class dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('gheu gheu')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('bah bah')


don1=cat('value')
don1.make_sound()
don2=dog('all value')
don2.make_sound()
don3=Goat('LM')
don3.make_sound()

don4=Goat('na')
don4.make_sound()
Animals=[don1,don2, don3, don4]

#Here is the issue of this code can't debug
for animal in Animals:
    animal.make_sound()
    