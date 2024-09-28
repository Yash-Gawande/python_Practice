# Check Vowel or Consonant

# The Vowels in the English Alphabets are [A,E,I,O,U,]

check = input("Enter The Character ")

Vowels = ["A","E","I","O","U"]

check1 = check.upper()


if check1 in Vowels:
    print(f"{check} is Vowel ")
else:
    print(f"{check} is consonant")


# ------------------------------------------------------------

def CheckVowel(x):
    Vowels = ["A", "E", "I", "O", "U"]

    if x.upper() in Vowels:
        return f"{x} is Vowel"
    else:
        return f"{x} is consonant"

char = input("Enter The Character ")

print(CheckVowel(char))

