numberat = 2

print('I will now print you Perfect Numbers.')
while 1 == 1:
    addto = 0
    factor = 1
    while factor != numberat:
        if numberat % factor == 0:
            addto += factor
        factor += 1
    if addto == numberat:
        print('Here is one: ', numberat)
    numberat += 1
