# Importerar funktionen randint, som tar fram ett slumpmässigt tal mellan 2 tal
from random import randint
# Importerar delar av assets-filen som används i denna fil
from assets import partier, Vänster, nöjd, missnöjd, randomrösta, adj
# Importerar funktionen median vilket gör exakt det du tror den gör
from statistics import median

# Printar en ny rad för att göra utrymme
print("\n")

# Lista som kommer innehålla alla partiers valresultat
randomröstlist = []

# Använder randomrösta-funktionen från assets-filen, där listan med partier är a, och listan med deras resultat är b
randomrösta(partier, randomröstlist)

# Lägger till varje partis valresultat i sin dictionary
for i in partier:
    i.update({"röster": randomröstlist[partier.index(i)]})

# Printar ut resultatet
# För varje parti så printar det att partier fick x antal röster
for i in partier:
    if i["röster"] >= 4:
        print(i["namn"], "fick", i["röster"], "procent av alla röster.\n")
    else:
        print(i["namn"], "fick för få röster för att komma in i riksdagen, med bara",
              i["röster"], "procent av alla röster.\n")

# Skapar variabler som är summan av antalet röster för både högern och vänstern
vänsterröst = 0
högerröst = 0

# Samma sak fast med blocken
småpartröst = 0
oljeblockröst = 0

# Lägger till alla resultat i rätt falang och block
for i in partier:
    # Kollar om partiet är vänsterinriktat, om det är sant så adderar den resultatet i variabeln vänsterröst
    if i[Vänster] == True:
        vänsterröst += i["röster"]
    # Annars lägger den till det i högerröst
    # Detta funkar eftersom alla partier är antingen höger eller vänster, och det finns liksom ingen tredje position
    else:
        högerröst += i["röster"]
    # Kollar om partiet är med i blocket Småpartierna, om det är sant så adderar den resultatet i variabeln småpartröst
    if i["Block"] == "Småpartierna":
        småpartröst += i["röster"]
    # Kollar om partiet är med i Oljeblocket, om det är sant så adderar den resultatet i variabeln oljeblockröst
    elif i["Block"] == "Oljeblocket":
        oljeblockröst += i["röster"]
    # Här funkar inte en Boolean eftersom inte alla partier är del av ett block

# Printar ut varje falangs valresultat
print("\nVänsterinriktade partier fick totalt",
      vänsterröst, "procent av alla röster.")
print("Högerinriktade partier fick totalt",
      högerröst, "procent av alla röster.")

# Printar blockens valresultat
print("\nSmåpartierna fick totalt", småpartröst, "procent av alla röster.")
print("Oljeblocket fick totalt", oljeblockröst, "procent av alla röster.\n")

# Här kommer den roliga delen 
print("\nUttalanden från alla partiledare:\n")

# För varje parti med i valet så händer detta:
for i in partier:
    # Skapar en variabel som heter med vilket är medianen av max och minimum antal röster, alltså ungefär det resultatet som förväntas av partiet
    med = median(range(i[min], i[max]))
    # Om partiet fick ett bra men inte fantastiskt resultat så säger partiledaren att hen är nöjd med partiets resultat och inget mer
    if i[max]-1 > i["röster"] >= med:
        print(i["ledare"], "är nöjd med partiets", i["röster"],
              "procent av alla röster, och är optimistisk om de kommande 4 åren.\n")
    # Om partiet fick ett fantastiskt bra resultat så blir de nöjda, och säger ett slumpmässigt uttalande från listan nöjd i assets-filen
    elif i["röster"] >= i[max]-1:
        print(i["ledare"], "är väldigt nöjd, och uttalar sig om partiets resultat i valet:",
              nöjd[randint(0, 6)], "\n")
    # Om partier fick ett dåligt men inte hemskt resultat så blir de missnöjda, och säger ett slumpmässigt uttalande från listan missnöjd i assets-filen
    elif med > i["röster"] > i[min]+1:
        print(i["ledare"], "är missnöjd, och uttalar sig om partiets resultat i valet:",
              missnöjd[randint(0, 6)], "\n")
    # Om partiets resultat är uruselt så kommer det beskrivas med ett slumpmässigt adjektiv från listan adj i assets-filen
    # Sedan kommer partiledaren avgå och uttala sig med ett påstående från missnöjd-listan
    elif i["röster"] <= i[min]+1:
        print(i["ledare"], "avgår som partiledare efter partiets", adj[randint(0, 6)], "valresultat, och kommenterar:",
              missnöjd[randint(0, 6)], "\n")

# Om vänstern har majoritet så kommer vänsterpartiledarna vara nöjda
if vänsterröst > 50:
    print("Jonas Ostbåge, Hans Majonäs, Robert Rostbiff och Dan Dan är väldigt nöjda med att vänstern är den dominerande falangen.")
# Respektive samma sak med högern
elif vänsterröst < 50:
    print("Pernilla Godisgorilla, Arja Samerna, Lennart Lurig och Antwon Släp är väldigt nöjda med att högern är den dominerande falangen.")
# Det följande printas om ingen av falangerna har majoritet, alltså om det blir 50/50
else:
    print("Båda falanger är missnöjda med att de inte har majoritet, men samtidigt glada att deras motståndare inte heller har det.")

# Om småpartierna har majoritet så kommer deras partiledare vara nöjda
if småpartröst > 50:
    print("Jonas Ostbåge, Hans Majonäs, Pernilla Godisgorilla och Arja Samerna är väldigt nöjda med att Småpartierna kommer styra Sverige de närmsta fyra åren.\n")
# Respektive samma sak med oljeblocket
elif oljeblockröst > 50:
    print("Lennart Lurig, Robert Rostbiff och Antwon Släp är väldigt nöjda med att Oljeblocket kommer styra Sverige de närmsta fyra åren.\n")
# Det följande printas om ingen av blocken har majoritet, vilket händer mycket oftare än falangerna
else:
    print("Båda block är missnöjda med att de inte har majoritet, men samtidigt glada att deras motståndare inte heller har det.\n")
