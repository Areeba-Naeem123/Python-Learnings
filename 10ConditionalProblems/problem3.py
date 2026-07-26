def grades(marks):
    if marks>=90 and marks <=100:
        grade="A"
    elif marks>=80 and marks <90:
        grade="B"
    elif marks >=70 and marks <80:
        grade="C"
    elif marks >=60 and marks <70:
        grade="D"
    elif marks <60:
        grade="F"
    return grade


studentsMarks = int(input("Enter your marks :"))
grade=grades(studentsMarks)
print (f"your grade is {grade}")
