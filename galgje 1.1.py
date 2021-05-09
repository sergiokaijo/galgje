import os

print("\nGalgje \n")

speler1 = input("Naam speler 1: ")                                                  # naam invoer spelers 
speler2 = input("Naam speler 2: ")

print()
print("Welkom", speler1, "en", speler2, "\n")

print(speler1, end="")                                                              # speler 1 voert een woord in
woord = input(", Vul hier uw woord in: ")
woord = woord.lower()                                                               # verzekeren dat het woord dat is ingevoerd uit kleine letters bestaat 

os.system('cls')                                                                    # het scherm leeg maken 

lengte_woord = len(woord)                                                           # eerst lengte woord opvragen en vervolgens zetten in een list 
lijst_woord = lengte_woord*["_"]

kansen = int(0)
max_kansen = int(9)
antwoord, nieuw_antwoord, fout_antwoord, fout_woord = "", "", "", ""

while kansen < 10:

    print("\nHet woord heeft",len(woord), "letters: ", *lijst_woord)                # lengte van het woord weergeven

    print("\nJe hebt nog", max_kansen - kansen, "kans(en). \n")                     # aantal kansen weergeven

    if "_" not in lijst_woord:                                                      # controleren of "_" nog in de varriable zit zo niet zijn alle letters geraden
        print("\n", speler2, end="")
        print(", gefeliciteerd je hebt het woord geraden:", woord.upper())
        input("Druk op ENTER om het spel te verlaten")
        break;

    print(speler2, end="")                                                          # speler 2 voert in welke letter of wat het hele woord is
    antwoord = input(", Voer een letter of een woord in: ")
    antwoord = antwoord.lower()                                                     # verzekeren dat het antwoord dat is ingevoerd uit een kleine letter bestaat 
    print()

    if len(antwoord) == len(woord) and antwoord.isalpha():                          # controleren of het antwoord hetzelfde lengte heeft als het woord en bestaat uit letters (alpha character)
        if antwoord == woord:                                                       # als het woord hetzelfde lengte heeft en antwoord komt overeen met woord heeft speler 2 gewonnen.
            print("\n", speler2, end="")
            print(", gefeliciteerd je hebt het woord geraden:", woord.upper())
            input("Druk op ENTER om het spel te verlaten")
            break;      
        elif antwoord in fout_woord:                                                # controleren of het fout woord al eerder is geraden
            print("\nDeze woord heb je al een keer fout geraden:", antwoord.upper(), "\n")
        else:
            print("\nJammer je hebt het woord niet goed geraden\n")
            kansen += 1
            fout_woord = antwoord + fout_woord

    os.system('cls')                                                                # het scherm leeg maken 

    if len(antwoord) == 1 and ord(antwoord) >= 97 and ord(antwoord) <= 122:         # controleren of ingevoerde antwoord uit 1 karakter bestaat en een letter is (alpha character) dmv ascii tabel
        for x in range(lengte_woord):                                               # controleren of ingevoerde antwoord voorkomt in woord
            if antwoord in woord[x]:
                del lijst_woord[x]
                lijst_woord.insert(x,antwoord)
                
        if antwoord in nieuw_antwoord:                                              # controleren of het antwoord al eerder is ingevoerd
            print("\nDeze letter heb je al goed geraden:", antwoord.upper(), "\n")
        elif antwoord in woord:                                                     # aangeven welke letter in het woord zit en opslaan om de stap hierboven uit te voeren
            print("\nKomt voor in het woord:", antwoord.upper(), "\n")
            nieuw_antwoord = antwoord + " " + nieuw_antwoord    
        elif antwoord in fout_antwoord:                                             # controleren of het foute antwoord al eerder is benoemd
            print("\nDeze letter komt niet voor in het woord en heb je al eerder gekozen:", antwoord.upper(), "\n")
        else:                                                                       # aangeven dat het letter niet voor komt en volgens op te slaan om de stap hierboven uit te voeren
            print("\nkomt niet voor in het woord:", antwoord.upper(), "\n")
            fout_antwoord = antwoord + fout_antwoord
            kansen += 1                                                             # de over gebleven kansen van speler 2 weergeven
    else:
        print("\nVoer maximaal 1 letter in of een woord van", len(woord), "letters\n")

    if kansen == 1:
        print("═══╩══════════\n")
    elif kansen == 2:
        print("   ║")
        print("   ║")
        print("   ║")
        print("   ║")
        print("   ║")
        print("   ║")

        print("   ║")
        print("═══╩══════════\n")
    elif kansen == 3:
        print("   ╔═════╗")
        print("   ║")
        print("   ║")
        print("   ║")
        print("   ║")
        print("   ║")
        print("   ║")
        print("   ║")
        print("═══╩══════════\n")
    elif kansen == 4:
        print("   ╔═════╗")
        print("   ║    ╔╩╗")
        print("   ║    ║ ║")
        print("   ║    ╚╦╝")
        print("   ║")
        print("   ║")
        print("   ║")
        print("   ║")
        print("═══╩══════════\n")
    elif kansen == 5:
        print("   ╔═════╗")
        print("   ║    ╔╩╗")
        print("   ║    ║ ║")
        print("   ║    ╚╦╝")
        print("   ║     ╬")
        print("   ║     ║")
        print("   ║     ╩")
        print("   ║")
        print("═══╩══════════\n")
    elif kansen == 6:
        print("   ╔═════╗")
        print("   ║    ╔╩╗")
        print("   ║    ║ ║")
        print("   ║    ╚╦╝")
        print("   ║    ═╬═")
        print("   ║     ║")
        print("   ║     ╩")
        print("   ║")
        print("═══╩══════════\n")
    elif kansen == 7:
        print("   ╔═════╗")
        print("   ║    ╔╩╗")
        print("   ║    ║ ║")
        print("   ║    ╚╦╝")
        print("   ║    ═╬═")
        print("   ║     ║")
        print("   ║    ═╩═")
        print("   ║")
        print("═══╩══════════\n")
    elif kansen == 8:
        print("   ╔═════╗")
        print("   ║    ╔╩╗")
        print("   ║    ║֍║")
        print("   ║    ╚╦╝")
        print("   ║    ═╬═")
        print("   ║     ║")
        print("   ║    ═╩═")
        print("   ║")
        print("═══╩══════════\n")
    elif kansen == 9:
        print("GAME OVER\n")
        print("               ☼")
        print("   ╔═════╗")
        print("   ║    ╔╩╗")
        print("   ║    ║֍║")
        print("   ║    ╚╦╝")
        print("   ║    ═╬═")
        print("   ║     ║")
        print("   ║    ═╩═")
        print("   ║")
        print("═══╩══════════ \n")
        input("Druk ENTER om het spel te verlaten")
        break;
    else:
        continue