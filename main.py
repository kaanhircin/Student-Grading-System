import pandas as pd

# Determine a lesson
lesson = input("\n" + "Lesson: ")

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
        letter_grade = 'Cc'
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

students = list()
control = 1

while control:
    
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
    
    students.append(student)

    # Check loop continuity
    control = int(input("\n" + "[Press '1' to Continue or Press '0' to Terminate]: "))
    if control == 0:
        break

print("\n", students)

# DataFrame creation
df = pd.read_excel("student_grading_system.xlsx")

my_columns = ['Name', 'Surname', 'Number', 'Grade', 'Letter Grade', 'Status', 'Lesson']
for student in students:
    df = df.append(
        {
            'Name': student["Name"],
            'Surname': student["Surname"],
            'Number': student["School number"],
            'Grade': student["Grade"],
            'Letter Grade': student["Letter grade"],
            'Status': student["Status"],
            'Lesson': student["Lesson"]
        },ignore_index = True
    )

print("\n", df)

df.to_excel("student_grading_system.xlsx")