import pandas as pd

"""
Grade range:
90-100  AA Pass
85-89   BA Pass
80-84   BB Pass
70-79   CB Pass
60-69   CC Pass
50-59   DC Conditional Pass
45-49   DD Conditional Pass
40-44   FD Fail
0-39    FF Fail
"""

# Determine student letter grade and status
def set_student_status(grade):
    
    if grade >= 90:
        letter_grade = 'AA'
        status = 'Pass'
    elif grade>= 85 and grade <= 89:
        letter_grade = 'BA'
        status = 'Pass'
    elif grade >= 80 and grade <= 84:
        letter_grade = 'BB'
        status = 'Pass'
    elif grade >= 70 and grade <= 79:
        letter_grade = 'CB'
        status = 'Pass'
    elif grade >= 60 and grade <= 69:
        letter_grade = 'CC'
        status = 'Pass'
    elif grade >= 50 and grade <= 59:
        letter_grade = 'DC'
        status = 'Conditional Pass'
    elif grade >= 45 and grade <= 49:
        letter_grade = 'DD'
        status = 'Conditional Pass'
    elif grade >= 40 and grade <= 44:
        letter_grade = 'FD'
        status = 'Fail'
    elif grade <= 39:
        letter_grade = 'FF'
        status = 'Fail'
    
    return letter_grade, status

class Student():
    
    def __init__(self, name, surname, school_number, grade, letter_grade, lesson, status):
        self.name = name
        self.surname = surname
        self.school_number = school_number
        self.grade = grade
        self.letter_grade = letter_grade
        self.lesson = lesson
        self.status = status
    
    """
    # For print test
    def info(self):
        return self.name, self.surname, self.school_number, self.grade, self.letter_grade, self.lesson, self.status
    """

# Determine a lesson
lesson = input("\n" + "Lesson: ")

students = list()
students_index = 0
control = 1

while True:
    
    # Created using the class / Usage with class
    if control == 1:
        student_name = input("\n" + "Name: ")
        student_surname = input("Surname: ")
        student_school_number = input("School number: ")
        student_grade = int(input("Grade: "))
        
        student_letter_grade, student_status = set_student_status(student_grade)
        student_temp = Student(student_name, student_surname, student_school_number, student_grade, student_letter_grade, lesson, student_status)
        students.insert(students_index, student_temp)
        students_index += 1
        control = int(input("\n" + "[Press '1' to Continue or Press '0' to Terminate]: "))
    else:
        break
    
    """
    # Usage with Dictionary
    student = {
        "Name": "",
        "Surname": "",
        "School number": "",
        "Grade": 0,
        "Letter grade": "",
        "Lesson": "",
        "Status": ""
    }
    
    student["Name"] = input("\n" + "Name: ")
    student["Surname"] = input("Surname: ")
    student["School number"] = input("School number: ")
    student["Grade"] = int(input("Grade: "))
    student["Lesson"] = lesson
    
    student["Letter grade"], student["Status"] = set_student_status(student["Grade"])

    # Check loop continuity
    control = int(input("\n" + "[Press '1' to Continue or Press '0' to Terminate]: "))
    if control == 0:
        break
    """

print("\n", students)

# DataFrame creation
my_columns = ['Name', 'Surname', 'Number', 'Grade', 'Letter Grade', 'Status', 'Lesson']
df = pd.DataFrame(columns = my_columns)

for student in students:
    df = df.append(
        {
            'Name': student.name,
            'Surname': student.surname,
            'Number': student.school_number,
            'Grade': student.grade,
            'Letter Grade': student.letter_grade,
            'Status': student.status,
            'Lesson': student.lesson
        }, ignore_index = True
    )

print("\n", df)

# DataFrame to Excel
df.to_excel("student_grading_system.xlsx")