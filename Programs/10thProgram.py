# * Program 10
import pickle as p
global n
n = 0


def createbinary():
    s = {}
    n = int(input('Enter the number of companies:\n'))
    with open('company.dat', 'wb') as f:
        for i in range(n):
            s['CompanyID'] = int(input('Enter Company ID:\n'))
            s['CompanyName'] = input('Enter Company Name:\n')
            s['Turnover'] = int(input('Enter Turnover:\n'))
            p.dump(s, f)


def display():
    s = {}
    with open('company.dat', 'rb') as f:
        for i in range(n):
            s = p.load(f)
            print(s)


def turnover():
    s = {}
    a = int(input('Enter a turnover:\n'))
    with open('company,dat', 'rb') as f:
        for i in range(n):
            s = p.load(f)
            if s['Turnover'] > a:
                print(s)


def companyid():
    s = {}
    a = int(input('Enter Company ID:\n'))
    with open('company.dat', 'rb') as f:
        for i in range(n):
            s = p.load(f)
            if s['CompanyID'] == a:
                print(s)


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to create a binary file named company and add company id, company name and turnover.
                   Enter 2 to read contents of the file.
                   Enter 3 to input a turnover value and know which Company's turnover is above your given value.
                   Enter 4 to search for a Company with a Company ID.\n'''))
    if n == 1:
        createbinary()
    elif n == 2:
        display()
    elif n == 3:
        turnover()
    elif n == 4:
        companyid()
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
