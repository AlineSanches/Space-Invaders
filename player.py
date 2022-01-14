import dados
from PPlay.gameimage import *
from PPlay.sprite import *

class Nave:
    def __init__(self, janela):
        self.janela = janela
        self.nave = Sprite("img/nave.png")

        self.nave.set_position(janela.width / 2 - self.nave.width / 2, janela.height - self.nave.height*1.25)
        self.tiros = []
        self.teclado = janela.get_keyboard()
        self.velNave = 280 - (30*dados.DIFICULDADE)
        self.velTiro = 300 - (20*dados.DIFICULDADE)

        self.pontosNave = 0

        self.countTempo = 0

    def run(self):
        self.nave.draw()
        for t in self.tiros:
            t.draw()

        self.countTempo += self.janela.delta_time()

        if self.teclado.key_pressed("LEFT") and self.nave.x >= 0:
            self.nave.x -= self.velNave * self.janela.delta_time()
        if self.teclado.key_pressed("RIGHT") and self.nave.x <= self.janela.width - self.nave.width:
            self.nave.x += self.velNave * self.janela.delta_time()

        if self.teclado.key_pressed("SPACE") and self.countTempo>(0.5*dados.DIFICULDADE):
            tiroCriado = Sprite("img/bullet.png",1)
            tiroCriado.x = self.nave.x + self.nave.width/2 - tiroCriado.width/2
            tiroCriado.y = self.nave.y - tiroCriado.height
            self.tiros.append(tiroCriado)
            self.countTempo = 0

        for tiro in self.tiros:
            if tiro.y <= 0:
                self.tiros.remove(tiro)
            tiro.y -= self.velTiro*self.janela.delta_time()
