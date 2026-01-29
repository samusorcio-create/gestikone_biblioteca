class Utente:
    def __iit__(self,nome,numero_tessera):
        self.nome = nome
        self.numero_tessera = numero_tessera
        self.libri = [] #deve risultare una lista

    def __repr__(self):
        return f"utrnte: nome=> {self.nome}, numero di tesserinoi=> {self.numero_tessera}, libri=>{self.libri}"
    
    def __eq__(self,other):
        if not isinstance(self,other):
            return False
        return self.nome == other.nome, self.numero_tessera == other.numero_tessera

    def richiestaLibro(self,libro):
        self.libri.append(libro)

    # def __eq__(self,other):
