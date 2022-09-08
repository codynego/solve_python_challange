"""
    Task no: Task 13
    Description: a simple fun program
    Return: no return 
"""

word = input("enter a word: ").lower()
vowel = ["a","e","i","o","u"]

if word[0] not in vowel:
    consonant_word = word[1:] + word[0] + "ay"
    print(consonant_word)

else:
    vowel_word = word + "way"
    print(vowel_word)