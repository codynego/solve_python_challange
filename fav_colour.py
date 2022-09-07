"""
    Task no: Task 10
    Description: A program thats prints a message when a user enters red
    as favourite colour
    Return: no return 
"""

favourite_colour = input("whats your favourite colour?: ")

if favourite_colour.lower() == "red":
    print("I like red too")
else:
    print(f"i dont like {favourite_colour}, i prefer red")