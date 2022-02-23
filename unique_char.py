# Michael Hofbauer ~ hofbauer@uab.edu

# Implement an algorithm to check
# whether a string has all unique characters.

def f():
    s = input('> Enter a string: ')
    l_s = list(s)
    s_s = set(s)
    if len(l_s) != len(s_s):
        print(f'String \'{s}\' has not unique characters.')
    else:
        print('This is a string with unique characters.')
