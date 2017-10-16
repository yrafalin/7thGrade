import math
import time
import random

money = 1000
print('Punto Banco rules. Tie bets pay 8:1.')
print('5 percent commission on winning Banker bets.')
print('You start out with ${money}.'.format(money = money))
values = {'2 of <3': 2, '3 of <3': 3, '4 of <3': 4, '5 of <3': 5,
'6 of <3': 6, '7 of <3': 7, '8 of <3': 8, '9 of <3': 9,
'10 of <3': 10, 'jack of <3': 10, 'queen of <3': 10,
'king of <3': 10, 'ace of <3': 1,
'2 of <>': 2, '3 of <>': 3, '4 of <>': 4, '5 of <>': 5,
'6 of <>': 6, '7 of <>': 7, '8 of <>': 8, '9 of <>': 9,
'10 of <>': 10, 'jack of <>': 10, 'queen of <>': 10,
'king of <>': 10, 'ace of <>': 1,
'2 of -3': 2, '3 of -3': 3, '4 of -3': 4, '5 of -3': 5,
'6 of -3': 6, '7 of -3': 7, '8 of -3': 8, '9 of -3': 9,
'10 of -3': 10, 'jack of -3': 10, 'queen of -3': 10,
'king of -3': 10, 'ace of -3': 1,
'2 of ->': 2, '3 of ->': 3, '4 of ->': 4, '5 of ->': 5,
'6 of ->': 6, '7 of ->': 7, '8 of ->': 8, '9 of ->': 9,
'10 of ->': 10, 'jack of ->': 10, 'queen of ->': 10,
'king of ->': 10, 'ace of ->': 1}

deck = []
def deckset():
    global deck
    deck = ['2 of <3', '3 of <3', '4 of <3', '5 of <3',
    '6 of <3', '7 of <3', '8 of <3', '9 of <3',
    '10 of <3', 'jack of <3', 'queen of <3',
    'king of <3', 'ace of <3', '2 of <>',
    '3 of <>', '4 of <>', '5 of <>', '6 of <>',
    '7 of <>', '8 of <>', '9 of <>', '10 of <>',
    'jack of <>', 'queen of <>', 'king of <>',
    'ace of <>', '2 of -3', '3 of -3', '4 of -3',
    '5 of -3', '6 of -3', '7 of -3', '8 of -3', '9 of -3',
    '10 of -3', 'jack of -3', 'queen of -3',
    'king of -3', 'ace of -3', '2 of ->', '3 of ->',
    '4 of ->', '5 of ->', '6 of ->', '7 of ->', '8 of ->',
    '9 of ->', '10 of ->', 'jack of ->',
    'queen of ->', 'king of ->', 'ace of ->',
    '2 of <3', '3 of <3', '4 of <3', '5 of <3',
    '6 of <3', '7 of <3', '8 of <3', '9 of <3',
    '10 of <3', 'jack of <3', 'queen of <3',
    'king of <3', 'ace of <3', '2 of <>',
    '3 of <>', '4 of <>', '5 of <>', '6 of <>',
    '7 of <>', '8 of <>', '9 of <>', '10 of <>',
    'jack of <>', 'queen of <>', 'king of <>',
    'ace of <>', '2 of -3', '3 of -3', '4 of -3',
    '5 of -3', '6 of -3', '7 of -3', '8 of -3', '9 of -3',
    '10 of -3', 'jack of -3', 'queen of -3',
    'king of -3', 'ace of -3', '2 of ->', '3 of ->',
    '4 of ->', '5 of ->', '6 of ->', '7 of ->', '8 of ->',
    '9 of ->', '10 of ->', 'jack of ->',
    'queen of ->', 'king of ->', 'ace of ->',
    '2 of <3', '3 of <3', '4 of <3', '5 of <3',
    '6 of <3', '7 of <3', '8 of <3', '9 of <3',
    '10 of <3', 'jack of <3', 'queen of <3',
    'king of <3', 'ace of <3', '2 of <>',
    '3 of <>', '4 of <>', '5 of <>', '6 of <>',
    '7 of <>', '8 of <>', '9 of <>', '10 of <>',
    'jack of <>', 'queen of <>', 'king of <>',
    'ace of <>', '2 of -3', '3 of -3', '4 of -3',
    '5 of -3', '6 of -3', '7 of -3', '8 of -3', '9 of -3',
    '10 of -3', 'jack of -3', 'queen of -3',
    'king of -3', 'ace of -3', '2 of ->', '3 of ->',
    '4 of ->', '5 of ->', '6 of ->', '7 of ->', '8 of ->',
    '9 of ->', '10 of ->', 'jack of ->',
    'queen of ->', 'king of ->', 'ace of ->',
    '2 of <3', '3 of <3', '4 of <3', '5 of <3',
    '6 of <3', '7 of <3', '8 of <3', '9 of <3',
    '10 of <3', 'jack of <3', 'queen of <3',
    'king of <3', 'ace of <3', '2 of <>',
    '3 of <>', '4 of <>', '5 of <>', '6 of <>',
    '7 of <>', '8 of <>', '9 of <>', '10 of <>',
    'jack of <>', 'queen of <>', 'king of <>',
    'ace of <>', '2 of -3', '3 of -3', '4 of -3',
    '5 of -3', '6 of -3', '7 of -3', '8 of -3', '9 of -3',
    '10 of -3', 'jack of -3', 'queen of -3',
    'king of -3', 'ace of -3', '2 of ->', '3 of ->',
    '4 of ->', '5 of ->', '6 of ->', '7 of ->', '8 of ->',
    '9 of ->', '10 of ->', 'jack of ->',
    'queen of ->', 'king of ->', 'ace of ->',
    '2 of <3', '3 of <3', '4 of <3', '5 of <3',
    '6 of <3', '7 of <3', '8 of <3', '9 of <3',
    '10 of <3', 'jack of <3', 'queen of <3',
    'king of <3', 'ace of <3', '2 of <>',
    '3 of <>', '4 of <>', '5 of <>', '6 of <>',
    '7 of <>', '8 of <>', '9 of <>', '10 of <>',
    'jack of <>', 'queen of <>', 'king of <>',
    'ace of <>', '2 of -3', '3 of -3', '4 of -3',
    '5 of -3', '6 of -3', '7 of -3', '8 of -3', '9 of -3',
    '10 of -3', 'jack of -3', 'queen of -3',
    'king of -3', 'ace of -3', '2 of ->', '3 of ->',
    '4 of ->', '5 of ->', '6 of ->', '7 of ->', '8 of ->',
    '9 of ->', '10 of ->', 'jack of ->',
    'queen of ->', 'king of ->', 'ace of ->',
    '2 of <3', '3 of <3', '4 of <3', '5 of <3',
    '6 of <3', '7 of <3', '8 of <3', '9 of <3',
    '10 of <3', 'jack of <3', 'queen of <3',
    'king of <3', 'ace of <3', '2 of <>',
    '3 of <>', '4 of <>', '5 of <>', '6 of <>',
    '7 of <>', '8 of <>', '9 of <>', '10 of <>',
    'jack of <>', 'queen of <>', 'king of <>',
    'ace of <>', '2 of -3', '3 of -3', '4 of -3',
    '5 of -3', '6 of -3', '7 of -3', '8 of -3', '9 of -3',
    '10 of -3', 'jack of -3', 'queen of -3',
    'king of -3', 'ace of -3', '2 of ->', '3 of ->',
    '4 of ->', '5 of ->', '6 of ->', '7 of ->', '8 of ->',
    '9 of ->', '10 of ->', 'jack of ->',
    'queen of ->', 'king of ->', 'ace of ->',
    '2 of <3', '3 of <3', '4 of <3', '5 of <3',
    '6 of <3', '7 of <3', '8 of <3', '9 of <3',
    '10 of <3', 'jack of <3', 'queen of <3',
    'king of <3', 'ace of <3', '2 of <>',
    '3 of <>', '4 of <>', '5 of <>', '6 of <>',
    '7 of <>', '8 of <>', '9 of <>', '10 of <>',
    'jack of <>', 'queen of <>', 'king of <>',
    'ace of <>', '2 of -3', '3 of -3', '4 of -3',
    '5 of -3', '6 of -3', '7 of -3', '8 of -3', '9 of -3',
    '10 of -3', 'jack of -3', 'queen of -3',
    'king of -3', 'ace of -3', '2 of ->', '3 of ->',
    '4 of ->', '5 of ->', '6 of ->', '7 of ->', '8 of ->',
    '9 of ->', '10 of ->', 'jack of ->',
    'queen of ->', 'king of ->', 'ace of ->',
    '2 of <3', '3 of <3', '4 of <3', '5 of <3',
    '6 of <3', '7 of <3', '8 of <3', '9 of <3',
    '10 of <3', 'jack of <3', 'queen of <3',
    'king of <3', 'ace of <3', '2 of <>',
    '3 of <>', '4 of <>', '5 of <>', '6 of <>',
    '7 of <>', '8 of <>', '9 of <>', '10 of <>',
    'jack of <>', 'queen of <>', 'king of <>',
    'ace of <>', '2 of -3', '3 of -3', '4 of -3',
    '5 of -3', '6 of -3', '7 of -3', '8 of -3', '9 of -3',
    '10 of -3', 'jack of -3', 'queen of -3',
    'king of -3', 'ace of -3', '2 of ->', '3 of ->',
    '4 of ->', '5 of ->', '6 of ->', '7 of ->', '8 of ->',
    '9 of ->', '10 of ->', 'jack of ->',
    'queen of ->', 'king of ->', 'ace of ->']

def total(currentplayer):
    total = 0
    for thing in currentplayer:
        for otherthing in values:
            if thing == otherthing:
                total += values[thing]
    total = total % 10
    return total

keepgoin = 'yes'
while keepgoin == 'yes':
    deckset()
    bet = input('Do you want to bet tie, banker, or player?\n')
    while bet != 'tie' and bet != 'banker' and bet != 'player':
        bet = input('Error. Do you want to bet tie, banker, or player?\n')
    betsum = int(input('How much do you want to bet?\n'))
    money -= betsum
    if money < 0:
        print('Cheater! You have been ejected.')
        break
    burn = [random.choice(deck)]            #}
    deck.remove(burn[-1])                   #}
    for num in range(1, values[burn[-1]] + 1):  #}  card burning mechanism
        burn.append(random.choice(deck))    #}
        deck.remove(burn[-1])               #}
    print(burn)
    print('{cards} cards were burned.'.format(cards = len(burn)))
    player = [random.choice(deck)]
    deck.remove(player[-1])
    banker = [random.choice(deck)]
    deck.remove(banker[-1])
    player.append(random.choice(deck))
    deck.remove(player[-1])
    banker.append(random.choice(deck))
    deck.remove(banker[-1])
    print('You have a {card1} and a {card2}. Your total is {total}.'.format(card1 = player[0],
                                                                            card2 = player[1],
                                                                            total = total(player)))
    print('The Banker has a {card1} and a {card2}. Their total is {total}.'.format(card1 = banker[0],
                                                                                   card2 = banker[1],
                                                                                   total = total(banker)))

    dontdo = 0
    draw = -1
    if total(player) == 8 or total(player) == 9 or total(banker) == 8 or total(banker) == 9:
        dontdo = 1
        print('The Banker or the player has a value of 8 or 9, so no one draws.')
    elif total(player) < 6:
        player.append(random.choice(deck))
        deck.remove(player[-1])
        draw = values[player[-1]]
        print('You drew a {card}. Your new total is {total}.'.format(card = player[-1], total = total(player)))
    else:
        print("Your value is over 5, so you don't draw.")

    if dontdo == 0:
        if draw == -1:
            if total(banker) < 6:
                banker.append(random.choice(deck))
                deck.remove(banker[-1])
                print('The Banker drew a {card}. Their new total is {total}.'.format(card = banker[-1],
                                                                                     total = total(banker)))
        else:
            if draw == 2 or draw == 3:
                if total(banker) < 5:
                    banker.append(random.choice(deck))
                    deck.remove(banker[-1])
                    print('The Banker drew a {card}. Their new total is {total}.'.format(card = banker[-1],
                                                                                         total = total(banker)))
            if draw == 4 or draw == 5:
                if total(banker) < 6:
                    banker.append(random.choice(deck))
                    deck.remove(banker[-1])
                    print('The Banker drew a {card}. Their new total is {total}.'.format(card = banker[-1],
                                                                                         total = total(banker)))
            if draw == 6 or draw == 7:
                if total(banker) < 7:
                    banker.append(random.choice(deck))
                    deck.remove(banker[-1])
                    print('The Banker drew a {card}. Their new total is {total}.'.format(card = banker[-1],
                                                                                         total = total(banker)))
            if draw == 8:
                if total(banker) < 3:
                    banker.append(random.choice(deck))
                    deck.remove(banker[-1])
                    print('The Banker drew a {card}. Their new total is {total}.'.format(card = banker[-1],
                                                                                         total = total(banker)))
            if draw == 1 or draw == 9 or draw == 0:
                if total(banker) < 4:
                    banker.append(random.choice(deck))
                    deck.remove(banker[-1])
                    print('The Banker drew a {card}. Their new total is {total}.'.format(card = banker[-1],
                                                                                         total = total(banker)))
    winner = ''
    if total(banker) > total(player):
        if bet == 'banker':
            money += betsum
            money += betsum - (betsum / 20)
            print('You win!')
            print('You now have ${money}!'.format(money = money))
        else:
            print('You lose.')
            betsum = 0
    elif total(player) > total(banker):
        if bet == 'player':
            money += betsum * 2
            print('You win!')
            print('You now have ${money}!'.format(money = money))
        else:
            print('You lose.')
            betsum = 0
    else:
        if bet == 'tie':
            money += betsum * 9
            print('You win!')
            print('You now have ${money}!'.format(money = money))
        else:
            print('There was a tie.')
            money += betsum
            print('You now have ${money}.'.format(money = money))
    keepgoin = input('Do you want to keep playing?\n')
