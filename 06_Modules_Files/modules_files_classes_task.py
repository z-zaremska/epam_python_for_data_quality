# Expand previous Homework 5 with additional class, which allow to provide records by text file:
# 1.Define your input format (one or many records)
# 2.Default folder or user provided file path
# 3.Remove file if it was successfully processed
# 4.Apply case normalization functionality form Homework 3/4
import datetime as dt
import os


class Input:
    def __init__(self, path='/input', default=True):
        self.path = path
        self.input = []
        if default:
            self.paths_list = [file for file in os.listdir(self.path) if file.endswith('.txt')]
            self.path_id = 0
            self.paths_num = len(self.paths_list)

    def change_path(self):
        if self.paths_list and self.path_id < self.paths_num:
            self.path = self.paths_list[self.path_id]
            self.path_id += 1

    def read_input_parameters(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            loops = len(lines) // 4

            for i in range(loops):
                input_param = {
                    'category': lines[0].split("'")[1],
                    'text': lines[1].split("'")[1],
                    'additional': lines[2].split("'")[1]
                }

                self.input.append(input_param)
                lines = lines[4:]


class Feed:
    file_path = 'news_feed.txt'

    def __init__(self, text):
        self.text = text
        self.insert_date = dt.datetime.now()
        self.feed = ''

    @classmethod
    def create_feed_file(cls):
        if os.path.isfile(cls.file_path) is False:
            with open(cls.file_path, 'w', encoding='utf-8') as file:
                file.write('NEWS FEED\n\n')

    def save_feed(self):
        with open('news_feed.txt', 'a', encoding='utf-8') as file:
            file.write(self.feed + '\n\n')


class News(Feed):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city
        self.feed = f'--- News ---\n{self.text}\n{self.city}, {self.insert_date.strftime("%d-%m-%Y %H:%M")}'


class PrivateAd(Feed):
    def __init__(self, text, exp_date):
        super().__init__(text)
        self.exp_date = dt.datetime.strptime(exp_date, '%d-%m-%Y')
        self.days_left = (self.exp_date - self.insert_date).days
        self.feed = f'--- Private Ad ---\n{self.text}\nActual until: {self.exp_date.strftime("%d-%m-%Y")}, {self.days_left} days left'


class Note(Feed):
    def __init__(self, text, name):
        super().__init__(text)
        self.name = name
        self.feed = f'--- Note ---\n{self.text}\n{self.name}, {self.insert_date.strftime("%d-%m-%Y %H:%M")}'


# Get information about input type.
data_type = input('Do you want to enter data manually/by file? (m/f) ').lower()

if data_type == 'f':
    custom_path = input('Do you want to provide path to the file? (y/n) ').lower()

    if custom_path == 'y' or custom_path == 'yes':
        custom_path = input('Enter path to the txt file with the input: ').lower()
        file_input = Input(custom_path, False)
    else:
        file_input = Input()
        file_input.change_path()

    file_input.read_input_parameters()


# Create new feed file if nox exists.
Feed.create_feed_file()
feed_counter = 0
next_feed = True

while next_feed:
    if data_type == 'm':
        # Take an information from user.
        user_category = input('What category you want to add?\n"News" | "Private ad" | "Note": ').lower()
    else:
        user_category = file_input.input[feed_counter]['category'].lower()

    if user_category == 'news':
        if data_type == 'm':
            news_text = input('Provide news text: ')
            user_city = input('Provide city name: ').lower().title()
        else:
            news_text = file_input.input[feed_counter]['text']
            user_city = file_input.input[feed_counter]['additional']

        news = News(news_text, user_city)
        news.save_feed()

    elif user_category == 'private ad':
        if data_type == 'm':
            ad_text = input('Provide advertisement text: ')
            expiration_date = input('Provide expiration date (dd-mm-yyyy): ')
        else:
            ad_text = file_input.input[feed_counter]['text']
            expiration_date = file_input.input[feed_counter]['additional']

        ad = PrivateAd(ad_text, expiration_date)
        ad.save_feed()

    else:
        if data_type == 'm':
            note_text = input('Provide note text: ')
            user_name = input('Provide your name ').lower().title()
        else:
            note_text = file_input.input[feed_counter]['text']
            user_name = file_input.input[feed_counter]['additional']

        note = Note(note_text, user_name)
        note.save_feed()

    if data_type == 'm':
        next_insert = input('Do you want to insert another (y/n)? ').lower()
        if next_insert in ['y', 'yes']:
            next_feed = True
        else:
            next_feed = False
    else:
        feed_counter += 1
        if feed_counter == len(file_input.input):
            next_feed = False

print('\nFile has been saved.')
