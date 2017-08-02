import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")

print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg", "https://youtu.be/d1_JBMrrYw8")

force_awakens = media.Movie("Star Wars: The Force Awakens", "A young woman discovers she is strong in the force.", "https://en.wikipedia.org/wiki/Star_Wars:_The_Force_Awakens#/media/File:Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg", "https://youtu.be/sGbxmsDFVnE") 

print(avatar.storyline)

#avatar.show_trailer()

print(force_awakens.storyline)

force_awakens.show_trailer()
