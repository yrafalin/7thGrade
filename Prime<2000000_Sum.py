import math
numberat = 2
factor = 2
total = 0
while numberat <= 2000000:
    if numberat % factor == 0 or factor >= math.sqrt(numberat):
        if factor >= math.sqrt(numberat):
            print('+++++++ FOUND PRIME ', numberat)
            total += numberat
        numberat += 1
        factor = 2
    else:
        factor += 1
print(total)
