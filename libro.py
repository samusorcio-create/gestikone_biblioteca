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
        
    def agiungiAutore(self,autor):
        self.autori.append(autor)




        