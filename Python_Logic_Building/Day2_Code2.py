
# Find the Duplicate Characters in the string

text = input("Enter the Text ")

print("The Duplicated characters in the Text ")
for i in range(0, len(text)):
    count =1
    for j in range(i+1, len(text)):
        if(text[i] == text[j] and text[i] != " "):
            count +=1

            text = text[:j] + '0' + text[j+1:]

    if (count > 1 and text[i] != '0'):
        print(text[i],end=" ")