import threading

def prendo_n1(lista_risultati,i):
    global n1
    n1 = lista_risultati[i]


def prendo_n2(lista_risultati,i):
    global n2
    n2 = lista_risultati[i + 1]


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

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        fai_calcolo(lista_risultati,n1,n2)
        i = i + 1
        print(lista_risultati)
        j = j + 1

if __name__ == "__main__":
    main()