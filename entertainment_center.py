
import media
import fresh_tomatoes

# Construct 6 movie instance
infernal_affairs3 = media.Movie("Infernal Affairs 3",
                                "A story about hongkong police"
                                " and gangsterdom",
                                "https://upload.wikimedia.org/wikipedia/en/6/6d/Infernal_Affairs_3.jpg", # NOQA
                                "https://www.youtube.com/watch?v=9EjS2fk2bb4")

infernal_affairs2 = media.Movie("Infernal Affairs 2",
                                "A story about hongkong police"
                                " and gangsterdom",
                                "https://upload.wikimedia.org/wikipedia/en/5/5a/Infernal_Affairs_II.jpg", # NOQA
                                "https://www.youtube.com/watch?v=TaDUZskpMfM")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "A story about how banker"
                                       " Andy Dufresne escape from jail",
                                       "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg", # NOQA
                                       "https://www.youtube.com/watch?v=zdWZBvd0-pg") # NOQA

the_terror_live = media.Movie("The Terror Live",
                              "A story about a live broadcast"
                              " of a terrorist attack",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/e/ea/The_Terror%2C_LIVE_poster.jpg/440px-The_Terror%2C_LIVE_poster.jpg", # NOQA
                              "https://www.youtube.com/watch?v=e_FSvAQMGNc")

the_dark_knight = media.Movie("The Dark Knight",
                        "The second part of Nolan's The Dark Knight Trilogy."
                        "Batman against the Joker",
                        "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", # NOQA
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", # NOQA
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# make the movie objects into a iterable list
movies = [the_terror_live, infernal_affairs3,
          infernal_affairs2, the_shawshank_redemption,
          the_dark_knight, avatar]

# creat a html file through open_movies_page defined in fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
