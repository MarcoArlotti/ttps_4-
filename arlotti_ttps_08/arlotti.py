import threading


def prendo1_n(lista_numeri,i):
    n1 = lista_numeri[i]
    lista_ris.append(n1)

def prendo2_n(lista_numeri,i):
    i = i + 1
    n2 = lista_numeri[i]
    lista_ris.append(n2)
    ris = lista_ris[i] + lista_ris[i + 1]
    lista_numeri.append(ris)
    

def main(i):

    # Creazione dei thread
    thread1 = threading.Thread(target=prendo1_n, args=(lista_numeri,i))
    thread2 = threading.Thread(target=prendo2_n, args=(lista_numeri,i))

    # Avvio dei thread
    thread1.start()
    thread2.start()

    # Attesa del completamento dei thread
    thread1.join()
    thread2.join()

    # Stampa dei risultati

    print(lista_numeri)


if __name__ == "__main__":
    lista_numeri = [1,1]
    lista_ris = []
    for i in range(6):
        i = 0
        main(i)