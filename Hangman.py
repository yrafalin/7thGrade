import math
import random
import time

print('You have ten wrong chances in hangman.')
level = input('What level do you want from 1 to 12 or random?\n')
while level != '1' and level != '2' and level != '3' and level != '4' and level != '5' and level != '6' and level != '7' and level != '8' and level != '9' and level != '10' and level != '11' and level != 'random' and level != '12':
    level = input('What level do you want from 1 to 12 or random?\n')
library = ['challenge', 'conjugation', 'harbinger', 'ivory', 'vaporize', 'blitz', 'zodiac', 'galaxy', 'duplex', 'jazzy', 'axiom', 'waltz']
word = ''
if level == 'random':
    word = random.choice(library)
else:
    word = library[int(level) - 1]
wordshown = ''
wordlist = []
origwordlist = ''
for thing in word:
    origwordlist += thing + ' '
for thing in word:
    wordshown += '__ '
    wordlist.append('__')
print(wordshown)
chosenletters = []
chances = 10
while chances != 0 and wordshown != origwordlist:
    letter = input('What letter do you want?\n')
    while letter in chosenletters:
        letter = input('Don\'t choose a letter that\'s been chosen. What letter do you want?\n')
    chosenletters.append(letter)
    places = []
    if letter in word:
        numcycle = 0
        for thing in word:
            if thing == letter:
                places.append(numcycle)
            numcycle += 1
        for part in places:
            wordlist[part] = letter
        wordshown = ''
        for partb in wordlist:
            wordshown += partb + ' '
        print('That letter is in the word.')
        print(wordshown)
        print('You have {chances} more chances.'.format(chances = chances))
    else:
        chances -= 1
        print('That letter is not in the word.')
        print(wordshown)
        print('You have {chances} more chances.'.format(chances = chances))
if chances == 0 or chances == -1:
    print('You lose the game.')
else:
    print('You win! That was a hard one.')
