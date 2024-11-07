for i in range(25, -1, -1):
    if i % 2 == 1:
        print(chr(90 - i), end='')
    else:
        print(chr(122 - i), end='')
print(chr(65), end='')
