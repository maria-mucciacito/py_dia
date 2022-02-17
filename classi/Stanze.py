class Stanza:

    NUMERO_MASSIMO_DERIZIONI = 4

    def __init__(self,nome):
        self.nome = nome
        self.nord = None
        self.sud = None
        self.est = None
        self.ovest = None
        self.stanzaVincente = None

    def __repr__(self):
        return f'Il giocatore si trova nella stanza:  {self.nome}'

    def get_nord(self):
        return self.nord
    def set_nord(self,nord):
        self.nord = nord

    def get_sud(self):
        return self.sud
    def set_sud(self,sud):
        self.sud = sud
    
    def get_est(self):
        return self.est
    def set_est(self,est):
        self.est = est

    def get_ovest(self):
        return self.ovest
    def set_ovest(self,ovest):
        self.ovest = ovest

    def get_nome(self):
        return self.nome
    def set_nome(self,nome):
        self.nome = nome








