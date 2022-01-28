import dados
from player import Nave
from enemies import Inimigos
from PPlay.mouse import *

class Jogar:
    def __init__(self, janela, fundo):
        self.janela = janela
        self.fundo = fundo
        self.teclado = janela.get_keyboard()

        self.nave = Nave(self.janela)
        self.monstros = Inimigos(self.janela, self.nave)

        self.countTempo = 0
        self.countFrame = 0
        self.frameRate = 0


    def adicionaPontuacaoRanking(self, nomeJogador, pontos):
        from os import remove, rename
        dadosRanking = open("rankingPontos", "r", encoding="utf-8")
        dadosRankingTemp = open("rankingPontos"+"$$$", "w", encoding="utf-8")
        escreveu = False

        for linha in dadosRanking:
            nome, pts = linha.strip("\n").split("#")
            pts = int(pts)
            if pts<pontos and not escreveu:
                dadosRankingTemp.write(nomeJogador + "#" + str(pontos) + "\n")
                escreveu = True
            dadosRankingTemp.write(nome + "#" + str(pts) + "\n")

        if not escreveu:
            dadosRankingTemp.write(nomeJogador + "#" + str(pontos) + "\n")


        dadosRanking.close()
        dadosRankingTemp.close()
        remove("rankingPontos")
        rename("rankingPontos" + "$$$", "rankingPontos")
        return None

    def run(self):
        # draw de estáticos
        self.fundo.draw()
        self.janela.draw_text(str(dados.pontosNave), self.janela.width/2-25, 5, size=50, color=(238, 204, 231), font_name="calibri", bold=True,
                         italic=False)
        self.janela.draw_text("fps: "+str(self.frameRate), self.janela.width - 100, 5, size=20, color=(238, 204, 231), font_name="calibri",
                         bold=False, italic=True)
        self.janela.draw_text("FASE " + str(dados.FASE), self.janela.width - 300, 5, size=40, color=(238, 204, 231),
                              font_name="calibri", bold=True, italic=False)

        # roda a mecanica do jogo
        self.nave.run()
        self.monstros.run()

        # cálculo do fps
        self.countTempo += self.janela.delta_time()
        self.countFrame += 1
        if self.countTempo >= 1:
            self.frameRate = self.countFrame
            self.countTempo = 0
            self.countFrame = 1

        # checagem se morreram todos os monstros, para mudar de fase
        if not self.monstros.inimigos:
            dados.GAME_STATE = 4
            dados.FASE += 1

        # checagem de fim de jogo (fim das vidas ou monstros colidiram com a nave)
        if not self.nave.vidasNave or self.monstros.colidiuNave:
            nomeJogador = input("Digite seu nome: ")
            self.adicionaPontuacaoRanking(nomeJogador, dados.pontosNave)
            dados.pontosNave = 0
            dados.GAME_STATE = 0

        if self.teclado.key_pressed('ESC'):
            dados.GAME_STATE = 0

