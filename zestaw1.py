import random
import copy

def wypisanie(macierz):
	for i in range(len(macierz)): #wypisuje macierz jako tablice dwuwymiarowa
		print(macierz[i])

def losuj_graf(krawedzie, wierzcholki): #losuje graf majac podana liczbe krawedzi i wierzcholkow
	if (krawedzie<=(wierzcholki*(wierzcholki-1))/2): #by stworzyc graf musi byc spelniony wzor 
                tablica=[0]*wierzcholki
                wspolrzedne=krawedzie*[0]
                for x in range(wierzcholki):
                        tablica[x]=wierzcholki*[0] #tworzy tablice wypelniona 0

                for x in range(krawedzie):
                        wspolrzedne[x]=2*[0]

                lista=[0,0] #lista do przetrzymywania wspolrzednych
                for i in range(krawedzie):
                        while(lista in wspolrzedne):
                                wspolrzednax=random.randint(1,wierzcholki-1)
                                wspolrzednay=random.randint(0,wspolrzednax-1)
                                lista=[wspolrzednax,wspolrzednay] #losuje miejsce w tablicy do postawienia 1
                        wspolrzedne[i][0]=wspolrzednax
                        wspolrzedne[i][1]=wspolrzednay
                        tablica[wspolrzednax][wspolrzednay]=1 #uzupelnienie tablicy
                        tablica[wspolrzednay][wspolrzednax]=1
	else:
		print("za duzo krawedzi")
	return tablica


def losuj_graf_losowo(wierzcholki,prawdopodobienstwo):
	tab=[0]*wierzcholki 
	for x in range(wierzcholki):
		tab[x]=wierzcholki*[0] #tworzy tablice wypelniona 0
	for i in range(1,wierzcholki):
		for j in range(0,i): #idzie po skosie prawej czesci macierzy
			p=random.random()
			#print(p)
			if p<prawdopodobienstwo: #sprawdza czy p jest mniejsze od prawdopodobienstwa
				tab[i][j]=1 #jesli tak, tworzy krawedz
				tab[j][i]=1
	return(tab)

def sasiedztwa_na_incydencji(sasiedztwa):
	krawedzie,k=0,0
	wierzcholki=len(sasiedztwa) #sprawdza liczbe wierzcholkow
	pomocnicza_sasiedztwa=copy.deepcopy(sasiedztwa) #pomocnicza macierz sasiedztwa
	pomocnicza_sasiedztwa=str(pomocnicza_sasiedztwa)
	krawedzie=pomocnicza_sasiedztwa.count('1') #zlicza ilosc 1 w macierzy sasiedztwa
	krawedzie=krawedzie//2 #oblicza ilosc krawedzi
	incydencji=krawedzie*[0]
	for x in range (krawedzie):
		incydencji[x]=wierzcholki*[0] #tworzy macierz incydencji wypelniona 0
	for i in range(wierzcholki):
		for j in range (i):
			if(sasiedztwa[j][i]==1): #jesli w macierzy sasiedztwa wystepuje polaczenie
				incydencji[k][i]=1 #to tworzy je w macierzy incydencji
				incydencji[k][j]=1
				k=k+1 #zwieksza nr krawedzi
	return incydencji


def incydencji_na_sasiedztwa(incydencji):
	wierzcholki=len(incydencji[0]) #sprawdza ilosc wierzcholkow
	sasiedztwa=wierzcholki*[0] 
	tab=2*[0] #tablica przechowujaca wierzcholki ktore laczy ta sama krawedz
	for x in range(wierzcholki):
		sasiedztwa[x]=wierzcholki*[0] #tworzy macierz sasiedztwa uzupelniona 0
	indexTab=0
	for i in range(len(incydencji)): # petla iterujaca po tablicy incydencji
		for j in range(wierzcholki):
			if incydencji[i][j]==1: #sprawdzenie kiedy w tablicy incydencji jest 1
				tab[indexTab]=j #zapisanie indeksu pod ktorym znajduje sie 1(beda takie 2)
				indexTab=indexTab+1
		sasiedztwa[tab[0]][tab[1]]=1 #tworzenie tablicy sasiedztwa poprzez wpisanie 1 pod indeksami z tablicy tab
		sasiedztwa[tab[1]][tab[0]]=1
		indexTab=0

	return sasiedztwa


def sasiedztwa_na_liste(sasiedztwa):
	wierzcholki=len(sasiedztwa)
	lista=wierzcholki*[None]
	for x in range(wierzcholki):
		lista[x]=[None] #tworzy pusta liste
		lista[x][0]=x #wypisuje ktory to wierzcholek (po kolei)
	for i in range(wierzcholki):
		for j in range(wierzcholki):
			if sasiedztwa[i][j]==1: #jesli jest polaczenie w macierzy sasiedztwa
				lista[i].append(j) #wpisuje do listy
	return(lista)

def liste_na_sasiedztwa(liste):
	macierz=len(lista)*[0]
	for x in range(len(lista)):
		macierz[x]=[0]*len(lista) #tworzy macierz sasiedztwa

	for i in range(len(lista)):
		for j in range(1,len(lista[i])):
			k=lista[i][j] #idzie po liscie wydobywajac polaczenie
			macierz[i][k]=1 #wpisuje w odpowiednie indeksy 1 w macierzy sasiedztwa
	return macierz

def incydencji_na_liste(incydencji):
	sasiedztwa=incydencji_na_sasiedztwa(incydencji) #wywoluje funkcje zamiany incydencji na sasiedztwa
	liste=sasiedztwa_na_liste(sasiedztwa) #wywoluje funkcje zamiany sasiedztwa na liste
	return liste #zwraca liste

def liste_na_incydencji(liste):
	sasiedztwa=liste_na_sasiedztwa(liste) #wywoluje funkcje zamiany listy na sasiedztwa
	incydencji=sasiedztwa_na_incydencji(sasiedztwa) #wywoluje funkcje zamiany sasiedztwa na liste
	return incydencji

a=random.randint(1,10)
b=random.randint(1,10) #losuje liczbe krawedzi i wierzcholkow

while (a>=(b*(b-1))/2):
	b=random.randint(1,10) #sprawdza czy liczba wierzcholkow zostala dobrze wylosowana


prawdopodobienstwo=random.random() #losuje prawdopodobienstwo powstania krawedzi
print("prawdopodobienstwo:",prawdopodobienstwo)


graf=losuj_graf_losowo(a,0.5)
graf=losuj_graf(10,20)

print("wylosowana macierz sasiedztwa:")
wypisanie(graf)
print("sasiedztwa na liste:")
lista=sasiedztwa_na_liste(graf) 
wypisanie(lista)

print("liste_na_sasiedztwa:")
macierz=liste_na_sasiedztwa(lista) 
wypisanie(macierz)

#print("GRAF:")
#wypisanie(graf)
print("sasiedztwa_na_incydencji:")
macierz=sasiedztwa_na_incydencji(graf) 
wypisanie(macierz)
print("incydencji na sasiedztwa:")
sasiedztwa=incydencji_na_sasiedztwa(macierz) 
wypisanie(sasiedztwa)

#print("GRAF:")
#wypisanie(macierz)
print("incydencji na liste:")
lista=incydencji_na_liste(macierz) 
wypisanie(lista)
print("liste na incydencji:")
incydencji=liste_na_incydencji(lista) 
wypisanie(incydencji)


