"""
This module centralizes all movies that
a user wants published on a web page,
generates an html with all the movie data, and
launches the html in a web browser
"""

import media
import fresh_tomatoes


# Instantiate movie objects with title, storyline,
# poster art url, and trailer url
devil_wears_prada = media.Movie(
    "The Devil Wears Prada",
    """A young, ambitious journalist makes her career start
    in NYC, navigating the world of high fashion as the new
    assistant of Runway's famous editor-in-chief""",
    "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Devil_Wears_Prada_main_onesheet.jpg",  # Noqa
    "https://www.youtube.com/watch?v=XTDSwAxlNhc")

dr_strange = media.Movie(
    "Doctor Strange",
    """How an arrogant doctor who lost his ability to heal
    unlocked his superhero potential""",
    "https://vignette.wikia.nocookie.net/marveldatabase/images/a/a0/Doctor_Strange_%28film%29_poster_006.jpg/revision/latest?cb=20160927161946",  # Noqa
    "https://www.youtube.com/watch?v=HSzx-zryEgM")

infernal_affairs = media.Movie(
    "Infernal Affairs",
    """An undercover cop serving as intelligence for Hong
    Kong's Narcotics Bureau goes against an undercover
    triad memeber serving as counter intelligence as an NB officer""",
    "https://upload.wikimedia.org/wikipedia/en/thumb/9/98/IAmoviepost.jpg/220px-IAmoviepost.jpg",  # Noqa
    "https://www.youtube.com/watch?v=VUMRXkYx4MQ")

easy_a = media.Movie(
    "Easy A",
    """A high school girl finds herself in the middle of
    a scandal after starting a rumor to help out a friend""",
    "http://www.sonypictures.com/movies/easya/assets/images/onesheet.jpg",
    "https://www.youtube.com/watch?v=QZ4EwBtyfaA")

good_will_hunting = media.Movie(
    "Good Will Hunting",
    """A gifted mind of a young janitor Will Hunting is given
    the chance to exercise his genius and to truly find himself
    along the way""",
    "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",  # Noqa
    "https://www.youtube.com/watch?v=PaZVjZEFkRs")

stranger_than_fiction = media.Movie(
    "Stranger than Fiction",
    """An average IRS agent Harold Crick finds himself in
    a narrated, parallel reality of novelist Kay's latest
    fictional work""",
    "https://daveexaminesmovies.files.wordpress.com/2013/06/strangerfictionposter.jpg?w=849",  # Noqa
    "https://www.youtube.com/watch?v=7dnbt5cuunc")

# A list to store all movie objects to be published to an html web page
my_movies = [
    devil_wears_prada,
    dr_strange,
    infernal_affairs,
    stranger_than_fiction,
    easy_a,
    good_will_hunting
]

# Generate and open movie trailers web page
fresh_tomatoes.create_movie_tiles_content(my_movies)
fresh_tomatoes.open_movies_page(my_movies)
