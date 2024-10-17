# 5.1 B) 1/3
def get_movie_parameters():
    movie_list = input("Enter list to add movie to:\n\n>")
    movie_title = input("Enter movie title:\n\n>")
    movie_year = input("Enter movie year:\n\n>")
    movie_rating = (float(input("Enter movie rating:\n\n>")))
    return movie_list, movie_title, movie_year, movie_rating

# 5.1 B) 2/3 & 5.1 C) 1/2
def add_movie(movie_list, movie_title, movie_year, movie_rating="5.0"):
    movie_list.append({"title": movie_title, "year": movie_year, "rating": movie_rating})
    print(movie_title,"added to the list.")

def print_movies(movie_list):
    print("\nCurrent items in list:")
    for i in range(len(movie_list)):
        print("\n",i+1,"-", movie_list[i])
    print("\n\n")

# A) Lag en funksjon som printer ut alle filmene i gitt format
def print_formatted_list(list_of_movies):
    for movies in list_of_movies:
        print(f"\n{list_of_movies["title"]} - {list_of_movies["year"]} has a rating of {list_of_movies["rating"]}")

# B) Lag en funksjon regner ut gjennomsnittsratingen for alle filmene i lista, og returnerer dette
def movie_average_rating(list_of_movies):
    sum_of_ratings = 0
    for movie in list_of_movies:
        movierating = float(movie["rating"])
        sum_of_ratings += movierating
    print("Average rating of the list:",round(sum_of_ratings/len(list_of_movies),1))
    return round(sum_of_ratings/len(list_of_movies),1)

#----------------------------------------------

# 5.1 A)
movies1 = []
add_movie(movies1,"Inception","2010", "8.7")
add_movie(movies1,"Inside Out","2015", "8.1")
add_movie(movies1,"Con Air","1997","6.9")
print_movies(movies1)

# 5.1 B) 3/3
movies2 = []
add_movie(movies2,"Léon: The Professional","1994","8.5")
add_movie(movies2,"Raiders of the Lost Ark","1981","8.4")
add_movie(movies2,"The Room","2004","3.6")
print_movies(movies2)

# 5.1 C) 2/2
add_movie(movies2,"Joker: folie a deux","2003",)
print_movies(movies2)

#print("\nA)")
#print_formatted_list(movies1)

print("\nB) Movies Average")
movie_average_rating(movies1)

while True:
    go = input("\nDo you want to add a movie? y/n\n\n>")
    if go == "y":
        movie_title, movie_year, movie_rating = get_movie_parameters()
        add_movie(movie_title, movie_year, movie_rating)
        print_movies()
        continue
    elif go == "n":
        print("Exiting...")
        break