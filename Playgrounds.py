
# 5.1 B) 1/3 & 5.1 C) 1/2
# Add movies to a list with specified parameters.
def add_movie(movie_list, movie_title, movie_year, movie_rating="5.0"):
    movie_list.append({"title": movie_title, "year": movie_year, "rating": movie_rating})
    print(movie_title,"added to",get_list_name(movie_list))

# 5.1 B) 2/3
# Get movie parameters from user inputs.
def get_movie_parameters():
    movie_list = input("Enter list to add movie to:\n\n>")
    movie_title = input("Enter movie title:\n\n>")
    movie_year = input("Enter movie year:\n\n>")
    movie_rating = (float(input("Enter movie rating:\n\n>")))
    return movie_list, movie_title, movie_year, movie_rating

# Print lists to console, to check current items.
def print_movies(movie_list):
    print("\nCurrent items in",get_list_name(movie_list))
    for i in range(len(movie_list)):
        print("\n",i+1,"-", movie_list[i])
    print("\n\n")

# Get "list names" as strings (for prints to console)
def get_list_name(movie_list):
    for name, value in globals().items():
        if value is movie_list:
            return name

#----------------------------------------------

# 5.1 A)
movies_1 = []
add_movie(movies_1,"Inception","2010", "8.7")
add_movie(movies_1,"Inside Out","2015", "8.1")
add_movie(movies_1,"Con Air","1997","6.9")
print_movies(movies_1)

# 5.1 B) 3/3
movies_2 = []
add_movie(movies_2,"Léon: The Professional","1994","8.5")
add_movie(movies_2,"Raiders of the Lost Ark","1981","8.4")
add_movie(movies_2,"The Room","2004","3.6")
print_movies(movies_2)

# 5.1 C) 2/2
add_movie(movies_2,"Joker: folie a deux","2003",)
print_movies(movies_2)

# Mulighet for å legge til filmer fra konsoll er kommentert ut, da oppg ikke spørr om dette.
"""
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
"""