
def student_navn():
    print(student["first_name"], student["last_name"])

#------------------------------------------------------

# 1 Lag en dictionary med informasjon om en student:
student = { "first_name": "Ola",
            "last_name": "Nordmann",
            "favourite_course": "Programmering 1" }

# 2 Skriv ut studentens fullstendige navn. Se def av funksjon i linje 2
student_navn()

# 3 Endre studentens favorittkurs til å inkludere emnekoden: "ITF10219 Programmering 1"
student["favourite_course"] = "ITF10219 Programmering 1"

# 4 Legg til en alder for studenten i dictionariet.
student["age"] = "22"

# Skriver ut, og bekrefter at alt ble lagt inn i henhold til oppgavetekst.
print(student)