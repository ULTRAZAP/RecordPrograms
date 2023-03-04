
# * Program 1
def fac():
    a = int(input('Enter a no.:\n'))
    b = 1
    for i in range(1, a+1):
        b *= i
    print(f'The Factorial of the no. is {b}.')


def fib():
    a = int(input('Enter a no.:\n'))
    e, b, c = 0, 1, 0
    print(e, b, end=' ')
    for i in range(a-2):
        c = e+b
        print(c, end=' ')
        e = b
        b = c
    print()


def palin():
    a = int(input('Enter a no.:\n'))
    b = len(str(a))-1
    c = a
    e = 0
    while a != 0:
        d = (a % 10) ** b
        e += d
        a //= 10
        b -= 1
    if e == c:
        print('Its a Palindrome.')
        return
    print('Its not a Palindrome.')

# * Program 2


def ams():
    a = int(input('Enter a no.:\n'))
    b = len(str(a))
    c = a
    e = 0
    while a != 0:
        d = (a % 10) ** b
        e += d
        a //= 10
    if c == e:
        print('It is an Amstrong no.')
        return
    print('Its not an Amstrong no.')


def floyd():
    a = int(input('Enter the number of Rows:\n'))
    for i in range(1, a+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()

# * Program 3


def MSEARCH(STATES):
    for i in STATES:
        if i[0] in 'Mm':
            print(i)


def remove_letter(sentence, letter):
    c = ''
    for i in sentence:
        if i != letter:
            c += i
    print('Here is the sentence without the letter:\n', c)


def cnt(sentence):
    print('Number of words = ', sentence.count(' ')+1)

# * Program 4


def max_list(l):
    a = l[0]
    for b in l:
        if b > a:
            a = b
    print('The Maximun of the elements is ', a, '.')


def min_list(l):
    a = l[0]
    for b in l:
        if b < a:
            a = b
    print('The Minimum of the elements is ', a, '.')


def sum_list(l):
    a = 0
    for b in l:
        a += b
    print('The Sum of the elements are ', a, '.')

# * Program 5


def separatebycharacter():
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

# * Program 6


def CreateTextFile():
    '''Creates a text file named data while'''
    with open('data.txt', 'w') as f:
        f.write('Yello')


def CopyVowelWord():
    '''To create text file named vowel which will store all the
    words starting with vowel from the text file data'''
