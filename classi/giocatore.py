from classi.Stanze import Stanza

class Giocatore:

    def __init__(self,nome):
        self.pv = 10
        self.__nome = nome
        self.__stanza = 'Parcheggio'

    @property
    def stanza(self):
        return self.__stanza.nome
    @stanza.setter
    def stanza(self,n_stanza):
        self.__stanza = n_stanza
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    def guarda(self):
        print('Ti trovi nella stanza: ')
        print(self.__stanza.nome)



        pass

    def esci(self):
        pass

    def vai(self,direzione):
        pass


