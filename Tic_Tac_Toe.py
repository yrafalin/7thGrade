import math
import random
import time

keepgoin = 'yes'
xwin = 0
owin = 0
currentplay = ''

def printboard():
    print(' ')
    print('       |     |')
    print('   {spot1} | {spot2} | {spot3}'.format(spot1 = spots[0], spot2 =
          spots[1], spot3 = spots[2]))
    print('       |     |')
    print('  TTTTTTTTTTTTTTTTT')
    print('       |     |')
    print('   {spot1} | {spot2} | {spot3}'.format(spot1 = spots[3], spot2 =
          spots[4], spot3 = spots[5]))
    print('       |     |')
    print('  TTTTTTTTTTTTTTTTT')
    print('       |     |')
    print('   {spot1} | {spot2} | {spot3}'.format(spot1 = spots[6], spot2 =
          spots[7], spot3 = spots[8]))
    print('       |     |')

def ifwon(spotis, player, add):
    global xwin
    global owin
    if spotis == 1:
        if spots[2] == spots[1] and spots[1] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[4] == spots[8] and spots[8] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[3] == spots[6] and spots[6] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
    if spotis == 2:
        if spots[2] == spots[0] and spots[0] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[4] == spots[7] and spots[7] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
    if spotis == 3:
        if spots[1] == spots[0] and spots[0] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[4] == spots[6] and spots[6] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[5] == spots[8] and spots[8] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
    if spotis == 4:
        if spots[0] == spots[6] and spots[6] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[4] == spots[5] and spots[5] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
    if spotis == 5:
        if spots[0] == spots[8] and spots[8] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[1] == spots[7] and spots[7] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[2] == spots[6] and spots[6] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[5] == spots[3] and spots[3] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
    if spotis == 6:
        if spots[4] == spots[3] and spots[3] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[2] == spots[8] and spots[8] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
    if spotis == 7:
        if spots[3] == spots[0] and spots[0] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[4] == spots[2] and spots[2] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[7] == spots[8] and spots[8] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
    if spotis == 8:
        if spots[1] == spots[4] and spots[4] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[6] == spots[8] and spots[8] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
    if spotis == 9:
        if spots[0] == spots[4] and spots[4] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[2] == spots[5] and spots[5] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
        if spots[6] == spots[7] and spots[7] == ' ' + player + ' ':
            if ' ' + player + ' ' == 'X':
                if add == 'yes':
                    xwin += 1
                return 1
            else:
                if add == 'yes':
                    owin += 1
                return 2
    return 0

def computerplay():
    global currentplay
    global spotnow
    emptycount = []
    count = 0
    dontdo = 0
    for thing in spots:
        if thing == '   ':
            emptycount.append(count)
        count += 1
    for nothing in emptycount:
        if dontdo == 0:
            if ifwon(nothing + 1, computer, 'no') == 1 or ifwon(nothing + 1, computer, 'no') == 2:
                spotnow = nothing + 1
                dontdo = 1
        if dontdo == 0:
            if ifwon(nothing + 1, player, 'no') == 1 or ifwon(nothing + 1, player, 'no') == 2:
                spotnow = nothing + 1
                dontdo = 1
    if dontdo == 0:
        spotnow = random.randrange(0, len(emptycount))
        while spots[spotnow - 1] != '   ':
            spotnow = random.randrange(0, len(emptycount))
    spots[spotnow] = ' ' + computer + ' '

def board_is_full():
  return (spots[0] is not '   ' and
    spots[1] is not '   ' and
    spots[2] is not '   ' and
    spots[3] is not '   ' and
    spots[4] is not '   ' and
    spots[5] is not '   ' and
    spots[6] is not '   ' and
    spots[7] is not '   ' and
    spots[8] is not '   ')


while True:
    spots = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']
    mode = input('Do you want to play another player, or AI? Write player or ai.\n')
    if mode == 'player':
        while keepgoin == 'yes':
            playfirst = random.randrange(1, 3)
            if playfirst == 1:
                playfirst = 'X'
                playsecond = 'O'
            else:
                playfirst = 'O'
                playsecond = 'X'
            currentplay = playfirst
            print('Decide who is X and who is O.')
            time.sleep(3)
            gofirst = '{go} goes first!'.format(go = playfirst)
            print(gofirst)
            printboard()
            spotnow = 0
            while (spots[0] == '   ' or
                   spots[1] == '   ' or
                   spots[2] == '   ' or
                   spots[3] == '   ' or
                   spots[4] == '   ' or
                   spots[5] == '   ' or
                   spots[6] == '   ' or
                   spots[7] == '   ' or
                   spots[8] == '   ') and ifwon(spotnow, currentplay, 'no') == 0:
                spotnow = int(input('What spot do you want?\n'))
                while spotnow > 9 or spots[spotnow - 1] is not '   ' or math.isnan(spotnow):
                    if math.isnan(spotnow):
                        if str(spotnow) == 'exit' or str(spotnow) == 'end':
                            break
                    else:
                        spotnow = int(input('There was an error. Choose a number again.\n'))
                spots[spotnow - 1] = ' ' + playfirst + ' '
                printboard()
                currentplay = playfirst

                if ifwon(spotnow, currentplay, 'no') == 0:
                    if (spots[0] == '   ' or
                        spots[1] == '   ' or
                        spots[2] == '   ' or
                        spots[3] == '   ' or
                        spots[4] == '   ' or
                        spots[5] == '   ' or
                        spots[6] == '   ' or
                        spots[7] == '   ' or
                        spots[8] == '   '):
                       spotnow = int(input('What spot do you want?\n'))
                       while spotnow > 9 or spots[spotnow - 1] is not '   ' or math.isnan(spotnow):
                           spotnow = int(input('There was an error. Choose a number again.\n'))
                       spots[spotnow - 1] = ' ' + playsecond + ' '
                       printboard()
                       currentplay = playsecond

                if (ifwon(spotnow, currentplay, 'no') is not 0) or (spots[0] is not
                    '   ' and
                    spots[1] is not '   ' and
                    spots[2] is not '   ' and
                    spots[3] is not '   ' and
                    spots[4] is not '   ' and
                    spots[5] is not '   ' and
                    spots[6] is not '   ' and
                    spots[7] is not '   ' and
                    spots[8] is not '   '):
                    wintime = 'X has won {firwin} times. O has won {secwin} times.'.format(firwin = xwin, secwin = owin)
                    print(wintime)
                    keepgoin = input('Do you want to keep playing?\n')
        else:
            break

    if mode == 'ai':
        while keepgoin == 'yes':
            spots = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']
            playfirst = random.randrange(1, 3)
            if playfirst == 1:
                playfirst = 'X'
                playsecond = 'O'
            else:
                playfirst = 'O'
                playsecond = 'X'
            letter = input('Do you want to be x or o?\n')
            if letter == 'x':
                if playfirst == 'X':
                    print('You go first.')
                    player = playfirst
                    computer = playsecond
                else:
                    print('You go second.')
                    player = playsecond
                    computer = playfirst
            elif letter == 'o':
                if playfirst == 'O':
                    print('You go first.')
                    player = playfirst
                    computer = playsecond
                else:
                    print('You go second.')
                    player = playsecond
                    computer = playfirst
            else:
                print('Please type correctly next time.')
                break
            currentplay = playsecond
            printboard()
            spotnow = 0
            while (spots[0] == '   ' or
                   spots[1] == '   ' or
                   spots[2] == '   ' or
                   spots[3] == '   ' or
                   spots[4] == '   ' or
                   spots[5] == '   ' or
                   spots[6] == '   ' or
                   spots[7] == '   ' or
                   spots[8] == '   ') and ifwon(spotnow, currentplay, 'no') == 0:
                if currentplay == player:
                    computerplay()
                    printboard()
                else:
                    spotnow = int(input('What spot do you want?\n'))
                    while spotnow > 9 or spots[spotnow - 1] is not '   ' or math.isnan(spotnow):
                        spotnow = int(input('There was an error. Choose a number again.\n'))
                    spots[spotnow - 1] = ' ' + playfirst + ' '
                    printboard()
                currentplay = playfirst

                if ifwon(spotnow, currentplay, 'no') == 0:
                    if (spots[0] == '   ' or
                        spots[1] == '   ' or
                        spots[2] == '   ' or
                        spots[3] == '   ' or
                        spots[4] == '   ' or
                        spots[5] == '   ' or
                        spots[6] == '   ' or
                        spots[7] == '   ' or
                        spots[8] == '   '):
                        if currentplay == player:
                            print('computer plays now')
                            computerplay()
                            printboard()
                        else:
                            print('player plays now')
                            spotnow = int(input('What spot do you want?\n'))
                            while spotnow > 9 or spots[spotnow - 1] is not '   ' or math.isnan(spotnow):
                                spotnow = int(input('There was an error. Choose a number again.\n'))
                            spots[spotnow - 1] = ' ' + playsecond + ' '
                            printboard()
                        currentplay = playsecond

            if (ifwon(spotnow, currentplay, 'no') is not 0) or (spots[0] is not
                '   ' and
                spots[1] is not '   ' and
                spots[2] is not '   ' and
                spots[3] is not '   ' and
                spots[4] is not '   ' and
                spots[5] is not '   ' and
                spots[6] is not '   ' and
                spots[7] is not '   ' and
                spots[8] is not '   '):
                print('Game is done. Check who won')
                winwin = ''
                print(ifwon(spotnow, currentplay, 'yes'))
                if currentplay == computer:
                    winwin = 'AI'
                else:
                    winwin = 'Player'
                print('The {winner} has won.'.format(winner = winwin))
                print('X has won {firwin} times. O has won {secwin} times.'.format(firwin = xwin, secwin = owin))
                keepgoin = input('Do you want to keep playing?\n')
        break
# Both modes work perfectly. :) ... 1 year later: NOT TRUE!
