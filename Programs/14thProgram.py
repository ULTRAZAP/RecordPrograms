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


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to push records of Hostel No., Total Students along with Total Rooms to a stack.
Enter 2 to Remove an element from the stack.
Enter 3 to Peek the stack.
Enter 4 to Display the stack.\n'''))
    if n == 1:
        a = 'Yy'
        while a in 'Yy':
            ht = int(input('Enter Hostel Number:\n'))
            ts = int(input('Enter Total Students:\n'))
            tr = int(input('Enter Total Rooms:\n'))
            a = input('Do you want to add more records? (Y/N)\n')
            l = [ht, ts, tr]
            push_element(l)
    elif n == 2:
        print(pop_element(hostel))
    elif n == 3:
        print(peek(hostel))
    elif n == 4:
        display(hostel)
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
