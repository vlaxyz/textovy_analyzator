"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Vlasta Pospěchová
email: pospechovavla@gmail.com
discord: Vlasta P#0037
"""

TEXTS = ["""
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,

"""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",

"""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""
]

registrovani_uzivatele = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}
oddelovac = "-" * 40
while True:
    uzivatel = input("username: ")
    if not uzivatel:
        print(f"Empty input. Try again...")
    else:
        break
while True:
    heslo = input("password: ")
    if not heslo:
        print(f"Empty input. Try again...")
    else:
        break
print(oddelovac)
if heslo == str(registrovani_uzivatele.get(uzivatel)):
    print(f"Welcome to the app, {uzivatel.title()}")
else:
    print(f"Unregistered user, terminating the program.")
    exit()
print(f"We have {len(TEXTS)} texts to be analyzed.")
print(oddelovac)
vybrany_text = 0
while True:
    vyber = input("Enter a number btw. 1 and 3 to select: ")
    if not vyber:
        print(f"Empty input. Try again...")
    else:
        break
if vyber.isnumeric():
    vyber = int(vyber)
    if vyber < 1 or vyber > 3:
        print(f"{vyber} is not btw numbers 1-3. Ending app...")
        exit()
    else:
        vybrany_text = TEXTS[vyber - 1]
elif '-' in vyber:
    vyber = vyber.replace("-","")
    if vyber.isnumeric():
        vyber = int(vyber)
        vyber *= -1
        print(f"{vyber} is a negative number. Ending app...")
        exit()
else:
    print(f"{vyber} is not a number. Ending app...")
    exit()
rozdeleny_text = vybrany_text.split()
ocisteny_text = [slovo.strip("',.?!") for slovo in rozdeleny_text]
delka = [len(slovo) for slovo in ocisteny_text]
prvni_velke = [slovo for slovo in ocisteny_text if slovo.istitle() and slovo.isalpha()]
velka_pismena = [slovo for slovo in ocisteny_text if slovo.isupper() and slovo.isalpha()]
mala_pismena = [slovo for slovo in ocisteny_text if slovo.islower() and slovo.isalpha()]
pocet_cisel = [slovo for slovo in ocisteny_text if slovo.isnumeric()]
suma_cisel = [int(cislo) for cislo in pocet_cisel]
print(oddelovac)
print(f"There are {len(delka)} words in the selected text.")
print(f"There are {len(prvni_velke)} titlecase words.")
print(f"There are {len(velka_pismena)} uppercase words.")
print(f"There are {len(mala_pismena)} lowercase words.")
print(f"There are {len(pocet_cisel)} numeric strings.")
print(f"The sum of all the numbers {sum(suma_cisel)}.")
print(oddelovac)
print(f"LEN | OCCURENCES | NR.")
hvezdicka = "*"
mezera = " "
cisla = set(delka)
frekvencni_cisla = []
for cislo in cisla:
    frekvencni_cisla.append(delka.count(cislo))
nejvyssi_cislo = max(frekvencni_cisla)
for pocet in cisla:
    pocet_mezer= nejvyssi_cislo - delka.count(pocet)
    print(f"{pocet} | {hvezdicka * delka.count(pocet)} {mezera * pocet_mezer} | {delka.count(pocet)}")