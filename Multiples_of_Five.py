numberat = 3
numbers = []
while numberat < 1000:
	if numberat % 3 == 0:
		numbers.append(numberat)
	elif numberat % 5 == 0:
		numbers.append(numberat)
	numberat += 1

addto = 0
for object1 in numbers:
	addto += object1
print(addto)
