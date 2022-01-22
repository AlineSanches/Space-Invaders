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
        self.velNave = 250 - (30*dados.DIFICULDADE) + (30*dados.FASE)
        self.velTiro = 350 - (20*dados.DIFICULDADE) + (50*dados.FASE)

        self.pontosNave = 0
        self.vidasNave = []
        self.qtdVidas = 4

        self.countTempo = 0
        self.iniciaVidas()

    def iniciaVidas(self):
        for v in range(self.qtdVidas):
            vida = GameImage("img/heart.png")
            vida.x = (v+1.25)*vida.width + v*5
            vida.y = 20
            self.vidasNave.append(vida)

    def controlaNave(self):
        if self.teclado.key_pressed("LEFT") and self.nave.x >= 0:
            self.nave.x -= self.velNave * self.janela.delta_time()
        if self.teclado.key_pressed("RIGHT") and self.nave.x <= self.janela.width - self.nave.width:
            self.nave.x += self.velNave * self.janela.delta_time()

        if self.teclado.key_pressed("SPACE") and self.countTempo>(0.5+0.1*dados.DIFICULDADE-(min(0.07*dados.FASE, 0.3))):
            tiroCriado = Sprite("img/bullet.png",1)
            tiroCriado.x = self.nave.x + self.nave.width/2 - tiroCriado.width/2
            tiroCriado.y = self.nave.y - tiroCriado.height
            self.tiros.append(tiroCriado)
            self.countTempo = 0


    def run(self):
        self.nave.draw()
        for t in self.tiros:
            t.draw()
        for v in self.vidasNave:
            v.draw()

        self.countTempo += self.janela.delta_time()
        self.controlaNave()

        for tiro in self.tiros:
            if tiro.y <= 0:
                self.tiros.remove(tiro)
            tiro.y -= self.velTiro*self.janela.delta_time()
