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


class Feed:
    def __init__(self, text):
        self.text = text
        self.insert_date = dt.date.today()


class News(Feed):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city


class PrivateAd(Feed):
    def __init__(self, text, expiration_date):
        super().__init__(text)
        self.expiration_date = dt.datetime.strptime(expiration_date, '%d-%m-%Y')




user_category = input('What category you want to add?\n"News" | "Private ad" | Type custom category: ').lower()

if user_category == 'news':
    city = input('Provide city name: ').capitalize()
    news_text = input('Provide news text: ')

    news = News(news_text, city)
    print(news.city)
    print(news.text)
    print(news.insert_date)

elif user_category == 'private ad':
    ad_text = input('Provide advertisement text: ')
    expiration_date = input('Provide expiration date (dd-mm-yyyy): ')
    print('Private ad')
else:
    print('Custom')
