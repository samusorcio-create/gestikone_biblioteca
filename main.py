from datetime import datetime
import biblioteca
import libro
import autore
import utente
import random

tesserino = 0
biblioteca_ = biblioteca()

while True:
    print("vuoi agiungere un libro o un utente?")
    up_date = input("digita selta")
    if up_date == "libro":
        titolo = input("inserire titolo")
        codice = random.randint(0,100000)
        formato_libro = libro(titolo,codice)
        biblioteca_.agiornamentoBiblioteca(formato_libro)
    elif up_date == "utente":
        nome = input("inserire nome")
        tesserino += 1
        formato_utente = utente(nome,tesserino)
        biblioteca_.nuovoUtente(formato_utente)
    else:
        print("input invalido")
    
    
