# * Program 11
import pickle as p

a = 0


def bina():
    '''Creates a binary file named travel which stores the travel id, from and to address respectively'''
    s = {}
    global a
    a = int(input('Enter the number of records you want to input:\n'))
    with open('travel.dat', 'wb') as f:
        for i in range(a):
            s['TravelID'] = int(input('Enter Travel ID:\n'))
            s['From'] = input('From:\n')
            s['To'] = input('To:\n')
            p.dump(s, f)


def apend():
    '''Adds travel data to the travel binary file'''
    s = {}
    global a
    c = int(input('Enter the number of records you want to add:\n'))
    a += c
    with open('travel.dat', 'ab') as f:
        for i in range(c):
            s['TravelID'] = int(input('Enter Travel ID:\n'))
            s['From'] = input('From:\n')
            s['To'] = input('To:\n')
            p.dump(s, f)


def updatetravelid():
    '''Changes the values of the travel data using travel id'''
    s = {}
    c = int(input('Enter the Travel ID:\n'))
    d = input('Enter the changed From:\n')
    e = input('Enter the changed To:\n')
    with open('travel.dat', 'rb+') as f:
        for i in range(a):
            r = f.tell()  # This should always be before load
            s = p.load(f)
            if s['TravelID'] == c:
                s['From'] = d
                s['To'] = e
                f.seek(r)
                p.dump(s, f)


def display():
    '''Displays the data on the binary file travel'''
    s = {}
    with open('travel.dat', 'rb') as f:
        for i in range(a):
            s = p.load(f)
            print(s)


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to create a binary file named Travel and add Travel id, From and To.
Enter 2 to add data to the binary file.
Enter 3 to update a record based on the Travel ID.
Enter 4 to read contents of the file.\n'''))
    if n == 1:
        bina()
    elif n == 2:
        apend()
    elif n == 3:
        updatetravelid()
    elif n == 4:
        display()
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
