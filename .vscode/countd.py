direction = input("do you want to count up or down?: ").lower()
number = int(input("enter the number to count from: "))

if direction == "up":
    for i in range(1, number + 1):
        print(i)

elif direction == "down":
    for i in range(0, number):
        print(number - i)

else:
    print("invalid input")
