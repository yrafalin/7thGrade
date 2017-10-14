numless = 1
total = 100
while numless <= 99:
    total *= 100 - numless
    numless += 1
total = str(total)
newtotal = 0
for letter in total:
    newtotal += int(letter)
print(newtotal)
