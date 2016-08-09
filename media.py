import webbrowser

class Movie() :
    """This class provides a way to store movie related information
    
    Attributes:
        movie_title(str): This is the title of the movie
        movie_storyline(str): This is the description of the Movie
        poster_image(str): This is a link to the cover image
        trailer_youtube(str): This is the link to the trailer on Youtube
    Methods
        show_trailer: Opens a web browser and displays the youtube trailer.
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)