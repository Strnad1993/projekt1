# Text, který určí celý projekt
'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# Registrovaní uživatelé
# Slovník, jen verze jak bude vypadat slovník registrovaných uživatelů. registr = {"USER":"PASSWORD"}
# Skutečný registr zaregistrovaných uživatelů a jejich hesel
registr = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
# ODDĚLOVAČ pro budoucí potřeby
oddelovac = "-" * 40
# SYMBOL pro potřeby grafů
symbol = "*"
# Vstup uživatele
# Vložení uživatelského jména a hesla + oddělení sekce
username = input("Username: ")
password = input("Password: ")
print(oddelovac)

# Kontrola uživatelského jména a hesla po zadání vstupu od uživatele
if registr.get(username) == password:
    print(f"Welcome to the app, {username} \nWe have {len(TEXTS)} texts to be analyzed.")
    print(oddelovac)
else:
    print("We are sorry, but only registered users can log in. If you are registered, you have entered the wrong username or password.")
    exit()

# po přihlášení - výběr analyzovaného textu. Od 1 do 3. + oddělení sekce
vyber = input("Enter a number btw. 1 and 3 to select: ")
print(oddelovac)

# ANALÝZA 1. TEXTU
if vyber == "1":
    # TEXTS 1
    prevedeni = str(TEXTS[0])
    jednotliva_slova = TEXTS[0].split()
    # pocet slov a vyčištění od jiných znaků
    for slovo in jednotliva_slova:
        ciste_slovo = slovo.strip(",.!_?+-*/")

    vycistena_slova = [slovo.strip(",.!_?+-*/") for slovo in jednotliva_slova]
    # vycistena_slova = type(list)
    print("There are " + str(len(vycistena_slova)) + " words in the selected text.")
    # pomocné
    slovnik = {"začínající": 0, "velká": 0, "malá": 0, "cisla": 0}
    soucet = []
    # Slova začínající Velkým písmenem
    for znak in vycistena_slova:
        if znak.istitle():
            slovnik["začínající"] += 1
    print("There are " + str(slovnik["začínající"]) + " titlecase words.")
    # Jen Velká
    for znak in vycistena_slova:
        if znak.isalpha() and znak.isupper():
            slovnik["velká"] += 1
    print("There are " + str(slovnik["velká"]) + " uppercase words.")
    # Jen Malé
    for znak in vycistena_slova:
        if znak.islower():
            slovnik["malá"] += 1
    print("There are " + str(slovnik["malá"]) + " lowercase words.")
    # pocet cisel
    for znak in vycistena_slova:
        if znak.isdecimal():
            slovnik["cisla"] += 1
    print("There are " + str(slovnik["cisla"]) + " numeric strings.")
    # soucet cisel
    for i in vycistena_slova:
        if i.isnumeric():
            i = int(i)
            soucet.append(i)
    print("The sum of all the numbers ", sum(soucet), ".", sep="")
    print(oddelovac)
    # GRAF
    print("LEN|  OCCURENCES\t|NR.")
    print(oddelovac)
    slovnik_znaky = {"jedna": 0, "dva": 0, "tri": 0, "ctyri": 0, "pet": 0, "sest": 0, "sedm": 0, "osm": 0, "devet": 0,
                     "deset": 0, "jedenact": 0, "dvanact": 0, "trinact": 0, "ctrnact": 0, "patnact": 0}
    # Přiřazení DÉLEK znaku do slovníku k jednotlivé hodnotě
    for znak in vycistena_slova:
        if len(znak) == 1:
            slovnik_znaky["jedna"] += 1
        if len(znak) == 2:
            slovnik_znaky["dva"] += 1
        if len(znak) == 3:
            slovnik_znaky["tri"] += 1
        if len(znak) == 4:
            slovnik_znaky["ctyri"] += 1
        if len(znak) == 5:
            slovnik_znaky["pet"] += 1
        if len(znak) == 6:
            slovnik_znaky["sest"] += 1
        if len(znak) == 7:
            slovnik_znaky["sedm"] += 1
        if len(znak) == 8:
            slovnik_znaky["osm"] += 1
        if len(znak) == 9:
            slovnik_znaky["devet"] += 1
        if len(znak) == 10:
            slovnik_znaky["deset"] += 1
        if len(znak) == 11:
            slovnik_znaky["jedenact"] += 1
        if len(znak) == 12:
            slovnik_znaky["dvanact"] += 1
        if len(znak) == 13:
            slovnik_znaky["trinact"] += 1
        if len(znak) == 14:
            slovnik_znaky["ctrnact"] += 1
        if len(znak) == 15:
            slovnik_znaky["patnact"] += 1
    # Vypsání grafu
    if slovnik_znaky["jedna"] > 0:
        print("  1|"+str(slovnik_znaky["jedna"] * symbol)+ "\t\t\t\t|"+str(slovnik_znaky["jedna"]))

    if slovnik_znaky["dva"] > 0:
        print("  2|"+str(slovnik_znaky["dva"] * symbol)+"\t\t|"+str(slovnik_znaky["dva"]))

    if slovnik_znaky["tri"] > 0:
        print("  3|"+str(slovnik_znaky["tri"] * symbol)+"\t\t\t|"+str(slovnik_znaky["tri"]))

    if slovnik_znaky["ctyri"] > 0:
        print("  4|"+str(slovnik_znaky["ctyri"] * symbol)+"\t\t|"+str(slovnik_znaky["ctyri"]))

    if slovnik_znaky["pet"] > 0:
        print("  5|"+str(slovnik_znaky["pet"] * symbol)+"\t|"+str(slovnik_znaky["pet"]))

    if slovnik_znaky["sest"] > 0:
        print("  6|"+str(slovnik_znaky["sest"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["sest"]))

    if slovnik_znaky["sedm"] > 0:
        print("  7|"+str(slovnik_znaky["sedm"] * symbol)+"\t\t\t|"+str(slovnik_znaky["sedm"]))

    if slovnik_znaky["osm"] > 0:
        print("  8|"+str(slovnik_znaky["osm"] * symbol)+"\t\t\t|"+str(slovnik_znaky["osm"]))

    if slovnik_znaky["devet"] > 0:
        print("  9|"+str(slovnik_znaky["devet"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["devet"]))

    if slovnik_znaky["deset"] > 0:
        print(" 10|"+str(slovnik_znaky["deset"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["deset"]))

    if slovnik_znaky["jedenact"] > 0:
        print(" 11|"+str(slovnik_znaky["jedenact"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["jedenact"]))

    if slovnik_znaky["dvanact"] > 0:
        print(" 12|"+str(slovnik_znaky["dvanact"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["dvanact"]))

    if slovnik_znaky["trinact"] > 0:
        print(" 13|"+str(slovnik_znaky["trinact"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["trinact"]))

    if slovnik_znaky["ctrnact"] > 0:
        print(" 14|"+str(slovnik_znaky["ctrnact"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["ctrnact"]))

    if slovnik_znaky["patnact"] > 0:
        print(" 15|"+str(slovnik_znaky["patnact"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["patnact"]))

# ANALÝZA 2. TEXTU
elif vyber == "2":
    # TEXTS 2
    prevedeni2 = str(TEXTS[1])
    jednotliva_slova2 = TEXTS[1].split()
    # pocet slov a vyčištění od jiných znaků
    for slovo in jednotliva_slova2:
        ciste_slovo = slovo.strip(",.!_?+-*/")

    vycistena_slova2 = [slovo.strip(",.!_?+-*/") for slovo in jednotliva_slova2]
    # vycistena_slova = type(list)
    print("There are " + str(len(vycistena_slova2)) + " words in the selected text.")
    # pomocné
    slovnik2 = {"začínající": 0, "velká": 0, "malá": 0, "cisla": 0}
    soucet2 = []
    # Slova začínající Velkým písmenem
    for znak in vycistena_slova2:
        if znak.istitle():
            slovnik2["začínající"] += 1
    print("There are " + str(slovnik2["začínající"]) + " titlecase words.")
    # Jen Velká
    for znak in vycistena_slova2:
        if znak.isalpha() and znak.isupper():
            slovnik2["velká"] += 1
    print("There are " + str(slovnik2["velká"]) + " uppercase words.")
    # Jen Malé
    for znak in vycistena_slova2:
        if znak.islower():
            slovnik2["malá"] += 1
    print("There are " + str(slovnik2["malá"]) + " lowercase words.")
    # pocet cisel
    for znak in vycistena_slova2:
        if znak.isdecimal():
            slovnik2["cisla"] += 1
    print("There are " + str(slovnik2["cisla"]) + " numeric strings.")
    # soucet cisel
    for i in vycistena_slova2:
        if i.isnumeric():
            i = int(i)
            soucet2.append(i)
    print("The sum of all the numbers ", sum(soucet2), ".", sep="")
    print(oddelovac)

    # GRAF
    print("LEN|  OCCURENCES\t\t|NR.")
    print(oddelovac)
    slovnik_znaky = {"jedna": 0, "dva": 0, "tri": 0, "ctyri": 0, "pet": 0, "sest": 0, "sedm": 0, "osm": 0, "devet": 0,
                     "deset": 0, "jedenact": 0, "dvanact": 0, "trinact": 0, "ctrnact": 0, "patnact": 0}
    # Přiřazení DÉLEK znaku do slovníku k jednotlivé hodnotě
    for znak in vycistena_slova2:
        if len(znak) == 1:
            slovnik_znaky["jedna"] += 1
        if len(znak) == 2:
            slovnik_znaky["dva"] += 1
        if len(znak) == 3:
            slovnik_znaky["tri"] += 1
        if len(znak) == 4:
            slovnik_znaky["ctyri"] += 1
        if len(znak) == 5:
            slovnik_znaky["pet"] += 1
        if len(znak) == 6:
            slovnik_znaky["sest"] += 1
        if len(znak) == 7:
            slovnik_znaky["sedm"] += 1
        if len(znak) == 8:
            slovnik_znaky["osm"] += 1
        if len(znak) == 9:
            slovnik_znaky["devet"] += 1
        if len(znak) == 10:
            slovnik_znaky["deset"] += 1
        if len(znak) == 11:
            slovnik_znaky["jedenact"] += 1
        if len(znak) == 12:
            slovnik_znaky["dvanact"] += 1
        if len(znak) == 13:
            slovnik_znaky["trinact"] += 1
        if len(znak) == 14:
            slovnik_znaky["ctrnact"] += 1
        if len(znak) == 15:
            slovnik_znaky["patnact"] += 1
    # Vypsání grafu
    if slovnik_znaky["jedna"] > 0:
        print("  1|"+str(slovnik_znaky["jedna"] * symbol)+ "\t\t\t\t\t|"+str(slovnik_znaky["jedna"]))

    if slovnik_znaky["dva"] > 0:
        print("  2|"+str(slovnik_znaky["dva"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["dva"]))

    if slovnik_znaky["tri"] > 0:
        print("  3|"+str(slovnik_znaky["tri"] * symbol)+"\t|"+str(slovnik_znaky["tri"]))

    if slovnik_znaky["ctyri"] > 0:
        print("  4|"+str(slovnik_znaky["ctyri"] * symbol)+"\t\t\t|"+str(slovnik_znaky["ctyri"]))

    if slovnik_znaky["pet"] > 0:
        print("  5|"+str(slovnik_znaky["pet"] * symbol)+"\t\t\t|"+str(slovnik_znaky["pet"]))

    if slovnik_znaky["sest"] > 0:
        print("  6|"+str(slovnik_znaky["sest"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["sest"]))

    if slovnik_znaky["sedm"] > 0:
        print("  7|"+str(slovnik_znaky["sedm"] * symbol)+"\t\t\t\t\t|"+str(slovnik_znaky["sedm"]))

    if slovnik_znaky["osm"] > 0:
        print("  8|"+str(slovnik_znaky["osm"] * symbol)+"\t\t\t\t\t|"+str(slovnik_znaky["osm"]))

    if slovnik_znaky["devet"] > 0:
        print("  9|"+str(slovnik_znaky["devet"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["devet"]))

    if slovnik_znaky["deset"] > 0:
        print(" 10|"+str(slovnik_znaky["deset"] * symbol)+"\t\t\t\t\t|"+str(slovnik_znaky["deset"]))

    if slovnik_znaky["jedenact"] > 0:
        print(" 11|"+str(slovnik_znaky["jedenact"] * symbol)+"\t\t\t\t\t|"+str(slovnik_znaky["jedenact"]))

    if slovnik_znaky["dvanact"] > 0:
        print(" 12|"+str(slovnik_znaky["dvanact"] * symbol)+"\t\t\t\t\t|"+str(slovnik_znaky["dvanact"]))

    if slovnik_znaky["trinact"] > 0:
        print(" 13|"+str(slovnik_znaky["trinact"] * symbol)+"\t\t\t\t\t|"+str(slovnik_znaky["trinact"]))

    if slovnik_znaky["ctrnact"] > 0:
        print(" 14|"+str(slovnik_znaky["ctrnact"] * symbol)+"\t\t\t\t\t|"+str(slovnik_znaky["ctrnact"]))

    if slovnik_znaky["patnact"] > 0:
        print(" 15|"+str(slovnik_znaky["patnact"] * symbol)+"\t\t\t\t\t|"+str(slovnik_znaky["patnact"]))


# ANALÝZA 3. TEXTU
elif vyber == "3":
    # TEXTS 3
    prevedeni3 = str(TEXTS[2])
    jednotliva_slova3 = TEXTS[2].split()
    # pocet slov a vyčištění od jiných znaků
    for slovo in jednotliva_slova3:
        ciste_slovo = slovo.strip(",.!_?+-*/")

    vycistena_slova3 = [slovo.strip(",.!_?+-*/") for slovo in jednotliva_slova3]
    # vycistena_slova = type(list)
    print("There are " + str(len(vycistena_slova3)) + " words in the selected text.")
    # pomocné
    slovnik3 = {"začínající": 0, "velká": 0, "malá": 0, "cisla": 0}
    soucet3 = []
    # Slova začínající Velkým písmenem
    for znak in vycistena_slova3:
        if znak.istitle():
            slovnik3["začínající"] += 1
    print("There are " + str(slovnik3["začínající"]) + " titlecase words.")
    # Jen Velká
    for znak in vycistena_slova3:
        if znak.isalpha() and znak.isupper():
            slovnik3["velká"] += 1
    print("There are " + str(slovnik3["velká"]) + " uppercase words.")
    # Jen Malé
    for znak in vycistena_slova3:
        if znak.islower():
            slovnik3["malá"] += 1
    print("There are " + str(slovnik3["malá"]) + " lowercase words.")
    # pocet cisel
    for znak in vycistena_slova3:
        if znak.isdecimal():
            slovnik3["cisla"] += 1
    print("There are " + str(slovnik3["cisla"]) + " numeric strings.")
    # soucet cisel
    for i in vycistena_slova3:
        if i.isnumeric():
            i = int(i)
            soucet3.append(i)
    print("The sum of all the numbers ", sum(soucet3), ".", sep="")
    print(oddelovac)

    # GRAF
    print("LEN|  OCCURENCES\t|NR.")
    print(oddelovac)
    slovnik_znaky = {"jedna": 0, "dva": 0, "tri": 0, "ctyri": 0, "pet": 0, "sest": 0, "sedm": 0, "osm": 0, "devet": 0,
                     "deset": 0, "jedenact": 0, "dvanact": 0, "trinact": 0, "ctrnact": 0, "patnact": 0}
    # Přiřazení DÉLEK znaku do slovníku k jednotlivé hodnotě
    for znak in vycistena_slova3:
        if len(znak) == 1:
            slovnik_znaky["jedna"] += 1
        if len(znak) == 2:
            slovnik_znaky["dva"] += 1
        if len(znak) == 3:
            slovnik_znaky["tri"] += 1
        if len(znak) == 4:
            slovnik_znaky["ctyri"] += 1
        if len(znak) == 5:
            slovnik_znaky["pet"] += 1
        if len(znak) == 6:
            slovnik_znaky["sest"] += 1
        if len(znak) == 7:
            slovnik_znaky["sedm"] += 1
        if len(znak) == 8:
            slovnik_znaky["osm"] += 1
        if len(znak) == 9:
            slovnik_znaky["devet"] += 1
        if len(znak) == 10:
            slovnik_znaky["deset"] += 1
        if len(znak) == 11:
            slovnik_znaky["jedenact"] += 1
        if len(znak) == 12:
            slovnik_znaky["dvanact"] += 1
        if len(znak) == 13:
            slovnik_znaky["trinact"] += 1
        if len(znak) == 14:
            slovnik_znaky["ctrnact"] += 1
        if len(znak) == 15:
            slovnik_znaky["patnact"] += 1
    # Vypsání grafu
    if slovnik_znaky["jedna"] > 0:
        print("  1|"+str(slovnik_znaky["jedna"] * symbol)+ "\t\t\t\t|"+str(slovnik_znaky["jedna"]))

    if slovnik_znaky["dva"] > 0:
        print("  2|"+str(slovnik_znaky["dva"] * symbol)+"\t\t|"+str(slovnik_znaky["dva"]))

    if slovnik_znaky["tri"] > 0:
        print("  3|"+str(slovnik_znaky["tri"] * symbol)+"\t|"+str(slovnik_znaky["tri"]))

    if slovnik_znaky["ctyri"] > 0:
        print("  4|"+str(slovnik_znaky["ctyri"] * symbol)+"\t\t|"+str(slovnik_znaky["ctyri"]))

    if slovnik_znaky["pet"] > 0:
        print("  5|"+str(slovnik_znaky["pet"] * symbol)+"\t\t|"+str(slovnik_znaky["pet"]))

    if slovnik_znaky["sest"] > 0:
        print("  6|"+str(slovnik_znaky["sest"] * symbol)+"\t\t\t|"+str(slovnik_znaky["sest"]))

    if slovnik_znaky["sedm"] > 0:
        print("  7|"+str(slovnik_znaky["sedm"] * symbol)+"\t\t|"+str(slovnik_znaky["sedm"]))

    if slovnik_znaky["osm"] > 0:
        print("  8|"+str(slovnik_znaky["osm"] * symbol)+"\t\t\t|"+str(slovnik_znaky["osm"]))

    if slovnik_znaky["devet"] > 0:
        print("  9|"+str(slovnik_znaky["devet"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["devet"]))

    if slovnik_znaky["deset"] > 0:
        print(" 10|"+str(slovnik_znaky["deset"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["deset"]))

    if slovnik_znaky["jedenact"] > 0:
        print(" 11|"+str(slovnik_znaky["jedenact"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["jedenact"]))

    if slovnik_znaky["dvanact"] > 0:
        print(" 12|"+str(slovnik_znaky["dvanact"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["dvanact"]))

    if slovnik_znaky["trinact"] > 0:
        print(" 13|"+str(slovnik_znaky["trinact"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["trinact"]))

    if slovnik_znaky["ctrnact"] > 0:
        print(" 14|"+str(slovnik_znaky["ctrnact"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["ctrnact"]))

    if slovnik_znaky["patnact"] > 0:
        print(" 15|"+str(slovnik_znaky["patnact"] * symbol)+"\t\t\t\t|"+str(slovnik_znaky["patnact"]))
else:
    print("Only 3 texts available. Only numbers 1, 2, 3 can be selected between them.")
    exit()
