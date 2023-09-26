import string
import re
from typing import List


def count_whitespaces(text: str):
    """Returns number of found whitespaces in the given text."""

    whitespaces = 0
    # Count whitespaces in the given text.
    for char in text:
        if char in string.whitespace:
            whitespaces += 1

    return whitespaces


def split_text(text: str):
    """Returns list of text lines and lowercase all letters."""
    return [line.lower() for line in text.split('\n')]


def create_last_words_sentence(lines: List[str]) -> str:
    """Returns sentence made of last words of given list of sentences."""
    last_words_sentence = ''

    for line in lines:
        if len(line) > 1:
            # Retrieve last word from the sentence and add to last_words_sentence.
            last_word_start = line.rfind(' ') + 1
            last_word = line[last_word_start:-1]
            last_words_sentence += last_word + ' '

    return last_words_sentence.rstrip() + '.'


def correct_is(line: str) -> str:
    # Returns given line with corrected typo of 'is'.
    if line.find(' iz ') != -1:
        return line.replace(' iz ', ' is ')
    else:
        return line


def detect_sentences(line: str):
    """
    Capitalizes first letters of all sentences in the given line
    and returns it.
    """

    # Capitalize first letter of given line.
    for char in line:
        if char not in string.whitespace:
            line = line.replace(char, char.upper(), 1)
            break

    # Capitalize first letters of inner sentence in each line if exists.
    if line.find('. ') != -1:
        inner_indexes = [i.start() for i in re.finditer('. ', line)]

        for index in inner_indexes:
            inner_sentence_start = index + 2
            letter = line[inner_sentence_start]
            line = line.replace(f'. {letter}', f'. {letter.upper()}')

    return line


def format_text(lines: List[str]):
    result_text = ''

    for line in lines:
        # Replace typos 'iz' with 'is'.
        line = correct_is(line)

        # Detect all line sentences.
        line = detect_sentences(line)

        # Append line to the result.
        result_text += line + '\n'

    return result_text


def adjust_text(text: str) -> str:
    """Adjust given text according to given rules."""

    # Edit text formatting.
    text_lines = split_text(text)
    # Create new sentence made of last word of all sentences.
    last_sentence = create_last_words_sentence(text_lines)
    # Update text lines with new sentence.
    text_lines.append(last_sentence)
    # Edit text formatting.
    formatted_text = format_text(text_lines)

    return formatted_text


homework = """ tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Print number of found in the text whitespaces.
text_whitespaces = count_whitespaces(homework)
print(f'Whitespaces: {text_whitespaces}')

# Format given text.
format_homework = adjust_text(homework)
print(format_homework)
