# * Program 12

import csv


def writeintocsv():
    '''Writes the data into the csv file'''
    with open('student.csv', 'w', newline='') as f:
        w = csv.writer(f)
        a = int(input('Enter the no. of records you want to enter:\n'))
        for i in range(a):
            r = int(input('Enter Roll No.:\n'))
            am = input('Enter Name:\n')
            m1 = int(input('Enter marks of Subject 1:\n'))
            m2 = int(input('Enter marks of Subject 2:\n'))
            m3 = int(input('Enter marks of Subject 3:\n'))
            m4 = int(input('Enter marks of Subject 4:\n'))
            m5 = int(input('Enter marks of Subject 5:\n'))
            l = [r, am, m1, m2, m3, m4, m5]
            w.writerow(l)


def totalpercen():
    '''Calculates Total and Percentage of each student'''
    total = 0
    with open('student.csv') as f:
        c = csv.reader(f)
        for i in c:
            for j in i[2:]:
                total += int(j)
            print(
                f'The Total and Percentage of {i[1]} is {total} and {total/5} respectively.')
            total = 0


def display():
    '''Displays the name of the student who have any marks that are grater than 80'''
    with open('student.csv') as f:
        c = csv.reader(f)
        for i in c:
            for j in i[2:]:
                a = int(j)
                if a > 80:
                    print(
                        f'{i[1]} has scored more than 80 in Subject {i.index(j)-1}.')


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to write onto a csv file the Roll No., Name, Marks for Subjects 1,2,3,4 & 5.
Enter 2 to calculate Total and Percentage of each Student.
Enter 3 to display the name of the Student who have any marks that are grater than 80.\n'''))
    if n == 1:
        writeintocsv()
    elif n == 2:
        totalpercen()
    elif n == 3:
        display()
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
