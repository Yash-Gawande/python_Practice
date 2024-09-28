# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input(f"Enter the list {i+1} number "))
	# adding the element
	lst.append(ele)

print(lst)

for i in range(len(lst) - 1):  # iterate up to the second-to-last element
    if lst[i] + 1 == lst[i + 1] or lst[i] - 1 == lst[i + 1]:
        print("Correct")
        break  # exit the loop if we find a match
else:
    print("Wrong")
