# Michael Hofbauer ~ hofbauer@uab.edu

# Given a string, write a function to check if
# it is a permutation of a palin­drome.

def h():
    s = input('> Input a string: ')
    s = s.strip()

    # Set of letters appearing only once
    # in the string s.
    sl = {i for i in s if s.count(i) == 1}

    # Palindrome can have at most one single letter.
    if len(sl) >= 2:
        print("""The number of single letters in
        the string are more than one.
        That\'s not a palindrome, due to symmetry.""")

    # Only one letter appears once in s,
    # but string has even number of letters
    # and is, thus, asymmetric,
    # hence, it cannot be a palindrome (e.g.'ataa'.)
    elif len(sl) == 1 and len(s) % 2 == 0:
        print("""Letter count even and the number
        of single letters is one (e.g. 'ataa'). This
        is not a palindrome.""")

    elif len(sl) == 1 and len(s) % 2 != 0:
        print(f'The string {repr(s)} is an odd palindrome.')

    elif len(sl) == 0 and len(s) >= 2:
        print(f'The string {repr(s)} is an even palindrome.')

    else:
        print('You entered an empty string or something non-sensible!')
        print('We call the initial function for you again.')
        # Jump back to calling inital function h().
        h()
