import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://youtu.be/d1_JBMrrYw8")

force_awakens = media.Movie("Star Wars: The Force Awakens", "A young woman discovers she is strong in the force.", "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg", "https://youtu.be/sGbxmsDFVnE")

aliens = media.Movie("Aliens", "A team of marines discover investigate a planet and get more than they anticipated", "https://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg", "https://youtu.be/W857ys3BlRI")

princess_bride = media.Movie("The Princess Bride", "A young child, home from school, bonds with his grandfather as he is read a story", "https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg", "https://youtu.be/VYgcrny2hRs")

arrival = media.Movie("The Arrival", "A translator must quickly learn an alien language to stop violence.", "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg", "https://youtu.be/tFMo3UJ4B4g")



movies = [toy_story, avatar, force_awakens, aliens, princess_bride, arrival]

fresh_tomatoes.open_movies_page(movies)
