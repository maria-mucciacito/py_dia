
from classi.labirinto import Labirinto

class Giocatore:

    MESSAGGIO_DI_BENVENUTO = "Benvenuto nel gioco py_dia!"
    ELENCO_COMANDI = ["vai <direzione>", "aiuto", "guarda", "fine"]

    def __init__(self,nome):
        self.pv = 10
        self.nome = nome
        self.partita = Labirinto()

    
    def get_nome(self):
        return self.nome
    def set_nome(self,nome):
        self.nome = nome

    def gioca(self):
        esci = False

        while(esci==False):
            comando = input('Inserisci comando: ')
            if (self.set_istruzione(comando) == True):
                esci = True

    def set_istruzione(sefl,istruzione):
        if(istruzione == "fine"):
            return self.fine()
        elif(istruzione == "aiuto"):
            return self.aiuto()
        elif(istruzione == 'guarda'):
            return self.guarda()
        elif(istruzione[0:3] == "vai"):
            return self.vai(istruzione[4: len(istruzione)])
        else:
            print('Inserisci un comando valido!')
            return False
    
    def guarda(self):
        print(f"Ti trovi nella stanza: {self.partita.stanzaCorrente}, hai ancora a disposizione {self.pv} punti vita! ")
        if (self.partita.stanzaCorrente == self.partita.stanzaVincente):
            print('Evviva! Hai trovato il manuale!')
            return True
        else:
            return False

    def fine(self):
        print('Grazie per aver giocato!')
        return True

    def aiuto(self):
        print('Hai a disposizione i seguenti comandi: ')
        print(*self.ELENCO_COMANDI, sep = ", ")
        return False

    def esci(self):
        pass

    def vai(self,direzione):
        if direzione == "nord" and self.partita.stanzaCorrente.nord != None:
            self.partita.stanzaCorrente = self.partita.stanzaCorrente.nord
        elif direzione == "sud" and self.partita.stanzaCorrente.sud != None: 
            self.partita.stanzaCorrente = self.partita.stanzaCorrente.sud
        elif direzione == "est" and self.partita.stanzaCorrente.est != None: 
            self.partita.stanzaCorrente = self.partita.stanzaCorrente.est
        elif direzione == "ovest" and self.partita.stanzaCorrente.ovest != None: 
            self.partita.stanzaCorrente = self.partita.stanzaCorrente.ovest
        else:
            print(f"{direzione} non esistente, inserisci una direzione valida!")
            return False
        self.pv -= 1
        
        if self.pv == 0:
            print('Hai finito i punti vita. Game Over!')
        print(f"Hai cambiato stanza, ti rimangono {self.pv} punti vita!")

player1 = Giocatore()
player1.gioca()

