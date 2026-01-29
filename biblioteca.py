import libro
import utente
import autore
# import data

class Biblioteca:
    def __init__(self):
        self.libro = []
        self.utente = []
        # self.data = []

    def __repr__(self):
        return "stampa non valida"
    
    def agiornamentoBiblioteca(self,libro):
        self.libro.append(libro)

    def nuovoUtente(self,utente):
        self.utente.append(utente)

    def stampaBiblioteca(self):
        pass

    def restituisciLibro(self):
        pass

    def restituisciUtente(self,numero_tessera):
        return self.utente[numero_tessera]
        

    # def prestito(self):
    #     self.libro[]