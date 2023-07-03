class School:
    def __init__(self, name, address) -> None:
        self.name=name
        self.address=address
        self.teachers={}
        self.classrooms={}
    
    def add_classromm(self, classroom):
        self.classrooms[classroom.name]=classroom
    
    def add_teacher(self, subject, teacher):
        self.teachers[subject]=teacher
    
    def student_admission(self, student):
        className=student.classroom.name
        if className in self.classrooms:
            self.classrooms[className].add_student(student)
        else:
            print(f'No classroom name as {className}')
            
            
    def __repr__(self) -> str:
        print('------------all classroom----------------')
        for key, value in self.classrooms.items():
            print(key)
        print("_________students____________")
        eight=self.classrooms['eight']
        for student in eight.students:
            print(student.name)

        print('__________Subjects--------------')
        for subject in eight.subjects:
            print(subject.name, subject.teacher.name)
        
        print('__________Student Exam Marks____________')
        # for key, value in eight.students[0].marks.items():
        #     print(key, value)
        
        for student in eight.students:
            for key, value in student.marks.items():
                print(student.name, key, value)
            print('_______student end______')
        
        #print(len(eight.students))
        return ' '
            
class classRoom:
    def __init__(self, name) -> None:
        self.name=name
        self.students=[]
        self.subjects=[]

        
    def add_student(self, student):
        serial_id=f'{self.name} - {len(self.students)+1}'
        student.id=serial_id 
        self.students.append(student)
    
    def add_subject(self, subject):
        self.subjects.append(subject)
        
    def take_semster_final(self):
        for subject in self.subjects:
            subject.exam(self.students)
            
        
    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'
    
    # TODO: get top student by grade
    def get_top_student(self):
        pass
            

class Subject:
    def __init__(self, name, teacher) -> None:
        self.name=name
        self.teacher=teacher
        self.max_marks=100
        self.pass_marks=30
        
    def exam(self, students):
        for student in students:
            mark=self.teacher.evaluate_exam()
            student.marks[self.name]=mark
        
        