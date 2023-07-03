from school import School, classRoom, Subject
from Persons import Student, Teacher

def main():
    school=School('name of schooö', 'Uttrae')
    eight=classRoom('eight')
    school.add_classromm(eight)
    
    Nine=classRoom('Nine')
    school.add_classromm(Nine)
    
    Ten=classRoom('Ten')
    school.add_classromm(Ten)
   
    
    abul=Student('abir', eight)
    school.student_admission(abul)
    
    babul=Student('babul', eight)
    school.student_admission(babul)
    
    labul=Student('labir', eight)
    school.student_admission(labul)
    
    #Subjects
    physics_teacher=Teacher('Shahajahan')
    physics=Subject('physics', physics_teacher)
    eight.add_subject(physics)
    
    chemistry_teacher=Teacher('Haradhan Nag')
    chemistry=Subject('chemistry', chemistry_teacher)
    eight.add_subject(chemistry)
    
    Biology_teacher=Teacher('Ajmal sir')
    Biology=Subject('Biology', Biology_teacher)
    eight.add_subject(Biology)
    
    eight.take_semster_final()

    
    
    print(school)
    
    

if __name__=='__main__':
    main()