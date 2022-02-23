# Method to find word frequencies in a text file.
# The goal is to provide a program, which is
# efficient when searching the text file more than once.

# Room for improvement:

# 1. Delete the current value of the word variable from list_of_words
# once the word has been added to no_of_words dictionary. Therefore,
# list_of_words becomes smaller and the we need to count the new word
# repetitions from a smaller list.

# 2. Create further partition elements for words in list_of_words, e.g. first
# and last letter of current word.


from string import ascii_lowercase as s_1
from string import ascii_uppercase as s_2

s = s_1 + s_2
temp_word = ''
list_of_words = []

file_path = input('Enter the path of the file you wish to open: ')
with open(file_path) as f:
    file_str = f.read()
    # Reading a word into temp_word, until we hit a letter/white space,
    # which is not contained in the ascii alphabet.
    # All words are saved in the list list_of_words.
    for letter in file_str:
        if letter in s:
            temp_word = temp_word + letter
            continue
        if temp_word == '':
            continue
        else:
            list_of_words.append(temp_word)
            temp_word = ''

    # print('\n',list_of_words,'\n')

    # no_of_words = {i:[] for i in range(1,len(list_of_words))}
    no_of_words = {}
    # length = len(list_of_words)

    for word in list_of_words:
        # list_of_words.remove(word)
        # print(list_of_words)
        # Comment:
        # For some reason, words variable always jumps one list item ahead.
        for j in range(1,len(list_of_words)):
            if list_of_words.count(word) == j:
                if j not in no_of_words.keys():
                    # Use set container to avoid repetitions.
                    no_of_words[j] = set()
                    no_of_words[j].add(word)
                    # Jump out of inner for loop if word count matches.
                    break
                else:
                    no_of_words[j].add(word)
                    # Jump out of inner for loop if word count matches.
                    break
            else:
                # Redundant continue statement.
                continue

print('''\nA dictionary displaying the words with their count from
the file {}\n'''.format(file_path))
print(no_of_words)
print()
