import threading
n1 = 5
n2 = 3

n3 = 4
n4 = 2

lista_risultati = []

def calcolo1(n1,n2):
    ris1 = n1 + n2
    print(ris1)
    
    #mettendo nella lista di risultati
    lista_risultati.append(ris1)

def calcolo2(n3,n4):
    ris2 = n3 - n4
    print(ris2)
    
    #mettendo nella lista di risultati
    lista_risultati.append(ris2)
    

def main():

    # Creazione dei thread
    thread1 = threading.Thread(target=calcolo1, args=(n1,n2))
    thread2 = threading.Thread(target=calcolo2, args=(n3,n4))

    # Avvio dei thread
    thread1.start()
    thread2.start()

    # Attesa del completamento dei thread
    thread1.join()
    thread2.join()

    # Stampa dei risultati
    print(lista_risultati[0]*lista_risultati[1])


if __name__ == "__main__":
    main()