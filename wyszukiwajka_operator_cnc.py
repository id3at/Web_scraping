"""
Autor: Tomasz Głuc
Wyszukiwajka :D
"""

from bs4 import BeautifulSoup
import requests

miasta = ["kraków", "wieliczka", "krosno", "sanok", "rzeszów",
          "jasło", "bochnia", "brzesko", "tarnów", "skawina", "wadowice",
          "andrychów", "korczyna", "brzozów", "strzyżów", "zagórz",
          "cisna", "pilzno", "strzyżów", "gorlice", "lesko", "polańczyk",
          "solina", "biecz"]

oferta = []
czas = []
firma = []
adres = []


def miasteczka(miasto):

    source = requests.get(f"https://www.pracuj.pl/praca/operator%20cnc;kw/{miasto};wp?rd=0")
    src = source.content
    soup = BeautifulSoup(src, 'lxml')
    return soup
###############################################################################


def miasteczka2(miasto):

    source1 = requests.get(f"https://www.infopraca.pl/praca?q=operator+cnc&lc={miasto}&d=0")
    src1 = source1.content
    soup1 = BeautifulSoup(src1, 'lxml')
    return soup1


def pracujpl(x):

    for article in x.find_all("h3", class_="offer-details__title"):
        oferta.append(article.text)
        tag = article.find("a", class_="offer-details__title-link")
        adres.append(tag.attrs["href"])

    for article in x.find_all("a", class_="offer-company__name"):
        firma.append(article.text)

    for t in x.find_all("span", class_="offer-actions__date"):
        data = t.text
        czas.append(data)


def infopraca(x):

    for article in x.find_all("h2", class_="p-job-title"):
        oferta.append(article.text)
        tag = article.find("a")
        adres.append(f'https://www.infopraca.pl{tag.attrs["href"]}')

    for article in x.find_all("h3", class_="p-name company"):
        firma.append(article.text)

    for t in x.find_all("span", class_="last-update"):
        data2 = t.text
        czas.append(data2)


for t in miasta:
    pracujpl(miasteczka(t))

for t in miasta:
    t.capitalize()
    infopraca(miasteczka2(t))

for t in range(len(oferta)):
    print(oferta[t].strip())
    print(firma[t].strip())
    print(adres[t].strip())
    print(czas[t].strip())
    print()
input()
