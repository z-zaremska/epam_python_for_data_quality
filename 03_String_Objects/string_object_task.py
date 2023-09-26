import string
import re

homework = """ tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

whitespaces = 0
# Count whitespaces in the given text.
for char in homework:
    if char in string.whitespace:
        whitespaces += 1

print(f'Whitespaces: {whitespaces}')

# Split each line and capitalize first letter.
lines = [line.lower() for line in homework.split('\n')]
last_words_sentence = ''
result = ''

for line in lines:
    # If line is more than one character get last word from the sentence
    # and append to the new sentence.
    if len(line) > 1:
        # Retrieve last word from the sentence and add to last_words_sentence.
        last_word_start = line.rfind(' ') + 1
        last_word = line[last_word_start:-1]
        last_words_sentence += last_word + ' '

    # Replace typo 'iz' with 'is'.
    if line.find(' iz ') != -1:
        line = line.replace(' iz ', ' is ')

    # Capitalize first letter of each sentence.
    for char in line:
        if char not in string.whitespace:
            line = line.replace(char, char.upper(), 1)
            break

    # Capitalize first letters of inner sentence in each line.
    if line.find('. ') != -1:
        inner_indexes = [i.start() for i in re.finditer('. ', line)]

        for index in inner_indexes:
            inner_sentence_start = index + 2
            letter = line[inner_sentence_start]
            line = line.replace(f'. {letter}', f'. {letter.upper()}')

    result += line + '\n'

# Append the sentence made of last words and format.
result += '\n' + last_words_sentence.capitalize().rstrip() + '.'
print(result)
