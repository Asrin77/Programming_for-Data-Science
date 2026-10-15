
# LAB-2 EXERCISE 1

data_processing = float(input("Enter your data processing grade: "))
pds = float(input("Enter your data PDS grade: "))
data_science = float(input("Enter your data science grade: "))
python = float(input("Enter your Python grade: "))

course_marks = [data_processing, pds, data_science, python]

total = 0
maximum = course_marks[0]
minimum = course_marks[0]

for mark in course_marks:
    total += mark

    if mark > maximum:
        maximum = mark

    if mark < minimum:
        minimum = mark

average_grade = total / len(course_marks)

passed = 0
failed = 0

for mark in course_marks:
    if mark >= 50:
        passed += 1
    else:
        failed += 1

print(f"Highest mark: {maximum}")
print(f"Lowest mark: {minimum}")
print(f"Average mark: {average_grade:.2f}")
print(f"Passed courses: {passed}")
print(f"Failed courses: {failed}")
