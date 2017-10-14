message = 'sld wrw blf fmhxiznyov gsrh nvhhztv'

answer = ''

current = 0

for letter in message:
    current = -(ord(letter) - 109.5)
    current += 109.5
    answer += chr(int(current))

print(answer)
