# * Program 13

import csv


def writecsvemp():
    '''Creates and writes onto a csv file named emp which stores Employee ID,
    Employee name, Employee's Salary and Employee's Department'''
    a = int(input('Enter the no. of records you want to input:\n'))
    with open('emp.csv', 'w', newline='') as f:
        w = csv.writer(f)
        for i in range(a):
            empid = int(input('Enter Employee ID:\n'))
            empam = input('Enter Name of Employee:\n')
            sal = input('Enter Salary of Employee:\n')
            dept = input('Enter the Name of the Department:\n')
            l = [empid, empam, sal, dept]
            w.writerow(l)


def searchemp():
    '''Searches for a record in emp.csv and returns it if found or
    gives an error message if not'''
    a = int(input('Enter Employee ID:\n'))
    e = True
    with open('emp.csv') as f:
        c = csv.reader(f)
        for i in c:
            if a == int(i[0]):
                print(i)
                e = False
    if e:
        print('The Record was not found.')


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to create and write onto a csv file named emp.csv which stores Employee ID,
Employee name, Employee's Salary and Employee's Department.
Enter 2 to search a record using the Employee ID.\n'''))
    if n == 1:
        writecsvemp()
    elif n == 2:
        searchemp()
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
