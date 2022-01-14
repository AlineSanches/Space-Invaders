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

    def run(self):
        self.fundo.draw()
        self.janela.draw_text(str(self.nave.pontosNave), self.janela.width/2-25, 0, size=50, color=(255, 255, 255), font_name="Arial", bold=True,
                         italic=False)
        self.janela.draw_text("fps: "+str(self.frameRate), self.janela.width - 100, 0, size=20, color=(255, 255, 255), font_name="Arial",
                         bold=False, italic=True)

        self.nave.run()
        self.monstros.run()


        self.countTempo += self.janela.delta_time()
        self.countFrame += 1
        if self.countTempo >= 1:
            self.frameRate = self.countFrame
            self.countTempo = 0
            self.countFrame = 1

        if self.teclado.key_pressed('ESC'):
            dados.GAME_STATE = 1

