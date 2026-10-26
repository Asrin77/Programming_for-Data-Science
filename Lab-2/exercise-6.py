#exercise 6

x = int(input("enter a number for count down: "))
if x > 0:
    countdown = x
    while countdown > 0:
        countdown -= 1
        print(countdown)
else:
    print("negative and 0 are not acceptable")