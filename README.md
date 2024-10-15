Programmering 

Oppgave 1 - Dictionaries 

Lag en dictionary med informasjon om en student: 

student = { 
    "first name" : "Ola", 
    "last name" : "Nordmann,
    "favourite course" : "Programmering 1" 
} 

    Skriv ut studentens fullstendige navn (fornavn og etternavn). 
    Programmatisk endre studentens favorittkurs til å inkludere kursets emnekode: "ITF10219 Programmering 1"
    Programmatisk legg til en alder for studenten i dictionarien. Du kan selv velge hva alderen skal være.

Oppgave 2 – Funksjon - Tallgenerering 

Definer en funksjon som lager en fin utskrift med et tilfeldig generert tall mellom 0 og 100 (husk at du kan benytte random.randrange()). Funksjonen skal ikke ta noen parametere. Eksempelutskrift: 

********* 

***97*** 

********* 

Kall denne funksjonen noen ganger. 

 

Oppgave 3 – Funksjon – Printe liste 

Definer en funksjon som heter print_list(). Denne funksjonen skal ta i mot en liste som parameter, og printe ut hvert element i denne listen en etter en. Lag deretter kort liste med dine 3 favorittmatretter, og kall funksjonen din med denne listen som parameter.

 

Oppgave 4 – Funksjon – Volum

Lag en funksjon for å regne ut volumet av et tredimensjonalt objekt. Vi lar ting være enkelt og forholder oss bare til enkle verdier for lengde, bredde og høyde. Volumet kan da beregnes med følgende formel: lengde*bredde*høyde. Du skal ta lengden, bredden og høyden som individuelle input-parametere for funksjonen, og returnere volumet. Kall funksjonen noen ganger med forskjellige verdier for lengde, bredde og høyde, og skriv ut resultatet av hver utregning.

 

Oppgave 5.1 - Dictionaries og Funksjoner 

A) Opprett en liste med filmer (hvor hver film er en egen dictionary med dataene om én film). Dataene om en film skal minst være: name, year og rating. Legg til filmene: 

        Inception – 2010 – 8.7 
        Inside Out – 2015 – 8.1 
        Con Air – 1997– 6.9  

B) Opprett en funksjon som legger til en film i filmlisten. Denne funksjonen skal være definert slik at den minst tar følgende parametere: 

    Listen filmen skal legges til i 
    name 
    year 
    rating 

 Benytt funksjonen til å legge til 3 filmer du selv bestemmer. 

C) Modifiser funksjonen fra forrige deloppgave til å sette default-ratingen til 5.0 hvis det ikke gis noen rating som argument til funksjonen. Test at dette fungerer ved å legge til en film uten å spesifisere dens rating. 

 

Oppgave 5.2 - Mer funksjoner 

Utvid forrige oppgave med noen funksjoner og benytt dem i koden din. 

A) Lag en funksjon som printer ut alle filmene i en gitt liste med filmer slik at formatet for hver filmutskrift blir seende slik ut: 

The Lion King - 1994 has a rating of 8.5 

 

B) Lag en funksjon som tar en liste med filmer som parameter og regner ut gjennomsnittsratingen for alle filmene i lista og returnerer dette. Test funksjonen og skriv ut gjennomsnittet. 
 

C) Lag en funksjon som tar en liste med filmer og et årstall som parametere, og returnerer en ny liste med alle filmer fra og med det gitte årstallet. 
Benytt funksjonen, og print ut informasjon om alle filmer fra og med 2010 (Kan vi  bruke en av funksjonene vi har laget tidligere til å hjelpe oss med noe av dette?). 

 

Oppgave 5.3 – Skrive/lese til fil 

Utvid forrige oppgave med noen funksjoner og benytt dem i koden din. 

A) Opprett en funksjon som tar en liste med filmer, og filnavn som parameter. Benytt denne funksjonen til å skrive alle filmene i lista til en fil du selv velger navnet på f.eks. "movies.txt". Hvis filen allerede eksisterer, skal den overskrives. Legg gjerne til hver film som en egen linje i filen med et fint format. For eksempel: 

The Lion King - 1994 has a rating of 8.5 

B) Lag en funksjon som leser den samme filen (filnavn som input-parameter til funksjonen) og skriver ut innholdet til terminalen.

 
Bonusoppgaver

Bonusoppgave 1 - Funksjonsparamatere

 Modifiser funksjonen du opprettet i Oppgave 5.1B) til å også kunne håndtere endring og fjerning av elementer. Gjør dette ved å legge til en ekstra parameter som kan benyttes for å spesifisere hvilken operasjon som ønskes å bli gjort. For eksempel: "a" - add, "c" - change, "r" - remove. Du står fritt til å håndtere dette som du selv ønsker. Sett standardverdien for denne parameteren til tilsvare operasjonen for å legge til elementer. 

 

Bonusoppgave 2 - Fil-modul

Opprett en python-fil med navnet, "file_handler.py". I denne oppgaven skal du gjøre denne filen til en modul for å håndtere lesing og skriving til fil (den vil bare inneholde funksjoner).

A) Opprett funksjoner for å skrive en liste til fil.

B) Lese fra en fil og legge innholdet i en liste

C) Skrive en dictionary til en fil i JSON-fromat

D) Lese fra en fil i JSON-format og legg dataen inn i en dictionary

 

Bonusoppgave 3 - Benytt modul

Benytt modulen du laget i forrige oppgave og test ut de forskjellige funksjonene.
