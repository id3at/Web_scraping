"""
Autor tomasz Głuc
Generator hasła na bazie cytatów.
dlugosc_hasła nigdy nie bedzie wieksza jak dlugosc wszystkich pierwszych dwoch liter z cytaty.
ale może byc mniejsza
znaki specjalne = jako opcja
"""

from bs4 import BeautifulSoup
import requests
import random
import string

def haslo(dlugosc_hasla):

    znaki = string.punctuation
    dane = []
    source = requests.get("http://www.aforyzmy.com.pl/")
    src = source.content
    soup = BeautifulSoup(src, 'lxml-xml')

    for enume, znajdz in enumerate(soup.find_all(class_="widget-area")):
        if enume < 2:
            for enum, t in enumerate(znajdz.find_all("a")):
                dane.append(t.get("href"))
                # print(enum, t.get("href"))

    losowy_temat = random.choice(dane)

    source1 = requests.get(f'{losowy_temat}')
    src1 = source1.content
    soup1 = BeautifulSoup(src1, 'lxml-xml')

    cytaty = []
    for znajdz in soup1.find_all(class_="entry-title"):
        for enum, znaj in enumerate(znajdz.find_all("a")):
            # print(enum, znaj.text)
            cytaty.append(znaj.text)

    losowy_cytat = random.choice(cytaty)

    # print(losowy_cytat.split())
    haslo_str = ""
    haslo_lic = ""
    haslo_lic_zn = ""
    for t in losowy_cytat.split():
        # print(t)
        if len(haslo_str) < int(dlugosc_hasla):
            haslo_str += "".join(t[0:2])
            haslo_lic += "".join(t[0:2])
            haslo_lic_zn += "".join(t[0:2])
            haslo_lic += str(random.randint(0, 9))
            haslo_lic_zn += str(random.randint(0, 9))
            haslo_lic_zn += random.choice(znaki)

    print(f"Hasło z cytatu: {haslo_str}")
    print(f"Hasło z liczbami {haslo_lic}")
    print(f"Hasło z liczbami i znakami specjalnymi {haslo_lic_zn}")
    print(losowy_cytat)


haslo(12)
input()
# print(dane)
