
import csv
import pickle as p
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


# * Program 9
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


# * Program 10
c = 0


def createbinary():
    '''Creates a binary file named company which stores the id of the companies, their names and turnover respectively'''
    s = {}
    global c
    c = int(input('Enter the number of companies:\n'))
    with open('company.dat', 'wb') as f:
        for i in range(c):
            s['CompanyID'] = int(input('Enter Company ID:\n'))
            s['CompanyName'] = input('Enter Company Name:\n')
            s['Turnover'] = int(input('Enter Turnover:\n'))
            p.dump(s, f)


def display():
    '''Displays all the companies dictionaries'''
    s = {}
    with open('company.dat', 'rb') as f:
        for i in range(c):
            s = p.load(f)
            print(s)


def turnover():
    '''Prints the turnover of the companies which are higher than the input turnover'''
    s = {}
    a = int(input('Enter a turnover:\n'))
    with open('company,dat', 'rb') as f:
        for i in range(c):
            s = p.load(f)
            if s['Turnover'] > a:
                print(s)


def companyid():
    '''Searches for a particular company using its id and prints only its data'''
    s = {}
    a = int(input('Enter Company ID:\n'))
    with open('company.dat', 'rb') as f:
        for i in range(c):
            s = p.load(f)
            if s['CompanyID'] == a:
                print(s)


# * Program 11


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

# * Program 12


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

# * Program 13


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

# * Program 14


hostel = []


def isEmpty(s):
    '''Checks if the stack is empty or not'''
    if len(s) == 0:
        return True
    return False


def push_element(l):
    '''Adds the element to stack'''
    hostel.append(l)


def pop_element(s):
    '''Checks if the stack is empty or not and returns a popped value from the stack'''
    if isEmpty(s):
        return 'Stack is Empty.'
    return s.pop()


def peek(s):
    '''Returns the topmost element from the stack'''
    if isEmpty(s):
        return 'Stack is Empty.'
    return s[-1]


def display(s):
    '''Displays the entire stack'''
    if isEmpty(s):
        print('Stack is Empty.')
        return
    for i in s[::-1]:
        print(i)


# * Program 15

books = []


def isEmpty(s):
    '''Checks if the stack is Empty or not.'''
    if len(s) == 0:
        return True
    return False


def enterdictionary():
    '''Stores the Book ID and Names of the Books in a dictionary.'''
    global bookdic
    e = eval(
        input('Enter a dictionary containing Book ID And Book Name:\n'))
    bookdic += e


def pushvalues():
    '''Adds the names of the Books starting with A or C to a stack.'''
    for i in list(bookdic.values()):
        if i[0] in 'CcAa':
            books.append(i)


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
