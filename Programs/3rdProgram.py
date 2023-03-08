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
    if sentence[0] != ' ':
        print('Number of words = ', sentence.count(' ')+1)
        return
    print('Number of words = ', sentence.count(' '))


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to display all the names from the list  STATES, which are starting with alphabet M.
Enter 2 to enter a sentence and remove a letter from it.
Enter 3 to count the no. of words in a sentence.\n'''))
    if n == 1:
        states = ["MP", "UP", "DL", "UK", "KA", 'MH']
        MSEARCH(states)
    elif n == 2:
        sentence = input('Enter A Sentence:\n')
        letter = input('Enter A Letter You Want To Remove:\n')
        remove_letter(sentence, letter)
    elif n == 3:
        sentence = input('Enter A Sentence:\n')
        cnt(sentence)
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
