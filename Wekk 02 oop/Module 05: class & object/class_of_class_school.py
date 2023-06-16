class Student:
    def __init__(self, name, current_class, id):
        self.name=name
        self.current_class=current_class
        self.id=id

    def __repr__(self) -> str:
        return f'student  {self.name}, {self.current_class}, {self.id}'
    

class Teacher:
    def __init__(self, name, subject ,id):
        self.name=name
        self.subject=subject
        self.id=id

    def __repr__(self) -> str:
        return f'techers {self.name}, {self.subject},{self.id}'


class School:
    def __init__ (self, name):
        self.name=name
        self.teachers=[]
        self.students=[]

    def add_techer(self, name, subject):
        id=len(self.teachers)+101
        teacher=Teacher(name, id, subject)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee<6500:
            return 'please deposit fee'
        else:
            id=len(self.students)+1
            student=Student(name,'C', id)
            self.students.append(student)

    def __repr__(self) -> str:
        print('Welcome to ', self.name)
        print('-------Our Teachers---------')
        for teacher in self.teachers:
            print(teacher)
        
        print('---------Our Students----------')
        for student in self.students:
            print(student)
        return 'all done'
# st=Student('al', 9, 1)
# print(st)

# te=Teacher('Te', 'c', 3)
# print(te)

phitron=School('phitron')
phitron.enroll('a', 5200)
phitron.enroll('b', 8000)
phitron.enroll('c', 7000)
phitron.enroll('D', 90000)

phitron.add_techer('Tom Cruse', 'algo')
phitron.add_techer('dynamic', 'DS')
print(phitron)