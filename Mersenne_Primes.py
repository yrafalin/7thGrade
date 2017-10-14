numberat = 4
divideby = 2
print('I will now print you Marsenne Prime numbers.')
while 1 == 1:
    if (numberat - 1) % divideby == 0 or divideby == numberat - 1:
        if divideby == numberat - 1:
            print('Here is one:')
            print(numberat - 1)
        numberat *= 2
        divideby = 2
    else:
        divideby += 1
