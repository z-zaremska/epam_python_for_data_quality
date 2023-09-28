# Calculate number of words and letters from previous Homeworks 5/6 output test file.
# Create two csv:
# 1.word-count (all words are preprocessed in lowercase)
# 2.letter, count_all, count_uppercase, percentage (add header, space characters are not included)
# CSVs should be recreated each time new record added.
import csv

file_path = 'news_feed.txt'

with open(file_path, encoding='utf-8') as file:
    text = file.read().replace('.', ' ').replace(',', ' ').replace('\n', ' ').replace('-', ' ').replace(':', ' ')
    items = [word for word in text.split(' ') if word.isalpha()]
    print(items)

# Word count
words_collection = {}
for word in items:
    if words_collection.get(word):
        words_collection[word] += 1
    else:
        words_collection[word] = 1
