# Michael Hofbauer ~ hofbauer@uab.edu

# Given two strings, write a method to check
# if one is a permutation of the other.

def f():
    s_1 = input('> Enter first string: ')
    s_2 = input('> Enter second string: ')
    l_1 = list(s_1)
    l_2 = list(s_2)

    for i in l_1:
        try:
            l_2.remove(i)
        except ValueError:
            print(f'''The strings \'{s_1}\', \'{s_2}\' are
            not permutations of each other.''')
            break

    if l_2 == []:
        print(f'''String \'{s_1}\' can be permuted
        into string \'{s_2}\'.''')
