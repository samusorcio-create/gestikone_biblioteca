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
    
#eq non necesario è efettuato nelle classi di aparteneza

    def agiornamentoBiblioteca(self,libro):
        self.libro.append(libro)

    def nuovoUtente(self,utente):
        self.utente.append(utente)

    def stampaBiblioteca(self):
        pass#restituisce tutta la biblioteca con utenti e libri 

    def stampaParzialelibreria(self):
        pass#restituire tutti i nomi con al suo interno una data o parziale sequenza str

    def restituisciLibro(self,titolo):
        for i in range(len(self.libro)):#integrare verifica disponibilita libro
            if self.libro[i].titolo == titolo:
                return self.libro[i]
        return None

    def restituisciUtente(self,numero_tessera):
        return self.utente[numero_tessera]#integrare verifica se untente sia gia iscritto
        

    # def prestito(self):
    #     self.libro[]