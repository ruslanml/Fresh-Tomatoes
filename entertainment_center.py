import fresh_tomatoes
import media


edge_of_tomorrow = media.Movie(
    "Edge of Tomorrow",
    "A soldier fighting aliens ge"
    "ts to relive the same day over and over again, "
    "the day restarting every time he dies.",
    "http://ia.media-imdb.com/images/M/MV5BMTc5OTk4MTM3M15BMl5BanBnXkFtZTgwODcxNjg3MDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=vw61gCe2oqI")
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
interstellar = media.Movie(
    "Interstellar",
    "A team of explorers travel through a "
    "wormhole in space in an attempt to ensure humanity's survival. ",
    "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=2LqzF5WauAw")
inception = media.Movie(
    "Inception",
    "A thief, who steals corporate secrets through use "
    "of dream-sharing technology, is given the inverse task of planting "
    "an idea into the mind of a CEO.",
    "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=66TuSJo4dZM")
prometheus = media.Movie(
    "Prometheus",
    "Following clues to the origin of mankind a team journey "
    "across the universe and find a structure on a distant planet containing a "
    "monolithic statue of a humanoid head and stone cylinders of alien blood but"
    " they soon find they are not alone.",
    "http://ia.media-imdb.com/images/M/MV5BMTY3NzIyNTA2NV5BMl5BanBnXkFtZTcwNzE2NjI4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=nmJOO6D5RvA")

# create an array with all of the movies
movies = [edge_of_tomorrow, avatar, interstellar, inception, prometheus]

# display all movies in the movies array on the web page
fresh_tomatoes.open_movies_page(movies)
