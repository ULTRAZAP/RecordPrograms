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


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to find Factorial of a number.
                   Enter 2 to generate Fibonacci Series for x no.
                   Enter 3 to check if a number is palindrome or not.\n'''))
    if n == 1:
        factorial()
    elif n == 2:
        fib()
    elif n == 3:
        palin()
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
