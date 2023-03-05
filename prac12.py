
# * Program 1
def factorial():
    """Calculating Factorial of a Number"""
    a = int(input('Enter a no.:\n'))
    b = 1
    for i in range(1, a+1):
        b *= i
    print(f'The Factorial of the no. is {b}.')


def fib():
    """ Function to generate Fibonacci series"""
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
    """ Palindrome checker"""
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
    """ Armstrong checker"""
    a = int(input('Enter a no.:\n'))
    b = len(str(a))
    c = a
    e = 0
    while a != 0:
        d = (a % 10) ** b
        e += d
        a //= 10
    if c == e:
        print('It is an Armstrong no.')
        return
    print('Its not an Armstrong no.')


def floyd():
    """ Function to generate Floyd's Triangle"""
    a = int(input('Enter the number of Rows:\n'))
    for i in range(1, a+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()


# * Program 3

def MSEARCH(STATES):
    """Sorting States from a list"""
    for i in STATES:
        if i[0] in 'Mm':
            print(i)


def remove_letter(sentence, letter):
    """ Removing a letter from a string"""
    c = ''
    for i in sentence:
        if i != letter:
            c += i
    print('Here is the sentence without the letter:\n', c)


def cnt(sentence):
    """ Count the number of words in a sentence"""
    print('Number of words = ', sentence.count(' ')+1)


# * Program 4

def max_list(l):
    """ Identify the element with the max len from a list"""
    a = l[0]
    for b in l:
        if b > a:
            a = b
    print('The Maximun of the elements is ', a, '.')


def min_list(l):
    """ Identify the element with the least len from a list"""
    a = l[0]
    for b in l:
        if b < a:
            a = b
    print('The Minimum of the elements is ', a, '.')


def sum_list(l):
    """ Calculating the sum of a list"""
    a = 0
    for b in l:
        a += b
    print('The Sum of the elements are ', a, '.')


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


# * Program 6

def CreateTextFile():
    """Creates a text file named data while"""
    a = '''This contains text that should be input in the data.txt file.
    Hello and How are you?
    I am fine, Don't Worry About me.'''
    with open('data.txt', 'w') as f:
        f.write(a)


def CopyVowelWord():
    '''To create text file named vowel which will store all the
    words starting with vowel from the text file data'''
    vowel = []
    with open('data.txt') as f:
        a = f.read().split()
        for i in a:
            if i[0] in 'AEIOUaeiou':
                vowel.append(i)

    with open('vowel.txt', 'w') as v:
        f.writelines(vowel)


def display():
    '''Displays the content of both the text files'''
    print('The Contents of data.txt is:')
    with open('data.txt') as f:
        print(f.read())
    print('The Content of vowel.txt is:')
    with open('vowel.txt') as v:
        print(v.read())


def TotalNumberOfWordsStartingWithVowel():
    '''Displays the no. of words starting with vowels in the data.txt file'''
    vowel = 0
    with open('data.txt') as f:
        a = f.read().split()
        for i in a:
            if i[0] in 'AEIOUaeiou':
                vowel += 1
    print(f'The no. of words starting with vowel in data.txt is {vowel}.')

# * Program 7


def CreateTextFile7():  # Added 6 to make the func name unique
    """ Function to create a text file with a few lines"""
    sampleLines = "Lorem ips3um dolor sit amet, 43c43onsectetur adipiscing 4elit. Vestibulum bi3b4endum mollis5 5viverra.3 Nulla a ipsum vitae nisl dignis3sim suscipit vitae at 4nisl. Curabitur3 finibus, sapien ac dic8tum ves3ibulum, eros magna auctor quam, quis eleifend tortor leo imperdiet ipsum. Praesent eget mo38lestie tellus. 8Mauris varius molestie enim nec euismod. Mauris tincidu3t lacinia pharetra. Quisque vel lacus id83 turpis egestas varius. Et83iam risus ipsum, elementum38 ac porta eu, rhoncus sed risus. D8uis vel nibh id dolor aliq8uam rutrum. Nunc ac pharetra ipsum. Fusce variu83s bibendum augue vitae sodales. Nam in nunc in lorem sagittis imperdiet 38a lacinia quam."

    with open("content.txt", "w") as f:
        f.write(sampleLines)


def CountAll():
    """ Calculate lines, consonants, words, digits and whitespaces from a txt file"""
    with open("content.txt", "r") as f:
        content = f.read()

        lines = sum(1 for line in open('content.txt'))

        consonants = 0
        for i in content.lower():
            # Excluding vowels, whitespaces, periods & commas
            vowels = ['a', 'e', 'i', 'o', 'u', ' ', ',', '.']
            if i not in vowels:
                consonants += 1

        digits = 0
        for char in content:
            if char.isdigit():
                digits = digits + 1

        whitespaces = 0
        for char in content:
            if char == " ":
                whitespaces += 1

        words = 0
        for word in content.split():
            words += 1

    return lines, consonants, digits, whitespaces, words  # Returns a tuple


def ReplaceSpace():
    """ Replacing all whitespaces with # in a file"""
    with open("content.txt", "r") as f1:
        output = f1.read().replace(' ', '#')

        with open("wspace.txt", "w") as f:
            f.write(output)


def display():
    print('The Content of content.txt is:')
    with open("content.txt") as f1:
        print(f1.read())
    print('The Content of wspace.txt is:')
    with open('wspace.txt') as f:
        print(f.read())
