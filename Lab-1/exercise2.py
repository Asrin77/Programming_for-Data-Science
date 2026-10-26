"""exercise 2"""
"""Input a student’s name, student ID, age, department, and CGPA. Display the information
as a formatted student profile."""

student_name = input("enter name: ")
student_ID = input("enter ID: ")
department = input("department: ")
cgpa = float(input("enter cgpa: "))

print("STUDENT INFORMATION \n")
print(f"NAME: {student_name.upper()}")
print(f"ID: {student_ID}")
print(f"DEPARTMENT: {department.upper()}")
print(f"CGPA: {cgpa}")