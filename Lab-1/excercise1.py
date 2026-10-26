
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))


print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print("not possible" if b == 0 else f"Quotient: {a / b}")