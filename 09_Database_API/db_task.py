# Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
# 1.Different types of records require different data tables
# 2.New record creates new row in data table
# 3.Implement “no duplicate” check.
from feed_lib import TxtInput, JsonInput, XmlInput, Feed, News, PrivateAd, Note, DatabaseManager

db_manager = DatabaseManager('task_database')
db_manager.create_tables()


# Get information about input type.
data_type = input('Do you want to enter data manually/by file? (m/f) ').lower()

if data_type == 'f':
    feed_counter = 0
    custom_path = input('Do you want to provide path to the file? (y/n) ').lower()

    if custom_path == 'y' or custom_path == 'yes':
        custom_path = input('Enter path to the txt file with the input: ').lower()
        if custom_path.endswith('.txt'):
            file_input = TxtInput(custom_path)
        elif custom_path.endswith('.json'):
            file_input = JsonInput(custom_path)
        elif custom_path.endswith('.xml'):
            file_input = XmlInput(custom_path)

        file_input.read_input_parameters()
    else:
        file_extension = input('What file type to process: json/txt/xml? ')
        if file_extension.lower() == 'txt':
            file_input = TxtInput()
        elif file_extension.lower() == 'json':
            file_input = JsonInput()
        elif file_extension.lower() == 'xml':
            file_input = XmlInput()

        file_input.get_input_from_all_files()

# Create new feed file if nox exists.
Feed.create_feed_file()
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
        db_manager.insert_data('news', news_text, user_city)

    elif user_category == 'private ad':
        if data_type == 'm':
            ad_text = input('Provide advertisement text: ')
            expiration_date = input('Provide expiration date (dd-mm-yyyy): ')
        else:
            ad_text = file_input.input[feed_counter]['text']
            expiration_date = file_input.input[feed_counter]['additional']

        ad = PrivateAd(ad_text, expiration_date)
        ad.save_feed()
        db_manager.insert_data('private_ads', ad_text, expiration_date)

    else:
        if data_type == 'm':
            note_text = input('Provide note text: ')
            user_name = input('Provide your name ').lower().title()
        else:
            note_text = file_input.input[feed_counter]['text']
            user_name = file_input.input[feed_counter]['additional']

        note = Note(note_text, user_name)
        note.save_feed()
        db_manager.insert_data('notes', note_text, user_name)

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
db_manager.cursor.execute('SELECT * FROM notes;')
print(db_manager.cursor.fetchall())
