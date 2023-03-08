# * Program 9
import pickle as p
c = 0


def createandaddtobinaryfile():
    '''Creates a binary file names student which stores admission no.,  student name and percentage in dictionary format'''
    s = {}
    global c
    c = int(input('How many records do you want to add?\n'))
    with open('student.dat', 'wb') as f:
        for i in range(c):
            s['Admission_number'] = int(input('Enter Admission number:\n'))
            s['Student Name'] = input('Enter Student Name:\n')
            s['Percentage'] = int(input('Enter Percentage:\n'))
            p.dump(s, f)


def countrec():
    '''Counts the no. of students who's percentage is above 75'''
    a = 0
    s = {}
    with open('student.dat', 'rb') as f:
        for i in range(c):
            s = p.load(f)
            if s['Percentage'] > 75:
                print(s)
                a += 1
    print(f'The No. of students scoring above 75% are {a}.')


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to create a binary file named student and add admission number, student name and percentage of students.
Enter 2 to read contents of the file.\n'''))
    if n == 1:
        createandaddtobinaryfile()
    elif n == 2:
        countrec()
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
