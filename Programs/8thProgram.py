# * Program 8

def displaywords():
    '''Displays the words from the text file story which are less than 4 characters'''
    with open('story.txt') as f:
        a = f.read().split()
        for i in a:
            if len(i) < 4:
                print(i)


def seachword():
    '''Searches the no. of times a word is repeated inside the file'''
    e = input('Enter a word to be searched:\n')
    with open('story.txt') as f:
        a = f.read().split()
        d = a.count(e)
        print(f'The word {e} is {d} times repeating in the file.')


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to display words which are less than 4 characters in story.txt.
Enter 2 to search a word and its frequency in story.txt.\n'''))
    if n == 1:
        displaywords()
    elif n == 2:
        seachword()
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
