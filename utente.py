class Utente:
    def __iit__(self,nome,numero_tessera,libri):
        self.nome = nome
        self.numero_tessera = numero_tessera
        self.libri = [0]*3 #deve risultare una lista

    def __repr__(self):
        return f"utrnte: nome=> {self.nome}, numero di tesserinoi=> {self.numero_tessera}, libri=>{self.libri}"
    
    # def __eq__(self,other):
