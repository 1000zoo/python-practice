class Movie:
    def __init__(self, title, year, grade):
        self.title = title
        self.year = year
        self.grade = grade
        
movie1 = Movie("Iron Man", 2010, 5)
movie2 = Movie("Endgame", 2019, 5)

print("Title: {0}, year: {1}".format(movie1.title,  movie1.year))
print("Title: {0}, year: {1}".format(movie2.title,  movie2.year))

movie2.director = "Kevin"

print("Title: {0}, Director: {1}".format(movie2.title, movie2.director))