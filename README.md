# biased_tomatoes
This ia a library for generating an html page of a collection of movie posters, their synopses, and their trailers ready for playback. This is a project based on the starter code from Udacity's [ud036_StarterCode](https://github.com/udacity/ud036_StarterCode.git)


## How to Run
```
 $ python entertainment_center.py
```
### Sample movie web page

Render fresh_tomatoes.html

## Adding Movies

### From source code

To add a new movie for display on the web page, instantiate a new movie variable with the Movie object constructor from media.py. Be sure to add this new movie variable to the list of my_movies.

For example:
```
stranger_than_fiction = media.Movie(
    movie_title="Stranger than Fiction",
    movie_storyline="An average IRS agent Harold Crick finds himself in a narrated, parallel reality of novelist Kay's latest fictional work",
    poster_image="https://daveexaminesmovies.files.wordpress.com/2013/06/strangerfictionposter.jpg?w=849",
    trailer_youtube="https://www.youtube.com/watch?v=7dnbt5cuunc")
.
.
.
my_movies = [..., ..., stranger_than_fiction]
```

## License
This repository is under the MIT license.
