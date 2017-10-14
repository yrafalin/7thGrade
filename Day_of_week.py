import math
print('Give me a date and I will tell you what day of the week it is.')

addup = -1
while addup == -1:
    month = str(input('What month? '))
    day = str(input('What day of the month? '))
    year = str(input('What year (after 1700)? '))
    if month == 'january' or month == 'october' or month == '1' or month == '10':
        addup = 6
    elif month == 'april' or month == 'july' or month == '4' or month == '7':
        addup = 5
    elif month == 'september' or month == 'december' or month == '9' or month == '12':
        addup = 4
    elif month == 'february' or month == 'march' or month == 'november' or month == '2' or month == '3' or month == '11':
        addup = 2
    elif month == 'may' or month == '5':
        addup = 0
    elif month == 'june' or month == '6':
        addup = 3
    elif month == 'august' or month == '8':
        addup = 1
    else:
        print('There was a mispelling. Please restart the program.')

addup += int(day)

loop = 1
last2years = ''
for letter in year:
    if loop >= len(year) - 1:
        last2years += letter
    loop += 1
last2years = int(last2years)

loop = 1
centuries = ''
for letter in year:
    if loop < 3:
        centuries += letter
        loop += 1
centuries = eval(centuries)

year = eval(year)
if (year % 400 == 0 or last2years % 4 == 0) and (month == 'january' or month == 'october'):
    addup -= 1

if centuries >= 20 and centuries <= 23:
    addup += last2years % 7
    addup += math.floor(last2years / 4)
elif centuries >= 16 and centuries <= 19:
    addup += last2years % 7
    addup += math.floor(last2years / 4)
    addup += 1
elif centuries >= 24 and centuries <= 27:
    addup += last2years % 7
    addup += math.floor(last2years / 4)
    addup += 6

if addup % 7 == 0:
    print('Your date is Sunday.')
elif addup % 7 == 1:
    print('Your date is Monday.')
elif addup % 7 == 2:
    print('Your date is Tuesday.')
elif addup % 7 == 3:
    print('Your date is Wednesday.')
elif addup % 7 == 4:
    print('Your date is Thursday.')
elif addup % 7 == 5:
    print('Your date is Friday.')
elif addup % 7 == 6:
    print('Your date is Saturday.')
