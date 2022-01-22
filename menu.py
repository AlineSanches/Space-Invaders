import dados
from PPlay.gameimage import *

class Menu:
    def __init__ (self, janela, fundo):
        self.janela = janela
        self.fundo = fundo
        self.mouse = janela.get_mouse()
        self.titulo = GameImage("img/title.png")

        self.btJogar = GameImage("img/buttons/btJogar.png")
        self.btDificuldade = GameImage("img/buttons/btDificuldade.png")
        self.btRanking = GameImage("img/buttons/btRanking.png")
        self.btSair = GameImage("img/buttons/btSair.png")

        self.titulo.set_position(self.janela.width/2 - self.titulo.width/2, self.titulo.height)
        self.btJogar.set_position(self.janela.width/2 - self.btJogar.width/2, self.titulo.y + self.titulo.height + 70)
        self.btDificuldade.set_position(self.janela.width/2 - self.btDificuldade.width/2, self.btJogar.y + self.btJogar.height + 30)
        self.btRanking.set_position(self.janela.width/2 - self.btRanking.width/2, self.btDificuldade.y + self.btDificuldade.height + 30)
        self.btSair.set_position(self.janela.width/2 - self.btSair.width/2, self.btRanking.y + self.btRanking.height + 30)


    def run(self):
        self.fundo.draw()
        self.titulo.draw()
        self.btJogar.draw()
        self.btDificuldade.draw()
        self.btRanking.draw()
        self.btSair.draw()

        if dados.cdTempo >= 0.5:
            if self.mouse.is_over_object(self.btJogar):
                if self.mouse.is_button_pressed(1):
                    dados.cdTempo = 0
                    dados.GAME_STATE = 2

            if self.mouse.is_over_object(self.btDificuldade):
                if self.mouse.is_button_pressed(1):
                    dados.cdTempo = 0
                    dados.GAME_STATE = 3

            if self.mouse.is_over_object(self.btSair):
                if self.mouse.is_button_pressed(1):
                    dados.cdTempo = 0
                    dados.GAME_STATE = 5
