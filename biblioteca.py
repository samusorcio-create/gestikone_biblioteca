import libro
import utente
import autore
# import data

class Biblioteca:
    def __init__(self):
        self.libro = []
        self.utente = []
        # self.data = []

    def agiornamentoBiblioteca(self,libro):
        self.libro.append(libro)

    def nuovoUtente(self,utente):
        self.utente.append(utente)


    # def prestito(self):
    #     self.libro[]