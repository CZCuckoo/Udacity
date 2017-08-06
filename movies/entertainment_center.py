#!/usr/bin/env python

"""This file is the main file to be run for our fresh tomatoes site.
It brings in the class Movie from media.py, and runs fresh_tomatoes.py
to get the html necessary to run the project. It creates instances of
the class Movie"""

import media
import fresh_tomatoes

fury_road = media.Movie("Mad Max: Fury Road",
                        "In a post apocalyptic world, two people struggle to "
                        "escape a warlord",
                        "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",  # NOQA
                        "https://youtu.be/hEJnMQG9ev8")

blade_runner = media.Movie("Blade Runner",
                           "A bounty hunter seeks out robotic 'replicants' "
                           "learns more about his prey, and questions his job.",
                           "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",  # NOQA
                           "https://youtu.be/eogpIG53Cis")

force_awakens = media.Movie("Star Wars: The Force Awakens",
                            "A young woman discovers she is strong in the force.",
                            "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",  # NOQA
                            "https://youtu.be/sGbxmsDFVnE")

aliens = media.Movie("Aliens",
                     "A team of marines discover investigate a planet and get "
                     "more than they anticipated",
                     "https://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg",  # NOQA
                     "https://youtu.be/W857ys3BlRI")

princess_bride = media.Movie("The Princess Bride",
                             "A young child, home from school, bonds with his "
                             "grandfather as he is read a story",
                             "https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",  # NOQA
                             "https://youtu.be/VYgcrny2hRs")

arrival = media.Movie("The Arrival",
                      "A translator must quickly learn an alien language to "
                      "stop violence.",
                      "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg",  # NOQA
                      "https://youtu.be/tFMo3UJ4B4g")

movies = [fury_road, blade_runner, force_awakens, aliens, princess_bride,
          arrival]

fresh_tomatoes.open_movies_page(movies)
