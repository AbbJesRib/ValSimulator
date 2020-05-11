from random import randint
from assets import partier, Vänster, nöjd, missnöjd, randomrösta, adj

print("\n")

randomröstlist = []

randomrösta(partier, randomröstlist)

for i in partier:
    i.update({"röster": randomröstlist[partier.index(i)]})

for i in partier:
    if i["röster"] >= 4:
        print(i["namn"], "fick", i["röster"], "procent av alla röster.\n")
    else:
        print(i["namn"], "fick för få röster för att komma in i riksdagen, med bara",
              i["röster"], "procent av alla röster.\n")

vänsterröst = 0
högerröst = 0

småpartröst = 0
oljeblockröst = 0

for i in partier:
    if i[Vänster] == True:
        vänsterröst += i["röster"]
    else:
        högerröst += i["röster"]
    if i["Block"] == "Småpartierna":
        småpartröst += i["röster"]
    elif i["Block"] == "Oljeblocket":
        oljeblockröst += i["röster"]


print("\nVänsterinriktade partier fick totalt",
      vänsterröst, "procent av alla röster.")
print("Högerinriktade partier fick totalt",
      högerröst, "procent av alla röster.")

print("\nSmåpartierna fick totalt", småpartröst, "procent av alla röster.")
print("Oljeblocket fick totalt", oljeblockröst, "procent av alla röster.\n")

print("\nUttalanden från alla partiledare:\n")

for i in partier:
    average = (i[min]+i[max])/2
    if i[max]-1 > i["röster"] >= average:
        print(i["ledare"], "är nöjd med partiets", i["röster"],
              "procent av alla röster, och är optimistisk om de kommande 4 åren.\n")
    elif i["röster"] >= i[max]-1:
        print(i["ledare"], "är väldigt nöjd, och uttalar sig om partiets resultat i valet:",
              nöjd[randint(0, 6)], "\n")
    elif average > i["röster"] > i[min]+1:
        print(i["ledare"], "är missnöjd, och uttalar sig om partiets resultat i valet:",
              missnöjd[randint(0, 6)], "\n")
    elif i["röster"] <= i[min]+1:
        print(i["ledare"], "avgår som partiledare efter partiets", adj[randint(0, 6)], "valresultat, och kommenterar:",
              missnöjd[randint(0, 6)], "\n")

if vänsterröst > 50:
    print("Jonas Ostbåge, Hans Majonäs, Robert Rostbiff och Dan Dan är väldigt nöjda med att vänstern är den dominerande falangen.")
elif vänsterröst < 50:
    print("Pernilla Godisgorilla, Arja Samerna, Lennart Lurig och Antwon Släp är väldigt nöjda med att högern är den dominerande falangen.")
else:
    print("Båda falanger är missnöjda med att de inte har majoritet, men samtidigt glada att deras motståndare inte heller har det.")

if småpartröst > 50:
    print("Jonas Ostbåge, Hans Majonäs, Pernilla Godisgorilla och Arja Samerna är väldigt nöjda med att Småpartierna kommer styra Sverige de närmsta fyra åren.\n")
elif oljeblockröst > 50:
    print("Lennart Lurig, Robert Rostbiff och Antwon Släp är väldigt nöjda med att Oljeblocket kommer styra Sverige de närmsta fyra åren.\n")
else:
    print("Båda block är missnöjda med att de inte har majoritet, men samtidigt glada att deras motståndare inte heller har det.\n")
