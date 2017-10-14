numberat = 2
addto = 0
factor = 1

while 1 == 1:
    addto = 0
    factor = 1
    while factor != numberat:
        if numberat % factor == 0:
            addto += factor
        factor += 1
    if addto == (numberat * 2):
        print('Here is one: ', numberat)
    #print(numberat)
    numberat += 1
