import webbrowser


class Movie():
    """This class provides a way to store information of a movie

    Attributes:
        title: A string that store the name of the moive
        storyline: A string A brief
        poster_image_url: A string
        trailer_youtube_url: A string the youtube trailer
    """

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']   # Class Variable

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
