import dados
from PPlay.gameimage import *


class TelaDificuldades:
    def __init__(self, janela, fundo):
        self.janela = janela
        self.fundo = fundo
        self.mouse = janela.get_mouse()

        self.btFacil = GameImage("img/buttons/btFacil.png")
        self.btMedio = GameImage("img/buttons/btMedio.png")
        self.btDificil = GameImage("img/buttons/btDificil.png")

        self.lisBtsDificuldade = [self.btFacil, self.btMedio, self.btDificil]
        for i in range(len(self.lisBtsDificuldade)):
            self.lisBtsDificuldade[i].x = self.janela.width / 2 - self.lisBtsDificuldade[i].width / 2
            self.lisBtsDificuldade[i].y = 130 * (i + 1) + self.lisBtsDificuldade[i].height / 2

    def run(self):
        # draw
        self.fundo.draw()
        for i in range(len(self.lisBtsDificuldade)):
            self.lisBtsDificuldade[i].draw()

        # mudança da dificuldade de acordo com o botão apertado
        if dados.cdTempo >= 0.5:  # para correção de problemas como duplo clique em um
            if self.mouse.is_over_object(self.btFacil):
                if self.mouse.is_button_pressed(1):
                    dados.cdTempo = 0
                    dados.DIFICULDADE = 1
                    dados.GAME_STATE = 1

            if self.mouse.is_over_object(self.btMedio):
                if self.mouse.is_button_pressed(1):
                    dados.cdTempo = 0
                    dados.DIFICULDADE = 2
                    dados.GAME_STATE = 1

            if self.mouse.is_over_object(self.btDificil):
                if self.mouse.is_button_pressed(1):
                    dados.cdTempo = 0
                    dados.DIFICULDADE = 3
                    dados.GAME_STATE = 1
