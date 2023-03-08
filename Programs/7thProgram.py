# * Problem 7

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


d = 'Yy'
while d in 'Yy':
    n = int(input('''Enter 1 to create a text file named content and add some text in it.
Enter 2 to count number of lines, consonants, digits, spaces & words.
Enter 3 to create another file called "wspace.txt" using the original which will contain the text after replacing all the blank spaces with '#'.
Enter 4 to Read & display the contents of both the files.\n'''))
    if n == 1:
        CreateTextFile7()
    elif n == 2:
        CountAll()
    elif n == 3:
        print(
            f'The no. of lines, consonants, digits, whitespaces and words are\n{ReplaceSpace()}')
    elif n == 4:
        display()
    else:
        print('Wrong Input!\nTry Again!')
    d = input('Do you want to try again? (Y/N)\n')
