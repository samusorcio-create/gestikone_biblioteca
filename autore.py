class Autore:
    def __init__(self,nome,nazionalita):
        self.nome = nome
        self.nazionalita = nazionalita
        
    def __repr__(self):
        return f"autore: nome=> {self.nome}, nazionalita=> {self.nazionalita}"
    