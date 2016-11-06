import random

def wierzcholki():
    lista=[x for x in range(random.randint(1,50))] #tworzy liste wypelniona losowa iloscia wierzcholkow od 1 do 50
    print(lista)
    return lista

def krawedzie():
    ilosc_wierzcholkow=len(wierzcholki()) #sprawdza ile wierzcholkow wylosowano
    b=ilosc_wierzcholkow
    ilosc_krawedzi=random.randint(1,(b*(b-1))/2) #losuje odpowiednia ilosc krawedzi
    lista=[(random.randint(1,ilosc_wierzcholkow),random.randint(1,ilosc_wierzcholkow)) for x in range(ilosc_krawedzi)] #tworzy liste polaczen krawedzi 
    return lista
