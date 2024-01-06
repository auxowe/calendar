import calendar
from datetime import datetime
year = 2021

from os import system, name
from time import sleep
  
def clear():
    if name=="nt":
        _=system("cls")
    else:
        _=system("clear")
    return ""

def muistutukset_tulostus():
    print("Muistutukset:")
    print(mtiedosto())
    for avain in gkirja:
        print(avain+gkirja[avain])
    return ""


def mtiedosto():
    with open("jorinat.txt") as tiedosto:
        lista = tiedosto.readlines()
    for i in range(len(lista)):
        lista[i] = lista[i].replace("\n","")

    global gkirja
    for alkio in lista:
        gkirja[alkio[0:6]]=str(alkio[6:])
    lista.sort()
    lista.sort(key=lambda alkio: alkio[3])
    return ""


def muistutukset_tulostus_kk():
    print(f"Muistutukset kuukaudelta {g}:")
    print(mtiedosto())
    for avain in gkirja:
            if avain[3:5]==g:
                print(avain+gkirja[avain])
    return ""
    

def muistutukset_poisto():
    #global g
    while True:         
        try:
            y=int(input("Päivä, jolta haluat poistaa muistutuksen (lukuna, esim. 2): "))
            if 0<y<32:         
                break
            if y>31 or y<1:
                print("Luvun täytyy olla väliltä 1-31 ja muotoa x (esim. Valintasi lukuna: 6)")
        except ValueError:
            print("Päivä pitää antaa lukuna!")
    y=str(y)
    if len(y)<2:
        y="0"+y

    x=str(y)+"."+str(g)+"."
    print(mtiedosto())

    with open("jorinat.txt", "r") as t:
        lines=t.readlines()
    with open("jorinat.txt", "w") as t:
        for line in lines:
            if x not in line.strip("\n"):
                t.write(line)
    try:
        del gkirja[x]
    except KeyError:
        print("Et ole laittanut muistutusta kyseiselle päivämäärälle")
    print(f"Muistiinpano päivältä {x} on poistettu.")
    sleep(1)
 
    return ""


gkirja={}

def muistutukset():
    while True:         
        try:
            pv=int(input("Päivä, jolle haluat muistutuksen (lukuna, esim 7): "))
            if 32>pv>0:         
                break
            if 31<pv or pv<1:
                print("Luvun täytyy olla väliltä 0-31 ja muotoa x (esim. Valintasi lukuna: 6)")
        except ValueError:
            print("Päivä pitää antaa lukuna!")

    muistiinpano=input("Kirjoita muistutus: ")

    pv=str(pv)
    if len(pv)<2:
        pv="0"+pv
    global g
    g=str(g)
    if len(g)<2:
        g="0"+g

    with open("jorinat.txt", "a") as tiedosto:
        tiedosto.write(str(pv)+"."+ str(g) + ".2021: " + muistiinpano + "\n")

    return ""


def muistiinpanovalikko():
    global g
    print("1. Lisää muistutus")
    print("2. Poista muistutus")
    print("3. Seuraava kuukausi")
    print("4. Edellinen kuukausi")
    print("0. Palaa kuukausivalikkoon")
    while True:
        try:
            v=int(input("Valintasi lukuna: "))
            if v==1 or v==2 or v==0 or v==3 or v==4:       
                break
            if v!=1 or v!=2 or v!=0 or v!=3 or v!=4:
                print("Luvun täytyy olla väliltä 0-4 ja muotoa x (esim. Valintasi lukuna: 1)")
        except ValueError:
             print("Valinta pitää antaa lukuna!")
    print("")

    if v==1:
        print(muistutukset())
        print(clear())
        g=int(g)
        print(calendar.month(year, g))
        g=str(g)
        if len(g)<2:
            g="0"+g
        print(muistutukset_tulostus_kk())
        print(muistiinpanovalikko())

    if v==2:
        print(muistutukset_poisto())
        print(clear())
        g=int(g)
        print(calendar.month(year, g))
        g=str(g)
        if len(g)<2:
            g="0"+g
        print(muistutukset_tulostus_kk())
        print(muistiinpanovalikko())

    if v==3:
        print(clear())
        g=int(g)
        while True:
            if g==12:
                g=g-1       
            if 13>g>0:
                break
        g=int(g)+1
        print(calendar.month(year, g))
        g=str(g)
        if len(g)<2:
            g="0"+g
        print(muistutukset_tulostus_kk())
        print(muistiinpanovalikko())

    if v==4:
        print(clear())
        g=int(g)
        while True:
            if g==1:
                g=g+1       
            if 13>g>0:
                break
        g=int(g)-1
        print(calendar.month(year, g))
        g=str(g)
        if len(g)<2:
            g="0"+g
        print(muistutukset_tulostus_kk())
        print(muistiinpanovalikko())
    
    if v==0:
        print(clear())
        print(kuukaudet())

    return ""


g=""

def kuukaudet():
    global g
    print("Kalenteri 2021"+"\n")
    print("1. Tammikuu")
    print("2. Helmikuu")
    print("3. Maaliskuu")
    print("4. Huhtikuu")
    print("5. Toukokuu")
    print("6. Kesäkuu")
    print("7. Heinäkuu")
    print("8. Elokuu")
    print("9. Syyskuu")
    print("10. Lokakuu")
    print("11. Marraskuu")
    print("12. Joulukuu"+"\n")
    print("0. Poistu kuukausivalikosta"+"\n")

    print(muistutukset_tulostus())

    while True:
        try:
            g=int(input("Valintasi lukuna: "))
            if g==1 or g==2 or g==0 or g==3 or g==4 or g==5 or g==6 or g==7 or g==8 or g==9 or g==10 or g==11 or g==12:          
                break
            else:
                print("Luvun täytyy olla väliltä 0-12 ja muotoa x (esim. Valintasi lukuna: 6)")
        except ValueError:
             print("Valinta pitää antaa lukuna!")
    print("")
    
    if g==0:
        print(clear())
        print(valikko())
    
    print(clear())
    i=1
    while True:
        if g==i:
            print(calendar.month(year, g))
        if g==i:
            break
        i+=1
    g=str(g)
    if len(g)<2:
        g="0"+g

    print(muistutukset_tulostus_kk())
    print(muistiinpanovalikko())
        
    return ""


def valikko():
    print("Kalenteri 2021"+"\n")

    tanaan=datetime.now()
    print(tanaan.strftime("Tänään on %d.%m.%Y"+"\n"))

    print("Valitse:")
    print("1: Avaa kalenteri")
    print("2: Avaa muistutukset")

    while True:
        try:
            valinta=int(input("Valintasi lukuna (esim. 1): "))
            if valinta==1 or valinta==2:
                break
            else:
                print("Luvun täytyy olla väliltä 1-2 ja muotoa x (esim. Valintasi lukuna: 1)")
        except ValueError:
            print("Valinta pitää antaa lukuna!")
    print("")

    if valinta==1:
        print(clear())
        print(kuukaudet())
    if valinta==2:
        print(clear())
        print(muistutukset_tulostus())
        print(valikko())

    return ""
    
print(valikko())