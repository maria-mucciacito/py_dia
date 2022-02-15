from classi.Stanze import Stanza

class Labirinto:
    lst_labirinto = []

    def __init__(self):
        self.lst_labirinto.append(self.parcheggio)
        self.lst_labirinto.append(self.atrio)
        self.lst_labirinto.append(self.area_relax)
        self.lst_labirinto.append(self.aula_azzurra)
        self.lst_labirinto.append(self.aula_gialla)
        self.lst_labirinto.append(self.segreteria)
        self.lst_labirinto.append(self.presidenza)


    def crea_labirinto(self):
        self.parcheggio = Stanza('Parcheggio',None,None,'Atrio',None)
        self.atrio = Stanza('Atrio')
        self.area_relax = Stanza('Area Relax')
        self.aula_azzurra = Stanza('Aula Azzurra')
        self.aula_gialla = Stanza('Aula Gialla')
        self.segreteria = Stanza('Segreteria')
        self.presidenza = Stanza('Presidenza')
        self.parcheggio.est('atrio')
        self.atrio.nord('segreteria')
        self.atrio.sud('area_relax')
        self.atrio.ovest('parcheggio')
        self.atrio.est('aula_gialla')
        self.area_relax.nord('atrio')
        self.area_relax.est('aula_gialla')
        self.area_relax.sud('aula_azzurra')
        self.area_relax.ovest('presidenza')
        self.segreteria.sud('atrio')
        self.segreteria.nord('presidenza')
        self.segreteria.est('aula_gialla')
        self.segreteria.ovest('aula_azzurra')
        self.aula_gialla.ovest('segreteria')
        self.aula_gialla.nord('presidenza')
        self.aula_gialla.sud('atrio')
        self.presidenza.sud('segreteria')
        self.presidenza.ovest('aula_azzurra')
        self.presidenza.est('aula_gialla')
        self.presidenza.nord('area_relax')
        self.aula_azzurra.est('segreteria')
        self.aula_azzurra.ovest('area_relax')
        self.aula_azzurra.nord('presidenza')