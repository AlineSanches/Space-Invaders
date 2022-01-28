from PPlay.gameimage import *
import dados


class Ranking:
    def __init__(self, janela, fundo):
        self.janela = janela
        self.fundo = fundo
        self.teclado = janela.get_keyboard()

        self.rankingTitulo = GameImage("img/rankingTxt.png")
        self.rankingTitulo.set_position(self.janela.width / 2 - self.rankingTitulo.width / 2, self.rankingTitulo.height)
        self.ranking = []
        self.pegaRanking()

    def pegaRanking(self):
        dados = open("rankingPontos", "r", encoding="utf-8")
        linha = dados.readline()
        if linha != "":
            while len(self.ranking) < 5 and linha != "":
                nome, pts = linha.strip("\n").split("#")
                self.ranking.append((nome, pts))
                linha = dados.readline()

        dados.close()

    def run(self):
        self.fundo.draw()
        self.rankingTitulo.draw()
        for i in range(len(self.ranking)):
            self.janela.draw_text(str(i+1) + " - " + self.ranking[i][0] + " (" + self.ranking[i][1] + ")",
                                  self.janela.width / 2 - 120, 200 + 50*(i+1), size=50, color=(238, 204, 231),
                                  font_name="calibri", bold=True, italic=False)

        if self.teclado.key_pressed('ESC'):
            dados.GAME_STATE = 0