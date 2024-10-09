text = input("Enter the string ")
textlength = len(text)
for char in text:
	ascii = ord(char)
	print(char, "\t", ascii)
