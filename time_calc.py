"""
    Task no: Task 8
    Description: A program that prints the number of hours,minutes and seconds
    are present in a given day
    Return: no return 
"""

days = int(input("enter the number of days: "))
hours = days * 24
minutes = (days * 24) * 60
seconds = ((days * 24) * 60) * 60

print(f"in {days} Days, there are: ")
print(f"{hours} hours")
print(f"{minutes} minutes")
print(f"{seconds} seconds")