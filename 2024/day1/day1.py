# readlines make the each line into string 
# e.g "99006   28305\n" To remove "\n" we need to use strip() in the loop 
# and s aved the data into the new list.
lines = [line.strip() for line in open("input.txt", "r").readlines()]

# Now let's separate the data and sort them
arr1 = []
arr2 = []

# Parse the file and populate arr1 and arr2
for i in lines:
    leftNum, rightNum = i.split("   ")
    arr1.append(int(leftNum))
    arr2.append(int(rightNum))



# Sort the arrays once
sortArr1 = sorted(arr1)
sortArr2 = sorted(arr2)

# Calculate the cost
i = 0
cost = 0
freq = 0
while i < len(sortArr1):  # Correct condition
    cost += abs(sortArr2[i] - sortArr1[i])
    freq += sortArr1[i] * (sum(sortArr1[i] ==k for k in sortArr2) )
    i += 1  # Increment index to avoid infinite loop

print(f"Part 1 answer Min cost: {cost} is the answer")
print(f"Part 2 Similar number: {freq} is the answer")
