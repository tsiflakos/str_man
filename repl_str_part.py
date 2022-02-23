# Michael Hofbauer ~ hofbauer@uab.edu

# Write a method to replace all spaces in a string
# with '%20'. Except for the end and the beginning.

def g():
    s = input('> Let\'s enter a string: ')
    # Splitting string without withespaces into list.
    l = s.split()
    # Joining words in list separated by '%20'.
    s_new = '%20'.join(l)
    print()
    print(s_new)
