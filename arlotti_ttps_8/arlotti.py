import threading

def prendo_n1(lista_risultati,i):
    n1 = lista_risultati[i]
    return n1

def prendo_n2(lista_risultati,i):
    n2 = lista_risultati[i + 1]
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

        thread1 = threading.Thread(target=prendo_n1, args=(lista_risultati,i))
        thread2 = threading.Thread(target=prendo_n2, args=(lista_risultati,i))
        # Avvio dei thread
        thread1.start()
        thread2.start()

        # Attesa del completamento dei thread
        thread1.join()
        thread2.join()

        fai_calcolo(lista_risultati,n1,n2)
        i = i + 1

        # Stampa dei risultati
        print(lista_risultati)
        j = j + 1

if __name__ == "__main__":
    main()