
# B) Opprett en funksjon som legger til en film i filmlisten.
def add_movie():
    movie_title = input("Enter movie title:\n\n>")
    movie_year = input("Enter movie year:\n\n>")
    movie_rating = input("Enter movie rating:\n\n>")
# C) Modifiser funksjonentil å sette default-ratingen til 5.0
#    hvis det ikke gis noen rating som argument til funksjonen.
    if movie_rating == "":
        movie_rating = 5.0
    movies.append({"title": movie_title, "year": movie_year, "rating": movie_rating})
    print("Movie added.")


# A) Opprett en liste med filmer.
movies = [{"title": "Inception", "year": "2010", "rating": "8.7"},
            {"title": "Inside Out", "year": "2015", "rating": "8.1"},
            {"title": "Con Air", "year": "1997", "rating": "6.9"}]

print("Movies:", movies, "\n")

add_movie()

while True:
    add_movie()
    print("Movies:",movies, "\n")
    go = input("Do you want to add a movie? y/n\n\n>")
    if go == "y":
        continue
    elif go == "n":
        break