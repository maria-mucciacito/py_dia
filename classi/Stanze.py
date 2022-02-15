class Stanza:

    def __init__(self,nome,nord,sud,est,ovest):
        self.__nome = nome
        self.__nord = nord
        self.__sud = sud
        self.__est = est
        self.__ovest = ovest

    def __repr__(self):
        return f'Il giocatore si trova nella stanza:  {self.nome}'

    @property
    def nord(self):
        return self.__nord
    @nord.setter
    def nord(self,nord):
        self.__nord = nord

    @property
    def sud(self):
        return self.__sud
    @sud.setter
    def sud(self,sud):
        self.__nord = sud

    @property
    def est(self):
        return self.__est
    @est.setter
    def est(self,s):
        self.__est = s

    @property
    def ovest(self):
        return self.__ovest
    @ovest.setter
    def ovest(self,ovest):
        self.__ovest = ovest

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome







