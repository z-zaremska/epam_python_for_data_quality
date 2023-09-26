# Create a tool, which will do user generated news feed:
# 1.User select what data type he wants to add
# 2.Provide record type required data
# 3.Record is published on text file in special format
#
# You need to implement:
# 1.News – text and city as input. Date is calculated during publishing.
# 2.Private ad – text and expiration date as input. Day left is calculated during publishing.
# 3.Your unique one with unique publish rules.
#
# Each new record should be added to the end of file. Commit file in git for review.
import datetime as dt
import os


class Feed:
    file_path = 'news_feed.txt'

    def __init__(self, text):
        self.text = text
        self.insert_date = dt.datetime.today()
        self.feed = ''

    @classmethod
    def create_feed_file(cls):
        if os.path.isfile(cls.file_path) is False:
            with open(cls.file_path, 'w', encoding='utf-8') as file:
                file.write('NEWS FEED\n\n')

    def save_feed(self):
        with open('news_feed.txt', 'a', encoding='utf-8') as file:
            file.write(self.feed)


class News(Feed):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city
        self.feed = f'--- News ---\n{self.text}\n{self.city}, {self.insert_date}\n'


class PrivateAd(Feed):
    def __init__(self, text, exp_date):
        super().__init__(text)
        self.exp_date = dt.datetime.strptime(exp_date, '%d-%m-%Y')
        self.days_left = (self.exp_date - self.insert_date).days
        self.feed = f'--- Private Ad ---\n{self.text}\nActual until: {self.exp_date}, {self.days_left} days left\n'


# Create new feed file if nox exists.
Feed.create_feed_file()
# Take an information from user.
user_category = input('What category you want to add?\n"News" | "Private ad" | Type custom category: ').lower()

if user_category == 'news':
    city = input('Provide city name: ').capitalize()
    news_text = input('Provide news text: ')

    news = News(news_text, city)
    news.save_feed()

elif user_category == 'private ad':
    ad_text = input('Provide advertisement text: ')
    expiration_date = input('Provide expiration date (dd-mm-yyyy): ')

    ad = PrivateAd(ad_text, expiration_date)
    ad.save_feed()

else:
    print('Custom')
