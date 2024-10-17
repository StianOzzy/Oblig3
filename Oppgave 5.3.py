
# 5.1 A) 1/2    |  5.1 B) 1/2   |  5.1 C) 1/2
# Add movies to a list with the specified parameters.
def add_movie(movie_list, movie_title, movie_year, movie_rating="5.0"):
    movie_list.append({"title": movie_title, "year": movie_year, "rating": movie_rating})
    print(movie_title,"- added to",get_list_name(movie_list))

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

# 5.2 A) 1/2
def print_formatted_list(movie_list):
    for movie in movie_list:
        print(f"{movie["title"]} - {movie["year"]} has a rating of {movie["rating"]}")

# 5.2 B) 1/2
def average(movie_list):
    totalscore = 0
    for movie in movie_list:
        totalscore += float(movie["rating"])
    return round(totalscore/len(movie_list),1)

# 5.2 C) 1/2
def movies_from_year(movie_list,movie_year):
    for movie in movie_list:
        if movie["year"] >= movie_year:
            print(movie["title"],"(",movie["year"],")","released was released after",int(movie_year)-1)

# 5.3 A) 1/2
def write_to_file(movie_list,file_name):
    with open(file_name,"w") as file:
        file.write("List:\n")
        for movie in movie_list:
            line = f"{movie["title"]} - {movie["year"]} has a rating of {movie["rating"]}\n"
            file.write(line)

# 5.3 B) 1/2
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            the_list = file.read()
            print(the_list)
    except FileNotFoundError:
        print(f"File {file_name} not found")

#----------------------------------------------

# 5.1 A) 2/2
movies_1 = []
add_movie(movies_1,"Inception","2010", "8.7")
add_movie(movies_1,"Inside Out","2015", "8.1")
add_movie(movies_1,"Con Air","1997","6.9")
print_movies(movies_1)

# 5.1 B) 2/2
movies_2 = []
add_movie(movies_2,"Léon: The Professional","1994","8.5")
add_movie(movies_2,"Raiders of the Lost Ark","1981","8.4")
add_movie(movies_2,"The Room","2004","3.6")

# 5.1 C) 2/2
add_movie(movies_2,"Joker: folie a deux","2024",)
print_movies(movies_2)

# 5.2 A) 2/2
print_formatted_list(movies_1)
print("\n")
print_formatted_list(movies_2)

# 5.2 B) 2/2
print("\nThe average rating of all movies in",get_list_name(movies_1),"is",average(movies_1))
print("\nThe average rating of all movies in",get_list_name(movies_2),"is",average(movies_2))

# 5.2 C) 2/2
print("\n")
movies_from_year(movies_1,"2010")
print("\n")

# 5.3 A) 2/2
write_to_file(movies_1,"movies_1.txt")

# 5.3 B) 2/2
read_file("movies_1.txt")

# Mulighet for å legge til filmer fra konsoll er kommentert ut, da oppgaven ikke spørr om dette
# Brukt til feilsøking under
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