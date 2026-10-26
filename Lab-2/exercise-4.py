#exercise 4

def calculate_grade(marks):
    average = sum(marks)/len(marks)
    print("average: ", average)

    if average >= 80:
        return "A"
    elif average >= 70 and average <80:
        return "B"
    elif average >=60 and average <70:
        return "C"
    elif average >= 50 and average < 60:
        return "D"
    else:
        return "F"

marks = [89, 90, 78, 86, 65.5]
print(calculate_grade(marks))