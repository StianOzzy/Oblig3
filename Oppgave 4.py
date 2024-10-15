# 1 Lag en funksjon for å regne ut volumet av et tredimensjonalt objekt.
# Du skal ta lengden, bredden og høyden som individuelle input-parametere
# for funksjonen, og returnere volumet.

def volume_calculation(obj_width,obj_height,obj_depth):
    volume = obj_width*obj_height*obj_depth
    return volume


# 2 Kall funksjonen noen ganger med forskjellige verdier for lengde, bredde og høyde,
# og skriv ut resultatet av hver utregning.

print("Volume of a 1x2x3 object:",volume_calculation(1,2,3))
print("Volume of a 2x3x4 object:",volume_calculation(2,3,4))
print("Volume of a 3x4x5 object:",volume_calculation(3,4,5))

# I denne while-loopen, så får brukeren muligheten til å  skrive ut så mange ganger
# som han/hun måtte ønske.
while True:
    print("\n")
    obj_width = int(input("What is the width of the object?\n\n>"))
    obj_height = int(input("What is the height of the object?\n\n>"))
    obj_depth = int(input("What is the depth of the object?\n\n>"))

    print("\nTotal volume of the object is:" , volume_calculation(obj_width,obj_height,obj_depth))
    retry = input("\n\nWould you like to try again? y/n\n\n>")
    if retry == "y":
        continue
    elif retry == "n":
        break
