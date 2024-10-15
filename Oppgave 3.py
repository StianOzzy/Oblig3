
# 1 Definer en funksjon som heter print_list().
# Denne funksjonen skal ta i mot en liste som parameter,
# og printe ut hvert element i denne listen en etter en.

def print_list(list):
    for element in enumerate(list):
        print(element)


# 2 Lag deretter en kort liste med dine 3 favorittmatretter

fav_retter = ("Pizza", "Kylling-gryte", "Laks")


# 3 Kall funksjonen din med denne listen som parameter.

print_list(fav_retter)