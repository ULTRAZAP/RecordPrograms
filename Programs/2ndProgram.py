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


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to find if a No. is Amstrong or not.
Enter 2 to generate Floyd's Triangle for x no.\n'''))
    if n == 1:
        ams()
    elif n == 2:
        floyd()
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
