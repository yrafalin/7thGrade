import math
import time
import random
'''
login = 0
guest = input('Do you want to log in, sign up, or play as a guest. Write login, signup, or guest.\n')
if guest == 'login' or guest == 'signup':
    users = open('usernames.txt', 'w+')
    passwords = open('passwords.txt', 'w+')
    moneysaves = open('moneysaves.txt', 'w+')
    if guest == 'login':
        username = input('What is your username?\n')
        password = input('What is your password?\n')
        lineis = 1
        for line in users:
            lineispass = 1
            for lines in passwords:
                if lineis == lineispass:
                    if line == (username + '\n') and lines == (password + '\n'):
                        login = 1
                lineispass += 1
            lineis += 1
        if login == 0:
            print("Error. Username and password don't match")
        users.seek(0, 0)
        linenum = 0
        stop = 0
        for line in users:
            if line == username + '\n':
                stop = 1
            if stop == 0:
                linenum += 1
        lineis = 1
        for line in moneysaves:
            if lineis == linenum:
                money = int(line)
        users.close()
        passwords.close()
    if guest == 'signup':
        signup = input('What do you want your username to be?\n')
        users.write(signup + '\n')
        yourpassword = input('What should your password be?\n')
        passwords.write(yourpassword + '\n')
        money = 1000
        users.seek(0, 0)
        linenums = users.readlines()
        linenum = len(linenums) - 1
        users.close()
        passwords.close()
if guest == guest:
    money = 1000

moneydoc = 0
yoav = input('Are you Yoav?\n')
if yoav == 'yes':
    moneydoc = open('moneysaves.txt', 'r+')
    moneydoc.seek(0, 0)
    moneylist = moneydoc.readlines()
    money = int((moneylist[-1])[:-2])
else:
    money = 1000'''
money = 1000

print('Blackjack pays 3:2. A win pays 1:1. Blackjack insurance pays 2:1.')
print('Dealer hits on soft 17s. Splitting allowed. Double downs only before split.')
print('Late surrenders allowed. Four decks in shoe.')
values = {'2 of <3': 2, '3 of <3': 3, '4 of <3': 4, '5 of <3': 5,
'6 of <3': 6, '7 of <3': 7, '8 of <3': 8, '9 of <3': 9,
'10 of <3 (10)': 10, 'jack of <3 (10)': 10, 'queen of <3 (10)': 10,
'king of <3 (10)': 10, 'ace of <3 (1, 11)': 0,
'2 of <>': 2, '3 of <>': 3, '4 of <>': 4, '5 of <>': 5,
'6 of <>': 6, '7 of <>': 7, '8 of <>': 8, '9 of <>': 9,
'10 of <> (10)': 10, 'jack of <> (10)': 10, 'queen of <> (10)': 10,
'king of <> (10)': 10, 'ace of <> (1, 11)': 0,
'2 of -8o': 2, '3 of -8o': 3, '4 of -8o': 4, '5 of -8o': 5,
'6 of -8o': 6, '7 of -8o': 7, '8 of -8o': 8, '9 of -8o': 9,
'10 of -8o (10)': 10, 'jack of -8o (10)': 10, 'queen of -8o (10)': 10,
'king of -8o (10)': 10, 'ace of -8o (1, 11)': 0,
'2 of ->': 2, '3 of ->': 3, '4 of ->': 4, '5 of ->': 5,
'6 of ->': 6, '7 of ->': 7, '8 of ->': 8, '9 of ->': 9,
'10 of -> (10)': 10, 'jack of -> (10)': 10, 'queen of -> (10)': 10,
'king of -> (10)': 10, 'ace of -> (1, 11)': 0}

acecount = 0
def total(currentplayer):
    global acecount
    total = 0
    for thing in currentplayer:
        for otherthing in values:
            if otherthing == thing:
                total += values[otherthing]
    for thing in currentplayer:
        if thing == 'ace of <3 (1, 11)':
            if total <= 10:
                total += 11
            else:
                total += 1
        elif thing == 'ace of -> (1, 11)':
            if total <= 10:
                total += 11
            else:
                total += 1
        elif thing == 'ace of -8o (1, 11)':
            if total <= 10:
                total += 11
            else:
                total += 1
        elif thing == 'ace of <> (1, 11)':
            if total <= 10:
                total += 11
            else:
                total += 1
        if total > 21:
            acecount = 0
            for thing in currentplayer:
                if thing[:3] == 'ace':
                    acecount += 1
        if acecount >= 2:
            if total - 10 <= 21:
                total -= 10
    return total

def hasace(currentplayer):
    #print('cheking has ace. checkig ', currentplayer[0], ' ', (currentplayer[0])[:3], ' or ', currentplayer[1], ' ', (currentplayer[1])[:3])
    if values[currentplayer[0]] == 0:
        return True
    elif values[currentplayer[1]] == 0:
        return True
    #print('no ace')
    return False

def hasface(currentplayer):
    #print('cheking has Face. checkig ', currentplayer[0], ' ', values[currentplayer[0]], ' or ', currentplayer[1], ' ', values[currentplayer[1]])
    if values[currentplayer[0]] == 10:
        return True
    elif values[currentplayer[1]] == 10:
        return True
    #print('no Face')
    return False

insurance = 0
keepgoin = 'yes'
while keepgoin == 'yes':
    deck = ['2 of <3', '3 of <3', '4 of <3', '5 of <3',
    '6 of <3', '7 of <3', '8 of <3', '9 of <3',
    '10 of <3 (10)', 'jack of <3 (10)', 'queen of <3 (10)',
    'king of <3 (10)', 'ace of <3 (1, 11)', '2 of <>',
    '3 of <>', '4 of <>', '5 of <>', '6 of <>',
    '7 of <>', '8 of <>', '9 of <>', '10 of <> (10)',
    'jack of <> (10)', 'queen of <> (10)', 'king of <> (10)',
    'ace of <> (1, 11)', '2 of -8o', '3 of -8o', '4 of -8o',
    '5 of -8o', '6 of -8o', '7 of -8o', '8 of -8o', '9 of -8o',
    '10 of -8o (10)', 'jack of -8o (10)', 'queen of -8o (10)',
    'king of -8o (10)', 'ace of -8o (1, 11)', '2 of ->', '3 of ->',
    '4 of ->', '5 of ->', '6 of ->', '7 of ->', '8 of ->',
    '9 of ->', '10 of -> (10)', 'jack of -> (10)',
    'queen of -> (10)', 'king of -> (10)', 'ace of -> (1, 11)',
    '2 of <3', '3 of <3', '4 of <3', '5 of <3',
    '6 of <3', '7 of <3', '8 of <3', '9 of <3',
    '10 of <3 (10)', 'jack of <3 (10)', 'queen of <3 (10)',
    'king of <3 (10)', 'ace of <3 (1, 11)', '2 of <>',
    '3 of <>', '4 of <>', '5 of <>', '6 of <>',
    '7 of <>', '8 of <>', '9 of <>', '10 of <> (10)',
    'jack of <> (10)', 'queen of <> (10)', 'king of <> (10)',
    'ace of <> (1, 11)', '2 of -8o', '3 of -8o', '4 of -8o',
    '5 of -8o', '6 of -8o', '7 of -8o', '8 of -8o', '9 of -8o',
    '10 of -8o (10)', 'jack of -8o (10)', 'queen of -8o (10)',
    'king of -8o (10)', 'ace of -8o (1, 11)', '2 of ->', '3 of ->',
    '4 of ->', '5 of ->', '6 of ->', '7 of ->', '8 of ->',
    '9 of ->', '10 of -> (10)', 'jack of -> (10)',
    'queen of -> (10)', 'king of -> (10)', 'ace of -> (1, 11)',
    '2 of <3', '3 of <3', '4 of <3', '5 of <3',
    '6 of <3', '7 of <3', '8 of <3', '9 of <3',
    '10 of <3 (10)', 'jack of <3 (10)', 'queen of <3 (10)',
    'king of <3 (10)', 'ace of <3 (1, 11)', '2 of <>',
    '3 of <>', '4 of <>', '5 of <>', '6 of <>',
    '7 of <>', '8 of <>', '9 of <>', '10 of <> (10)',
    'jack of <> (10)', 'queen of <> (10)', 'king of <> (10)',
    'ace of <> (1, 11)', '2 of -8o', '3 of -8o', '4 of -8o',
    '5 of -8o', '6 of -8o', '7 of -8o', '8 of -8o', '9 of -8o',
    '10 of -8o (10)', 'jack of -8o (10)', 'queen of -8o (10)',
    'king of -8o (10)', 'ace of -8o (1, 11)', '2 of ->', '3 of ->',
    '4 of ->', '5 of ->', '6 of ->', '7 of ->', '8 of ->',
    '9 of ->', '10 of -> (10)', 'jack of -> (10)',
    'queen of -> (10)', 'king of -> (10)', 'ace of -> (1, 11)',
    '2 of <3', '3 of <3', '4 of <3', '5 of <3',
    '6 of <3', '7 of <3', '8 of <3', '9 of <3',
    '10 of <3 (10)', 'jack of <3 (10)', 'queen of <3 (10)',
    'king of <3 (10)', 'ace of <3 (1, 11)', '2 of <>',
    '3 of <>', '4 of <>', '5 of <>', '6 of <>',
    '7 of <>', '8 of <>', '9 of <>', '10 of <> (10)',
    'jack of <> (10)', 'queen of <> (10)', 'king of <> (10)',
    'ace of <> (1, 11)', '2 of -8o', '3 of -8o', '4 of -8o',
    '5 of -8o', '6 of -8o', '7 of -8o', '8 of -8o', '9 of -8o',
    '10 of -8o (10)', 'jack of -8o (10)', 'queen of -8o (10)',
    'king of -8o (10)', 'ace of -8o (1, 11)', '2 of ->', '3 of ->',
    '4 of ->', '5 of ->', '6 of ->', '7 of ->', '8 of ->',
    '9 of ->', '10 of -> (10)', 'jack of -> (10)',
    'queen of -> (10)', 'king of -> (10)', 'ace of -> (1, 11)']
    print('You currently have ${money}.'.format(money = money))
    bet = int(input('How much do you bet.\n'))
    money -= bet
    if money < 0:
        print('Cheater! You have been ejected.')
        break
    print('Now, you currently have ${money}.'.format(money = money))
    player = [random.choice(deck)]
    deck.remove(player[-1])
    dealer = [random.choice(deck)]
    deck.remove(dealer[-1])
    player.append(random.choice(deck))
    deck.remove(player[-1])
    holecard = random.choice(deck)
    deck.remove(holecard)
    dealer.append(holecard)
    print('You have a {card1} and a {card2}.'.format(card1 = player[0],
                                                     card2 = player[1]))
    print('The Dealer has a {card1} and a Hole card.'.format(card1 = dealer[0]))

    if (dealer[0])[:3] == 'ace':
        yesinsure = input('Would you like to take out insurance against a Dealer Blackjack?\n')
        if yesinsure == 'yes':
            insurance = bet + 1
            while insurance > bet:
                insurance = int(input('How much is your insurance? It should be below your bet.\n'))
            money -= insurance
            if money < 0:
                print('Cheater! You have been ejected.')
                break
            print('You now have ${money}.'.format(money = money))

    dontdo = 0
    dontdo2 = 0
    bust = 0
    bust2 = 0
    nosplit = 0
    print('Your cards value is {value}.'.format(value = total(player)))
    if hasace(player) and hasface(player) :
        if not hasace(dealer) or not hasface(dealer):   #there is a bug here: doesn't tell me I got 21
            print('You got a Blackjack!')
            print('The Hole card is a {card}.'.format(card = holecard))
            money += (bet / 2) * 5
            print('You now have ${money}!'.format(money = money))
            keepgoin = input('Do you want to keep playing?\n')
        else:
            print('You got a Blackjack!')
            print('There is a push.')
            print('The Hole card is a {card}.'.format(card = holecard))
            money += bet
            money += (insurance * 3)
            print('You now have ${money}!'.format(money = money))
            keepgoin = input('Do you want to keep playing?\n')
    elif hasace(dealer) and hasface(dealer):
        print('The Hole card is a {card}.'.format(card = holecard))
        print('The opponent had a Blackjack!')
        money += (insurance * 3)
        print('You now have ${money}!'.format(money = money))
        keepgoin = input('Do you want to keep playing?\n')
    else:
        if values[player[0]] == values[player[1]]:
            splityes = input('Do you want to split?\n')
            if splityes == 'yes':
                nosplit = 1
                player2 = [player[-1]]
                player.remove(player[-1])
                player.append(random.choice(deck))
                deck.remove(player[-1])
                bet2 = bet
                money -= bet2
                if money < 0:
                    print('Cheater! You have been ejected.')
                    break
                print('Your first hand is a {card} and a {card2}. Its value is {value}.'.format(card = player[0], card2 = player[-1], value = total(player)))
                print('Your second hand is currently a {card}.'.format(card = player2[-1]))
        if nosplit == 1:
            while dontdo != 1:
                nextmove = input('First hand. Choose: hit, or stand.\n')
                while nextmove != 'hit' and nextmove != 'stand':
                    nextmove = input('Error. Choose: hit, stand, surrender, or double.\n')
                if nextmove == 'hit':
                    player.append(random.choice(deck))
                    deck.remove(player[-1])
                    print('Your first hand drew a {card1}. Its value is {value}.'.format(card1 = player[-1], value = total(player)))
                    dontdo = 2
                    if total(player) > 21:
                        print('Your first hand busted. You lose.')
                        bust = 1
                        bet = 0
                        dontdo = 1
                if nextmove == 'stand':
                    dontdo = 1
            while dontdo2 != 1:
                if len(player2) == 1:
                    player2.append(random.choice(deck))
                    deck.remove(player2[-1])
                    print('Your second hand drew a {card1}. Its value is {value}.'.format(card1 = player2[-1], value = total(player2)))
                nextmove = input('Second hand. Choose: hit, or stand.\n')
                while nextmove != 'hit' and nextmove != 'stand':
                    nextmove = input('Error. Choose: hit, stand, surrender, or double.\n')
                if nextmove == 'hit':
                    player2.append(random.choice(deck))
                    deck.remove(player2[-1])
                    print('Your second hand drew a {card1}. Its value is {value}.'.format(card1 = player2[-1], value = total(player2)))
                    dontdo = 2
                    if total(player2) > 21:
                        print('Your second hand busted. You lose.')
                        bust2 = 1
                        bet2 = 0
                        dontdo2 = 1
                if nextmove == 'stand':
                    dontdo2 = 1
        else:
            while dontdo != 1:
                if dontdo == 0:
                    nextmove = input('Choose: hit, stand, surrender, or double.\n')
                    while nextmove != 'hit' and nextmove != 'stand' and nextmove != 'double' and nextmove != 'surrender':
                        nextmove = input('Error. Choose: hit, stand, surrender, or double.\n')
                else:
                    nextmove = input('Choose: hit, or stand.\n')
                    while nextmove != 'hit' and nextmove != 'stand':
                        if nextmove == 'end' or nextmove == 'exit':
                            print('You fold.')
                            break
                        nextmove = input('Error. Choose: hit, or stand.\n')
                if nextmove == 'hit':
                    player.append(random.choice(deck))
                    deck.remove(player[-1])
                    print('You drew a {card1}. Your value is {value}.'.format(card1 = player[-1], value = total(player)))
                    dontdo = 2
                    if total(player) > 21:
                        print('You busted. You lose.')
                        bust = 1
                        bet = 0
                        dontdo = 1
                if nextmove == 'double':
                    money -= bet
                    if money < 0:
                        print('Cheater! You have been ejected.')
                        break
                    bet *= 2
                    player.append(random.choice(deck))
                    deck.remove(player[-1])
                    print('You drew a {card1}. Your total value is {total}.'.format(card1 = player[-1], total = total(player)))
                    dontdo = 1
                    if total(player) > 21:
                        print('You busted. You lose.')
                        bust = 1
                        bet = 0
                if nextmove == 'surrender':
                    money += (bet / 2)
                    bet = 0
                    print('You now have ${money}.'.format(money = money))
                    bust = 1
                    dontdo = 1
                if nextmove == 'stand':
                    dontdo = 1

        if nosplit == 1:
            if bust == 0 or bust2 == 0:
                holecard = random.choice(deck)
                deck.remove(holecard)
                dealer.append(holecard)
                print('The Dealer has a {card1}, and the Hole card is a {card2}.'.format(card1 = dealer[0], card2 = holecard))
                while total(dealer) <= 16 or (total(dealer) == 17 and hasace(dealer)):
                    dealer.append(random.choice(deck))
                    deck.remove(dealer[-1])
                    print('The Dealer drew a {card2}. They have {total}.'.format(card2 = dealer[-1], total = total(dealer)))
                    if total(dealer) > 21:
                        print('The Dealer busted. You win!')
                        if bust == 0:
                            money += bet * 2
                        if bust2 == 0:
                            money += bet2 * 2
                        print('You now have ${money}!'.format(money = money))
                        bust = 1
                if bust == 0:
                    if total(player) > total(dealer):
                        print('Your first hand won!')
                        money += bet * 2
                    elif total(player) == total(dealer):
                        print('Your first hand has a push.')
                        money += bet
                    else:
                        print('Your first hand lost.')
                        bet = 0
                if bust2 == 0:
                    if total(player2) > total(dealer):
                        print('Your second hand won!')
                        money += bet2 * 2
                        print('You now have ${money}!'.format(money = money))
                    elif total(player2) == total(dealer):
                        print('Your second hand has a push.')
                        money += bet2
                        print('You now have ${money}!'.format(money = money))
                    else:
                        print('Your second hand lost.')
                        bet2 = 0
                        print('You now have ${money}!'.format(money = money))
        elif bust == 0:
            print('The Dealer has a {card1}, and the Hole card is a {card2}.'.format(card1 = dealer[0], card2 = holecard))
            while total(dealer) <= 16:
                dealer.append(random.choice(deck))
                deck.remove(dealer[-1])
                print('The Dealer drew a {card2}. They have {total}.'.format(card2 = dealer[-1], total = total(dealer)))
                if total(dealer) > 21:
                    print('The Dealer busted. You win!')
                    money += bet * 2
                    print('You now have ${money}!'.format(money = money))
                    bust = 1
            if bust == 0:
                if total(player) > total(dealer):
                    print('You win!')
                    money += bet * 2
                    print('You now have ${money}!'.format(money = money))
                elif total(player) == total(dealer):
                    print('There is a push.')
                    money += bet
                    print('You now have ${money}!'.format(money = money))
                else:
                    print('You lost.')
                    bet = 0
                    print('You now have ${money}!'.format(money = money))

        keepgoin = input('Do you want to keep playing?\n')
'''if yoav == 'yes':
    moneydoc.write(str(money) + '\n')
    moneydoc.close()

lineis = 1
for line in moneysaves:
    if lineis == linenum:
        moneysaves.replace(line, str(money) + '\n')
    lineis += 1
moneysaves.close()
'''
