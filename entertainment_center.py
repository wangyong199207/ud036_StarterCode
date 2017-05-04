import movie
import fresh_tomatoes

avatar = movie.Movie("Avatar", 
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = movie.Movie("School of Rock", 
                     "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "http://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = movie.Movie("Ratatouille", 
                     "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "http://www.youtube.com/watch?v=c3sBBRxDAqk")

movies = [avatar, school_of_rock, ratatouille]

fresh_tomatoes.open_movies_page(movies)


