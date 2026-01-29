class Libro:
    def __init__(self,titolo,codice):
        self.titolo = titolo
        self.stato = True
        self.codice = codice
        self.autori = [] #deve risultare una lista

    def __repr__(self):
        if self.stato:
            return f"utrnte: titolo=> {self.titolo}, stato=> disponibile , codice=> {self.codice}, autori=>{self.autori}"
        else:
            return f"utrnte: titolo=> {self.titolo}, stato=> non disponibile , codice=> {self.codice}, autori=>{self.autori}"
        
    def __eq__(self,other):
        if not isinstance(self,other):
            return False
        return self.titolo == other.titolo, self.codice == other.codice
    

    def agiungiAutore(self,autore):
        self.autori.append(autore)




        