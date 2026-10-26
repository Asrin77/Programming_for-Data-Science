#exercise 7

students = [
    {"name": "Satoru", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Sasuke", "department": "CSE", "marks": 98, "attendance": 76},
    {"name": "Eren", "department": "DS", "marks": 91, "attendance": 95},
    {"name": "Tomoe", "department": "DS","marks": 87, "attendance": 84},
    {"name": "Yamada", "department": "CSE", "marks": 93, "attendance": 78}
    ]


# def student_info(name, mark):
#     print(f"Name: {name}")
#     print(f"Marks: {mark}")

def student_info (student):
    passed = 0
    failed = 0
    total = 0
    count = 0
    highest = 0
    top_student = ""
    for info in student:
        print(f"names: {info['name']} and mark: {info['marks']}")
        count += 1
        total += info['marks']

        if info['marks'] >= 50:
            passed += 1
        else:
            failed += 1

        if info['marks'] > highest:
            highest = info['marks']
            top_student = info['name']

    average = total / count

    print("passed: ", passed)
    print("failed: ", failed)
    print("average: ", average)
    print(f"{top_student} got highest mark {highest} ")

student_info(students)