from datetime import datetime
import biblioteca
import libro
import autore
import utente
import random

tesserino = -1
biblioteca_ = biblioteca()

while True:
    #pensare di usare uno swic per navigare nel menu
    print("vuoi agiungere un libro o un utente?")
    add_date = input("digita selta")
    
    if add_date == "libro":
    
        titolo = input("inserire titolo")
        codice = random.randint(0,100000)
        formato_libro = libro(titolo,codice)
        #integrare creazione autore
        formato_libro.agiungiAutore("quack")#provisorio da integrare con una if che verifichi che non ci siano piu autori
        biblioteca_.agiornamentoBiblioteca(formato_libro)
    
    elif add_date == "utente":
    
        nome = input("inserire nome")
        tesserino += 1
        formato_utente = utente(nome,tesserino)
    
        biblioteca_.nuovoUtente(formato_utente)
    
    else:
    
        print("input invalido")

    add_date = input("un utente vuole ritirare un libro? si / no")
    
    if add_date == "si":
        
        numero_tessera = int(input("numero tessera"))

        nome_libro = input("inserire numero nome derl libro che si desidera")

        richiesta_utente = biblioteca_.restituisciUtente(numero_tessera)
        libro_selezionato = biblioteca_.restituisciLibro(nome_libro)
        
        for i in range(3):
            if richiesta_utente.libri[i] == None:
                richiesta_utente.richiestaLibro(libro_selezionato)
                break
    elif add_date == "no":#pensare una modalita piu comoda e meno incapzulata
        add_date = input("vuole restituire il libro? si / no")
    #da inserire if con restituzione di libro Nota ripetere tutte le domande efettuate prima 
    # a ecezione di quale riguardanti il libro (è ricavabile dalla classe utente) 
        
    
    
