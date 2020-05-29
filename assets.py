# Importerar funktionen randint, som tar fram ett slumpmässigt tal mellan 2 tal, som används i funktionen nedan
from random import randint

# I denna funktion är a listan med partier, och b är en ny lista med hur många röster alla partier fick
def randomrösta(a, b):
    # För varje parti, så får funktionen fram ett slumpmässigt tal mellan det minsta och största antalet röster, och lägger till det i listan b
    for i in a:
        b.append(randint(i[min], i[max]))
    # Om summan av alla röster inte blir hundra, så rensar den listan b och kör om funktionen
    if sum(b) != 100:
        b.clear()
        randomrösta(a, b)


# En boolean som bestämmer om det är ett högerparti eller ett vänsterparti
Vänster = bool

# En dictionary för varje parti, som innehåller namn, inrikting, block, minimum antal röster, max antal röster, partiledare och senare, hur många röster partiet fick
gröng = {
    "namn": "Gröngölingarna",
    Vänster: True,
    "Block": "Småpartierna",
    min: 3,
    max: 12,
    "ledare": "Jonas Ostbåge"
}
part = {
    "namn": "Partikelpartiet",
    Vänster: True,
    "Block": "Småpartierna",
    min: 2,
    max: 8,
    "ledare": "Hans Majonäs"
}
mälar = {
    "namn": "Mälarpartiet",
    Vänster: False,
    "Block": "Småpartierna",
    min: 8,
    max: 18,
    "ledare": "Pernilla Godisgorilla"
}
sjö = {
    "namn": "Sjörövarpartiet",
    Vänster: False,
    "Block": "Småpartierna",
    min: 3,
    max: 12,
    "ledare": "Arja Samerna"
}
extrem = {
    "namn": "Extremisterna",
    Vänster: False,
    "Block": "Oljeblocket",
    min: 3,
    max: 6,
    "ledare": "Lennart Lurig"
}
maskin = {
    "namn": "Maskinpartiet",
    Vänster: True,
    "Block": "Oljeblocket",
    min: 12,
    max: 22,
    "ledare": "Robert Rostbiff"
}
framtid = {
    "namn": "Framtidspartiet",
    Vänster: False,
    "Block": "Oljeblocket",
    min: 12,
    max: 18,
    "ledare": "Antwon Släp"
}
allp = {
    "namn": "Allpartiet",
    Vänster: True,
    "Block": "Inget",
    min: 20,
    max: 34,
    "ledare": "Dan Dan"
}

# En lista med alla partier för att kunna ta värden från deras dictionary
partier = [
    gröng,
    part,
    mälar,
    sjö,
    extrem,
    maskin,
    framtid,
    allp
]

# Lista med påståenden som en partiledare kan säga om hens parti fick nära max antal röster
nöjd = [
    '"Det här gör oss alla i partiet väldigt nöjda. Jag hoppas att vårat nya inflytande i riksdagen kommer gå en lång väg."',
    '"Det här gick jättebra. Jag lovar att ge alla som röstade på mitt parti 10 000 kr."',
    '"Tack för att ni röstade på vårt parti."',
    '"Jäklar! Valfusk funkar ju."',
    '"Jag ser en bra framtid för Sverige."',
    '"Jag visste att det här skulle hända."',
    '"Jarrå, gubbar, så ska det gå."'
]

# Lista med påståenden som partiledaren kan säga om hens parti fick nära minimum antal röster
missnöjd = [
    '"Fyfan vad arg jag är"',
    '"Det svenska folket är äckliga"',
    '"Det här är en katastrof, inte bara för partiet, men för hela Sverige"',
    '"Det här måste ju ha varit valfusk. Jag ser ingen annan förklaring"',
    '"Jaha, tillbaka till ritbordet."',
    '"Jag visste att det här skulle hända."',
    '"Det här kunde ingen i partiet ha förväntat sig. Jag skäms."'
]

# Lista med adjektiv som kan beskriva ett partis valresultat om det gick riktigt dåligt för dem
adj = [
    "katastrofala",
    "oerhört dåliga",
    "usla",
    "urusla",
    "hemska",
    "förfärliga",
    "misslyckade"
]
