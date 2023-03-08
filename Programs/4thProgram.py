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


d = 'Yy'
while d in 'Yy':
    li = eval(input('Enter a list containing no.:\n'))
    n = int(input('''Enter 1 to find the highest no. in the list.
Enter 2 to find the lowest value in the list.
Enter 3 to calculate the sum of all the values in the list.\n'''))
    if n == 1:
        max_list(li)
    elif n == 2:
        min_list(li)
    elif n == 3:
        sum_list(li)
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
