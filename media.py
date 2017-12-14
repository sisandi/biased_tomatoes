"""
This module holds the class data structure for a Movie object.
Based on a tutorial from Udacity's Full Stack Development course.
"""


import webbrowser


class Movie(object):
    """
    Movie class object stores information and related media about one movie.

    Attributes:
        title (str): Title of the movie e.g. Forrest Gump
        storyline (str): Short synopsis of the movie
        poster_image_url (str): url path or link to the movie poster art
        trailer_youtube_url (str): url path or link to the movie's trailer on YouTube
    """

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def __repr__(self):
        return '{}: {}'.format(self.title, self.storyline)

    def show_trailer(self):
        """Opens and plays movie's trailer video"""

        webbrowser.open(self.trailer_youtube_url)

