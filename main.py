from datetime import datetime
import biblioteca
import libro
import autore
import utente
import random

tesserino = -1
biblioteca_ = biblioteca()

while True:#provisorio, forse da implementare alinterno di un while piu grande
    #pensare di usare uno swic per navigare nel menu
    print("vuoi agiungere un libro o un utente?")
    add_date = input("digita selta")
    
    if add_date == "libro":
    
        titolo = input("inserire titolo")
        codice = random.randint(0,100000)
        formato_libro = libro(titolo,codice)
    
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
  
        richiesta_utente = biblioteca_.restituisciUtente(numero_tessera)
  
        for i in range(3):
            if richiesta_utente.libri[i] == None:
                richiesta_utente.richiestaLibro()
                break
    elif add_date == "no":#pensare una modalita piu comoda e meno incapzulata
        add_date = input("vuole restituire il libro? si / no")
        
    
    
