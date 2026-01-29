import biblioteca
import libro
import autore
import utente
import random

while True:
    print("vuoi agiungere u libro o un utente")
    up_date = input("digita selta")
    if up_date == "libro":
        titolo = input("inserire titolo")
        codice = random.randint(0,100000)
        formato_libro = libro(titolo,codice)
    else if up_date == "utente":

    else:
        print("input invalido")
