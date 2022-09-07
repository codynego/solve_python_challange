"""
    Task no: Task 12
    Description: A program thats joins 2 string thne display the string plus the lenght
    Return: no return 
"""

first_name = input("enter your first name: ")
surname = input("enter your surname: ")

full_name = first_name + " " + surname
len = 0

for i in full_name:
    len += 1
print(f"your full name is {full_name}")
print(f"lenght of full_name is {len} ")