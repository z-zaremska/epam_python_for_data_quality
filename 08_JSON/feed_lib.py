from abc import ABC, abstractmethod
import datetime as dt
import os


class Input(ABC):
    def __init__(self, path='input/'):
        self.path = path
        self.input = []
        self.extension = ''
        if path == 'input/':
            self.paths_list = [file for file in os.listdir(self.path) if file.endswith(self.extension)]
            self.path_id = 0
            self.paths_num = len(self.paths_list)

    def change_path(self, new_path):
        self.path = 'input/' + new_path

    def delete_input_file(self):
        """Removes current file with input data."""
        os.remove(self.path)

    @abstractmethod
    def read_input_parameters(self):
        pass

    def get_input_from_all_files(self):
        """
        Scans all available files in the default directory, retrieve
        input data and deletes the file.
        """
        for path in self.paths_list:
            self.change_path(path)
            self.read_input_parameters()


class TxtInput(Input):
    def __init__(self, path='input/'):
        super().__init__(path)
        self.extension = '.txt'

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

        self.delete_input_file()


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
