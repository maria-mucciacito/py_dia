from classi.stanze import Stanza
class Labirinto:

    def __init__(self):
        self.stanzaVincente = None
        self.stanzaCorrente = None
        self.crea_labirinto()

    def crea_labirinto(self):
        parcheggio = Stanza('Parcheggio')
        atrio = Stanza('Atrio')
        area_relax = Stanza('Area Relax')
        aula_azzurra = Stanza('Aula Azzurra')
        aula_gialla = Stanza('Aula Gialla')
        segreteria = Stanza('Segreteria')
        presidenza = Stanza('Presidenza')

        parcheggio.set_est('atrio')
        
        atrio.set_nord('segreteria')
        atrio.set_sud('area_relax')
        atrio.set_ovest('parcheggio')
        atrio.set_est('aula_gialla')
        
        area_relax.set_nord('atrio')
        area_relax.set_est('aula_gialla')
        area_relax.set_sud('aula_azzurra')
        area_relax.set_ovest('presidenza')
        
        segreteria.set_sud('atrio')
        segreteria.set_nord('presidenza')
        segreteria.set_est('aula_gialla')
        segreteria.set_ovest('aula_azzurra')
        
        aula_gialla.set_ovest('segreteria')
        aula_gialla.set_nord('presidenza')
        aula_gialla.set_sud('atrio')
        
        presidenza.set_sud('segreteria')
        presidenza.set_ovest('aula_azzurra')
        presidenza.set_est('aula_gialla')
        presidenza.set_nord('area_relax')
        
        aula_azzurra.set_est('segreteria')
        aula_azzurra.set_ovest('area_relax')
        aula_azzurra.set_nord('presidenza')

        self.stanzaCorrente = parcheggio
        segreteria.stanzaVincente = True

        print('Labirinto creato')