# write a python program to count vowels and consonant in the string

string1 = input("Enter a String ")

string1 = string1.lower()
vowel = 0
consonant = 0

for i in string1:
    if i in ("a","e","i","o","u"):
        vowel+=1
    elif i.isalpha():
        consonant+=1
print(f"Vowels in the String are {vowel} & Consonants in the String are {consonant}")