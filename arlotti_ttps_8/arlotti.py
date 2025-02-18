import threading

def prendo_n1(lista_risultati,i):
    n1 = lista_risultati[i]
    print(n1)
    return n1

def prendo_n2(lista_risultati,i):
    n2 = lista_risultati[i + 1]
    print(n2)
    return n2

def fai_calcolo(lista_risultati,n1,n2):
    ris = n1 + n2
    lista_risultati.append(ris)

def main():
    lista_risultati = [1,1]
    i = 0
    j = 0

    for j in range(16):
        # Creazione dei thread
        # thread1 = threading.Thread(target=prendon1, args=(lista_risultati,i))
        # thread2 = threading.Thread(target=prendon2, args=(lista_risultati,i))
        n1 = prendo_n1(lista_risultati,i)
        n2 = prendo_n2(lista_risultati,i)
        fai_calcolo(lista_risultati,n1,n2)
        i = i + 1
        # Avvio dei thread
        # thread1.start()
        # thread2.start()

        # Attesa del completamento dei thread
        # thread1.join()
        # thread2.join()

        # Stampa dei risultati
        print(lista_risultati)
        j = j + 1

if __name__ == "__main__":
    main()