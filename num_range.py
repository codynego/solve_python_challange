"""
    Task no: Task 9
    Description: A program thats prints a message if a user enters
    a number within a range
    Return: no return 
"""

number = int(input("enter a number within 10 - 20: "))

if number >= 10 and number <= 20:
    print("Thank you!")
else:
    print("Incorrect Answer")