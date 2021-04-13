library = []
book_list = []
magazine_list = []
podcast_episode_list = []
audio_book_list = []

'''
 we creat a book class
'''


class Book:

    def __init__(self, title, author, publish_year, language, price, pages, status=None, progress=None):

        '''
        :param title: book title
        :param author: book author
        :param publish_year: book publish year
        :param language: book language
        :param price: book price
        :param pages:book pages
        :param status: status
        '''
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.language = language
        self.price = price
        self.pages = pages
        self.status = status
        self.progress = progress

    '''
    we creat a read method to calculate unread pages 
    '''

    def read(self, num_read_page):
        self.unread = self.pages - num_read_page
        self.progress = num_read_page / self.pages
        print(
            f'u read {num_read_page} more pages u have {self.unread} more'
            f' pages to finish the book and'
            f' status is {self.status} and the progress is {self.progress}')

    '''
    we creat a status method to return the status of book according to read pages
    '''

    def get_status(self, num_read_page):
        if num_read_page == self.pages:
            self.status = 'finished'
        elif 0 < num_read_page < self.pages:
            self.status = 'reading'
        elif num_read_page == 0:
            self.status = 'unread'
        else:
            print('sth went wrong enter again')


    '''
    a static method  to get data for how many books u like to add 
    '''

    @staticmethod
    def get_data(num_book):
        title = input(f'Enter the book {num_book + 1 } title here:')
        author = input(f'Enter the author  of {title} here:')
        publish_year = int(input(f'Enter the {title} publish_year here:'))
        language = input(f'Enter the language of book {title} here :')
        price = int(input(f'Enter the price of book {title} here:'))
        pages = int(input(f'Enter pages of book {title} here:'))
        book = Book(title, author, publish_year, language,
                    price, pages, status=None, progress=None)
        library.append(book)
        book_list.append(book)
        print(book.__str__())

    def __str__(self):
        return f" book title: {self.title} book author : {self.author}  published year : {self.publish_year}" \
               f"  language : {self.language} price : " \
               f" {self.price}$  pages: {self.pages}  "


######################################################################################
######################################################################################
'''
class Magazine that is class Books child
'''


class Magazine(Book):
    def __init__(self, title, author, publish_year, language, price, pages, issue, status=None, progress=None):
        super().__init__(title, author, publish_year, language,
                         price, pages, status=None, progress=None)
        '''
        self.issue = issue
        self.status = status
        self.progress = progress
        the rest are inherited from class parent book
        '''
        self.issue = issue
        self.status = status
        self.progress = progress

    '''
    here we override the get_data method
    '''

    @staticmethod
    def get_data(num_magazine):
        title = input(f'Enter the magazine {num_magazine+1} title here:')
        author = input(f'Enter the author of  {title} here:')
        publish_year = int(input(f'Enter the {title} publish_year here:'))
        language = input(f'Enter the language of magazine {title} here :')
        price = int(input(f'Enter the price of magazine {title} here:'))
        pages = int(input(f'Enter pages of magazine {title} here:'))
        issue = int(input('Enter the issue here :'))
        magazine = Magazine(title, author, publish_year, language,
                            price, pages, issue, status=None, progress=None)
        library.append(magazine)
        magazine_list.append(magazine)
        print(magazine.__str__())
    '''
    here we override the str
    '''

    def __str__(self):
        return f" book title: {self.title} book author : {self.author}  published year : {self.publish_year}" \
               f"  language : {self.language} price : " \
               f" {self.price} $ \n  issue : {self.issue} pages: {self.pages}"


#############################################################################################################
'''
we creat a new class PodcastEpisode
'''


class PodcastEpisode:

    def __init__(self, title, speaker, publish_year, time, language, price, status=None, progress=None):
        '''

        :param title: title
        :param speaker: speaker
        :param publish_year: publish_year
        :param time: time
        :param language: language
        :param price: price
        :param status: status
        :param progress: progress
        '''
        self.title = title
        self.speaker = speaker
        self.publish_year = publish_year
        self.time = time
        self.language = language
        self.price = price
        self.status = status
        self.progress = progress

    '''
    a method that will return the progress and the un_listened time
    '''

    def listen(self, min_listened_podcast):
        self.un_listened = self.time - min_listened_podcast
        self.progress = min_listened_podcast / self.time
        print(
            f'u listened {min_listened_podcast} more minutes u have {self.un_listened} more minutes and the'
            f' status is {self.status}   and the progress is {self.progress}')



    '''
    a method that will return the statue of our instance
    '''

    def get_status(self, min_listened_podcast):
        if min_listened_podcast == self.time:
            self.status = 'finished'
        elif 0 < min_listened_podcast < self.time:
            self.status = 'listening'
        elif min_listened_podcast == 0:
            self.status = 'un_listened'
        else:
            print('sth went wrong enter again')

    '''
    a static method that would creat a instance from  input and would append it to library
    '''
    @staticmethod
    def get_data(num_podcast_episode):
        title = input(f'Enter the podcast {num_podcast_episode + 1} title here:')
        speaker = input(f'Enter the speaker of  {title} here:')
        publish_year = int(input(f'Enter the {title} publish_year here:'))
        time = int(input(f"Enter the time of {title} here "))
        language = input(f'Enter the language of  {title} here :')
        price = int(input(f'Enter the price of  {title} here:'))
        podcasepisode = PodcastEpisode(title, speaker, publish_year, time, language, price, status=None,
                                       progress=None)
        library.append(podcasepisode)
        podcast_episode_list.append(podcasepisode)
        print(podcasepisode.__str__())
        print([podcast.title for podcast in podcast_episode_list])

    def __str__(self):
        return f" the podcast: {self.title} speaker : {self.speaker}  published year : {self.publish_year}" \
               f" time: {self.time} language: {self.language} price :" \
               f"{self.price} "


#####################################################################################################################

'''
the class AudioBook is PodcastEpisode  child
'''


class AudioBook(PodcastEpisode):

    def __init__(self, title, speaker, publish_year, time, language, price, author, pages, audio_language, status=None,
                 progress=None):
        super().__init__(title, speaker, publish_year, time,
                         language, price, status=None, progress=None)
        '''
        self. author = author
        self.pages = pages
        self.audio_language = audio_language
        self.status = status
        self.progress = progress
        '''
        self.author = author
        self.pages = pages
        self.audio_language = audio_language
        self.status = status
        self.progress = progress

    '''
    we override our get data method 
    '''
    @staticmethod
    def get_data(num_audio):
        title = input(f'Enter the audio {num_audio+ 1} title here:')
        speaker = input(f'Enter the speaker of  {title} here:')
        publish_year = int(input(f'Enter the {title} publish_year here:'))
        time = int(input(f"Enter the time of {title} here "))
        language = input(f'Enter the language of  {title} here :')
        price = int(input(f'Enter the price of  {title} here:'))
        author = input(f'Enter the {title} author here :')
        pages = int(input(f'Enter the pages of {title} here :'))
        audio_language = input(f'enter the {title} audio language here:')
        audiobook = AudioBook(title, speaker, publish_year, time, language,
                              price, author, pages,
                              audio_language, status=None,
                              progress=None)
        library.append(audiobook)
        audio_book_list.append(audiobook)
        print(audiobook.__str__())
        print([audiobook.title for audiobook in audio_book_list])

    def __str__(self):
        return f" the audio: {self.title} speaker : {self.speaker}  published year : {self.publish_year}" \
               f" time : {self.time} language : {self.language} audio language : {self.audio_language}" \
               f" price : {self.price}  "
#######################################################################################################
######################################################################################################################


def sorted_library(list_input, metric, reverse):
    """
        This function get  argument and show  base on metric
    """
    library_list = sorted(list_input, key=lambda x:
                          x.__getattribute__(metric), reverse=reverse)
    for _ in library_list:
        class_name = type(_).__name__
        if class_name == 'Book':
            media_name = 'book'
        elif class_name == 'Magazine':
            media_name = 'magazine'
        elif class_name == 'PodcastEpisode':
            media_name = 'podcast episode'
        else:
            media_name = 'audiobook'
        print(media_name, _.title, _.progress)
############################################################################################################
###########################################################################################################
##############################################################################################################
#####################################################################################################################


user_name = input('Enter username here :')
user_password = int(input('enter password  here :'))
if user_name == 'zahrajalilian' and user_password == 1997:
    print('WELCOME TO "ZAHRA" PERSONAL LIBRARY ')
    while True:
        menu_selection = int(input('please chose from: \n 1-add media type\n 2-show library\n '
                                   '3-more read \n 4-more listened\n 5-show progress\n 6-quit\n Enter here:'))
        if menu_selection == 1:
            add = input(
                'Enter your choice from (book),(magazine),(podcast episode),(audiobook) ) here:\n').lower()
            if add == 'book':
                num_book = int(input('Enter the number  of books here:\n'))
                for i in range(num_book):
                    Book.get_data(i)

            elif add == 'magazine':
                num_magazine = int(
                    input('Enter the number  of magazine here:\n'))
                for i in range(num_magazine):
                    Magazine.get_data(i)

            elif add == 'podcast episode':
                num_podcast = int(
                    input('Enter the number  of podcast_episode here:\n'))
                for i in range(num_podcast):
                    PodcastEpisode.get_data(i)

            elif add == 'audiobook':
                num_audiobook = int(
                    input('Enter the number  of audio books  here:\n'))
                for i in range(num_audiobook):
                    AudioBook.get_data(i)

            else:
                print('something went wrong zahra ENTER again :')

        elif menu_selection == 2:
            if not library:
                print('library is empty First add something')
            else:
                print([item.__str__() for item in library])

        elif menu_selection == 3:
            read_media_type = input('from book  or magazine ').lower()
            if read_media_type == 'book':
                print([item.title for item in book_list])
                print([item.pages for item in book_list])
                chose_book = input('from book list chose the book:').lower()
                for item in book_list:
                    if item.title == chose_book:
                        more_read_page = int(
                            input('enter the number of more  pages you read here:'))
                        item.get_status(more_read_page)
                        item.read(more_read_page)

            else:
                print([item.title for item in magazine_list])
                print([item.pages for item in magazine_list])
                chose_magazine = input(
                    'from magazine list chose the magazine:').lower()
                for item in magazine_list:
                    if item.title == chose_magazine:
                        more_read_page = int(
                            input('enter the number of more  pages you read here'))
                        item.get_status(more_read_page)
                        item.read(more_read_page)

                    else:
                        print('sth wrong')

        elif menu_selection == 4:
            listened_media_type = input('from podcast_episode  or audiobook ').lower()
            if listened_media_type == 'book':
                print([item.title for item in podcast_episode_list])
                print([item.time for item in podcast_episode_list])
                chose_podcast = input('from podcast_list chose the podcast :').lower()
                for item in podcast_episode_list:
                    if item.title == chose_podcast:
                        more_listened_podcast = int(input('enter the minutes you listened more  here:'))
                        item.get_status(more_listened_podcast)
                        item.listen(more_listened_podcast)

            else:
                print([item.title for item in audio_book_list])
                print([item.time for item in audio_book_list])
                chose_audiobook = input('from audio_book_list chose the audio_book:').lower()
                for item in audio_book_list:
                    if item.title == chose_audiobook:
                        more_minutes_audio = int(input('enter the minutes you listened more  here:'))
                        item.get_status(more_minutes_audio)
                        item.listen(more_minutes_audio)

        elif menu_selection == 5:
            sorted_library(library, 'progress', True)

        elif menu_selection == 6:
            print('bye bye zahra have a good day')
            break
        else:
            print('wrong number zahra chose again !!!!')

else:
    print('system didnt recognize the user_name or password enter again!')
