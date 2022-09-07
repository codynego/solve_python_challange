"""
    Task no: Task 6
    Description: A program thats prints the remaining pizza slice
    a user has eaten
    Return: no return 
"""

total_slice = int(input("Whats the total slice of pizza?: "))
slice_eaten = int(input("how many slice have you eaten?: "))

rem_slice = total_slice - slice_eaten
print(f"You have {rem_slice} slice remaining")