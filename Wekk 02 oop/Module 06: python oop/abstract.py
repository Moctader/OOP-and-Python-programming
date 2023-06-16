from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod #decorator
    def eat(self):
        print('hello world')

    @abstractmethod
    def move(self):
        pass


class Monkey(Animal):

    def __init__(self, name) -> None:
        self.name='Monkey'
        super().__init__()

    def eat(self):
        print('Now ok')

    def move(self):
        print('all ok')

layka=Monkey('monkey')
layka.eat()

layka1=Monkey('value')
layka1.move()