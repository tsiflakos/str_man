# Given two strings, write a function to check
# whether they are one (or zero) edits away.

def b(s1,s2):
    l1, l2 = list(s1), list(s2)

    # Define function b, with two parameters string lists (l1, l2),
    # which outputs the longer string list of the two.
    b = lambda l1, l2 : l1 if len(l1) > len(l2) else l2

    # If the difference of the string lengths is largen than two,
    # then strings differ by more than one edit.
    if abs(len(s1)-len(s2)) >= 2:
        print('String lengths difference is larger equal to two.')

    # Procedure if string lengths are exactly one unit apart.
    elif len(s1) == len(s2) + 1 or len(s1) + 1 == len(s2):
        for i in b(l1,l2):
            # l3 is a copy of the longest string list.
            # We need a copy to remove and compare entries.
            l3 = b(l1,l2)[:]
            l3.remove(i)
            # We remove always only one letter from l3
            # and compare it with the other string list for equality.
            if l3 == l2 or l3 == l1:
                print(f'Strings {s1}, {s2} are one insert or remove edit away.')
                break
        else:
            print('Strings differ by more than two characters.')
    # Procedure for strings of equal length.
    else:
        if s1 == s2:
            return print(f'Strings {s1}, {s2} are the same.')
# The l3 list contains the positions where the strings differ.
        l3 = [j for j in range(len(s1)+1) if s1[:j] != s2[:j]]
# If l3 contains only one number then the strings differ
# only at one letter and the following comparision returns True.
        if s1[l3[0]:] == s2[l3[0]:]:
            print(f'Strings {s1}, {s2} are one replace edit away.')
        else:
            print('Strings have the same lengths, but are different.')
