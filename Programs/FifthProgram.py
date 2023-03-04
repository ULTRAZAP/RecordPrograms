# * Program 5

def separatebycharacter():
    """ Replace all whitespace with an emoji"""
    c = ''
    with open('f.txt', 'r') as f:
        a = f.read()
        for i in a:
            if i == ' ':
                c += '😊'
                continue
            c += i
    print(c)


def remove_a():
    """ Remove all lines containing the letter a"""
    c = []
    b = []
    with open('f.txt') as f:
        a = f.readlines()
        for i in a:
            if 'a' in i:
                b.append(i)
                continue
            c.append(i)
    if len(b) != 0:
        with open('f.txt', 'w') as e:
            e.writelines(c)
        with open('k.txt', 'w') as d:
            d.writelines(b)
    else:
        print('The File does not have the character\'a\'')


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to seperate the words in a txt file with 😊.
                   Enter 2 to remove any lines containing the character 'a' from a txt file and adding them to new text file.\n'''))
    if n == 1:
        separatebycharacter()
    elif n == 2:
        remove_a()
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
