import math
import random
import time

numplayer = int(input('How many players are there?\n'))
while type(numplayer) is not int:
    numplayer = int(input('Please put a positive whole number. How many players are there?\n'))
players = [0 for x in range(numplayer)]
playnum = 1
doitlist = ['1', '5', 't1', 't2', 't3', 't4', 't5', 't6', '3pair', '4ofakind', '5ofakind', '6ofakind', '6inarow', 'roll', 'done']
six = 0
five = 0
four = 0
three = 0
two = 0
one = 0
current = 0
dienums = []

def nofarkle():
    global six
    global five
    global four
    global three
    global two
    global one
    dielist = [six, four, three, two]
    stepdos = 0
    steptres = 0
    if one == 0 and five == 0:
        pass
    else:
        return True
    for thing in dielist:
        if thing < 3:
            stepdos = 1
    for thing in dielist:
        if thing < 2:
            steptres +=1
    if stepdos == 1 and steptres < 1:
        return False
        dielist = [one, two, three, four, five, six]
    else:
        return True
        dielist = [one, two, three, four, five, six]

def ifin(command):
    global current
    global dienums
    global six
    global five
    global four
    global three
    global two
    global one
    dielist = [one, two, three, four, five, six]
    if command == '5':
        if five >= 1:
            five -= 1
            current += 50
            dienums.remove(5)
            return True
        else:
            return False
    elif command == '1':
        if one >= 1:
            one -= 1
            current += 100
            dienums.remove(1)
            return True
        else:
            return False
    elif command == 't1':
        if one >= 3:
            one -= 3
            current += 300
            for i in range(3):
                dienums.remove(1)
            return True
        else:
            return False
    elif command == 't2':
        if two >= 3:
            two -= 3
            current += 200
            for i in range(3):
                dienums.remove(2)
            return True
        else:
            return False
    elif command == 't3':
        if three >= 3:
            three -= 3
            current += 300
            for i in range(3):
                dienums.remove(3)
            return True
        else:
            return False
    elif command == 't4':
        if four >= 3:
            four -= 3
            current += 400
            for i in range(3):
                dienums.remove(4)
            return True
        else:
            return False
    elif command == 't5':
        if five >= 3:
            five -= 3
            current += 500
            for i in range(3):
                dienums.remove(5)
            return True
        else:
            return False
    elif command == 't6':
        if six >= 3:
            six -= 3
            current += 600
            for i in range(3):
                dienums.remove(6)
            return True
        else:
            return False
    elif command == '4ofakind':
        if 4 in dielist or 5 in dielist or 6 in dielist:
            for thing in dielist:
                if thing == 6 or thing == 5 or thing == 4:
                    thing -= 4
            current += 1000
            return True
        else:
            return False
    elif command == '5ofakind':
        if 5 in dielist or 6 in dielist:
            for thing in dielist:
                if thing == 6 or thing == 5:
                    thing -= 5
            current += 2000
            return True
        else:
            return False
    elif command == '6ofakind':
        if 6 in dielist:
            for thing in dielist:
                if thing == 6:
                    thing -= 6
            current += 3000
            numvar = 1
            for i in range(6):
                c = dienums.count(numvar)
                numvar += 1
            return True
        else:
            return False
    elif command == '3pair':
        thingcount = 0
        for thing in dielist:
            if thing == 2:
                thingcount +=1
        if thingcount == 3:
            for thing in dielist:
                thing = 0
            current += 1500
            return True
        else:
            return False
    elif command == '6inarow':
        thingcount = 0
        for thing in dielist:
            if thing == 1:
                thingcount +=1
        if thingcount == 6:
            for thing in dielist:
                thing = 0
            current += 1500
            return True
        else:
            return False
    dielist = [one, two, three, four, five, six]

def farklenow():
    global current
    global dienums
    global six
    global five
    global four
    global three
    global two
    global one
    global players
    global playnum
    dice = 0
    doit = 'o'
    current = 0
    while doit != 'done':
        dienums = []
        doit = 'o'
        six = 0
        five = 0
        four = 0
        three = 0
        two = 0
        one = 0
        dielist = [one, two, three, four, five, six]
        if dice == 0:
            dice = 6
        print('Rolling ...')
        time.sleep(1.5)
        for _ in range(0, dice):
            dienums.append(random.randrange(1, 7))
            print(dienums)
            if dienums[-1] == 1:
                one += 1
            elif dienums[-1] == 2:
                two += 1
            elif dienums[-1] == 3:
                three += 1
            elif dienums[-1] == 4:
                four += 1
            elif dienums[-1] == 5:
                five += 1
            elif dienums[-1] == 6:
                six += 1
        while doit != 'done' and doit != 'roll':
            if nofarkle():
                doit = str(input('Type 1, 5, t1, t2, t3, t4, t5, t6, 3pair, '+
                '4ofakind, 5ofakind, 6ofakind, 6inarow, roll, or done.\n'))
                while doit not in doitlist:
                    doit = str(input('Type 1, 5, t1, t2, t3, t4, t5, t6, 3pair, '+
                    '4ofakind, 5ofakind, 6ofakind, 6inarow, roll, or done.\n'))
                if doit != 'done' and doit != 'roll':
                    if ifin(doit):
                        print('Great! You have gained {x} points this turn.'.format(x = current))
                six = 0
                five = 0
                four = 0
                three = 0
                two = 0
                one = 0
                for thing in dienums:
                    if thing == 1:
                        one += 1
                    elif thing == 2:
                        two += 1
                    elif thing == 3:
                        three += 1
                    elif thing == 4:
                        four += 1
                    elif thing == 5:
                        five += 1
                    elif thing == 6:
                        six += 1
                dielist = [one, two, three, four, five, six]
                totals = 0
                for thing in dielist:
                    totals += thing
                dice = totals
                print(doit)
                if totals == 0:
                    break
            else:
                doit = 'done'
                print('You got Farkled!')
                current = 0
    players[playnum -1] += current
    print('Congrats! You have {i} points now.'.format(i = players[playnum -1]))
    if playnum == numplayer:
        playnum = 0
    playnum += 1

def twonineninenine():
    cycle = 1
    for thing in players:
        if thing > 2999:
            winna = cycle
            return False
        cycle += 1
    return True

print('Whoever gets to 3000 first, wins.')
while twonineninenine():
    print('\nPlayer {go} is going now.'.format(go = playnum))
    farklenow()

print('\nHey look, player number {go} has won!'.format(go = winna))
