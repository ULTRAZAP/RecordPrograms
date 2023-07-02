# * Program 15

books = []
bookdic = {}


def isEmpty(s):
    '''Checks if the stack is Empty or not.'''
    if len(s) == 0:
        return True
    return False


def enterdictionary():
    '''Stores the Book ID and Names of the Books in a dictionary.'''
    e = eval(
        input('Enter a dictionary containing Book ID And Book Name:\n'))
    bookdic.update(e)


def pushvalues():
    '''Adds the names of the Books starting with A or C to a stack.'''
    for i in list(bookdic.values()):
        if i[0] in 'CcAa':
            books.append(i)
    bookdic.clear()


def popvalues():
    '''Removes and Returns a value from the stack.'''
    if isEmpty(books):
        return 'Stack Empty'
    return books.pop()


def peekvalues():
    '''Returns the topmost value from the stack.'''
    if isEmpty(books):
        return 'Stack Empty'
    return books[-1]


def display():
    '''Displays the whole stack from the top.'''
    if isEmpty(books):
        print('Stack Empty')
    for i in books[::-1]:
        print(i)


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to store book details like Book ID & Book Name in a dictionary format.
Enter 2 to Push Names of the Books which start with A or C to stack.
Enter 3 to Remove an element from the stack.
Enter 4 to Peek the stack.
Enter 5 to Display the stack.\n'''))
    if n == 1:
        a = 'Yy'
        while a in 'Yy':
            enterdictionary()
            a = input('Do you want to add more records? (Y/N)\n')
    elif n == 2:
        pushvalues()
    elif n == 3:
        print(popvalues())
    elif n == 4:
        print(peekvalues())
    elif n == 5:
        display()
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
