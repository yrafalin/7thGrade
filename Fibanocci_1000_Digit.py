thefibs =[1, 1]
numbernow = 1
loopnum = 1
while True:
    digit = 0
    numbernow += thefibs[len(thefibs) - 2]
    thefibs.append(numbernow)
    numbernow = str(numbernow)
    print('after stringmake:', loopnum +2)
    if len(numbernow) == 1000:
        break
    numbernow = int(numbernow)
    loopnum += 1
print(loopnum +2)
