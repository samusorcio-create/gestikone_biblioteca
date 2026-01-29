class Autore:
    def __init__(self,nome,nazionalita):
        self.nome = nome
        self.nazionalita = nazionalita
        
    def __repr__(self):
        return f"autore: nome=> {self.nome}, nazionalita=> {self.nazionalita}"
    
    def __eq__(self,other):
        if not isinstance(self,other):
            return False
        return self.nome == other.nome, self.nazionalita == other.nazionalita
    