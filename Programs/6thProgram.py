# * Program 6

def CreateTextFile():
    """Creates a text file named data while"""
    a = '''This contains text that should be input in the data.txt file.
    Hello and How are you?
    I am fine, Don't Worry About me.'''
    with open('data.txt', 'w') as f:
        f.write(a)


def CopyVowelWord():
    """To create text file named vowel which will store all the
    words starting with vowel from the text file data"""
    vowel = []
    with open('data.txt') as f:
        a = f.read().split()
        for i in a:
            if i[0] in 'AEIOUaeiou':
                vowel.append(i)

    with open('vowel.txt', 'w') as v:
        v.writelines(vowel)


def display():
    """Displays the content of both the text files"""
    print('The Contents of data.txt is:')
    with open('data.txt') as f:
        print(f.read())
    print('The Content of vowel.txt is:')
    with open('vowel.txt') as v:
        print(v.read())


def TotalNumberOfWordsStartingWithVowel():
    """Displays the no. of words starting with vowels in the data.txt file"""
    vowel = 0
    with open('data.txt') as f:
        a = f.read().split()
        for i in a:
            if i[0] in 'AEIOUaeiou':
                vowel += 1
    print(f'The no. of words starting with vowel in data.txt is {vowel}.')


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to create a text file named data and add some text in it.
Enter 2 to copy all the words starting with a vowel from data and adding them to a new text file named vowel.
Enter 3 to display the content of both the files.
Enter 4 to count the number of words starting with vowel in data.txt.\n'''))
    if n == 1:
        CreateTextFile()
    elif n == 2:
        CopyVowelWord()
    elif n == 3:
        display()
    elif n == 4:
        TotalNumberOfWordsStartingWithVowel()
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
