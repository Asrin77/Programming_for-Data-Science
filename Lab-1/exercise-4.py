"""exercise 4"""

"""Input a student’s name and five course marks. Calculate the total, average, highest mark,
lowest mark, and number of passed courses. Display all results. A mark of 50 or higher is considered a
pass."""

Name = input("enter name: ")
Marks = []
for mark in range(1, 6):
    mark = float(input(f"enter mark {mark}: "))
    Marks.append(mark)
def course_calc(x):
    total = sum(x)
    print(f"total: {total}")
    avg = total / len(x)
    print(f"average: {avg:.2f}")
    highest_mark = max(x)
    print(f"highest mark:  {highest_mark}")
    lowest_mark = min(x)
    print(f"lowest mark: {lowest_mark}")


    for mark in x:
        if mark >= 50:
            print("passed")
        else:
            print("failed")
course_calc(Marks)
    

    