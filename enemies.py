import dados
from PPlay.sprite import *
from random import randint

class Inimigos:
    def __init__(self, janela, nave):
        self.janela = janela
        self.linsInimigos = 2 + (2*dados.DIFICULDADE)
        self.colsInimigos = 2 + (3*dados.DIFICULDADE)

        self.inimigos = []
        self.velMonstroX = 200 * dados.DIFICULDADE
        self.velMonstroY = 30
        self.velTiroInimigo = 250 + (20*dados.DIFICULDADE)
        self.nave = nave
        self.cdNaveInvencivel = 0
        self.naveLevouDano = False

        self.cooldownDescida = 0
        self.cooldownTiro = 0
        self.tempoTiro = randint(5,20)/10
        self.tirosMonstros = []

        self.criaInimigos()

    def criaInimigos(self):
        for l in range(self.linsInimigos):
            for c in range(self.colsInimigos):
                monstro = Sprite("img/enemie.png", 1)
                if c == 0:
                    monstro.x = self.janela.width / 2 - (self.colsInimigos / 2 * monstro.width)
                    monstro.y = (l + 1.8) * monstro.height
                else:
                    monstro.x = self.inimigos[c - 1].x + monstro.width * 3 / 2
                    monstro.y = (l + 1.8) * monstro.height
                self.inimigos.append(monstro)

    def colidiu(self):
        for m in self.inimigos:
            if m.x >= self.janela.width - m.width or m.x<=0:
                return 1
        return 0

    def movimentaInimigos(self):
        self.cooldownDescida += self.janela.delta_time()

        for m in self.inimigos:
            m.x += self.velMonstroX * self.janela.delta_time()

        if self.cooldownDescida > 0.15:
            if self.colidiu():
                for monstro in self.inimigos:
                    monstro.y += self.velMonstroY
                self.velMonstroX *= (-1)
                self.cooldownDescida = 0

    def detectaMorteMonstro(self):
        colidiu = False
        for tiro in self.nave.tiros:
            if self.inimigos[0].y <= tiro.y <= self.inimigos[-1].y+self.inimigos[-1].height:
                for mon in self.inimigos:
                    #print("analisando monstros")
                    if tiro.collided(mon):
                        #print("colidiu!")
                        self.nave.tiros.remove(tiro)
                        self.inimigos.remove(mon)
                        self.nave.pontosNave += 1
                        colidiu = True
                        break
                if colidiu:
                    break

    def detectaDanoNave(self):
        for tiro in self.tirosMonstros:
            if (self.nave.nave.y <= tiro.y <= self.nave.nave.y + self.nave.nave.height) and not self.naveLevouDano:
                #print("analisando tiros nave")
                if tiro.collided(self.nave.nave):
                    #print("levou dano!")
                    self.tirosMonstros.remove(tiro)
                    self.nave.vidasNave.pop(-1)
                    self.naveLevouDano = True
                    self.cdNaveInvencivel = 0
                    self.nave.nave.set_position(self.janela.width / 2 - self.nave.nave.width / 2,
                                                self.janela.height - self.nave.nave.height * 1.25)
                    break

    def piscaNave(self):
        if self.cdNaveInvencivel <= 2:
            self.cdNaveInvencivel += self.janela.delta_time()
            if 0 <= self.cdNaveInvencivel <= 0.4 or 0.7 <= self.cdNaveInvencivel <= 1.1 or 1.4 <= self.cdNaveInvencivel <= 1.7:
                coordsAnteriores = (self.nave.nave.x, self.nave.nave.y)
                self.nave.nave = Sprite("img/naveDano.png")
                self.nave.nave.set_position(coordsAnteriores[0], coordsAnteriores[1])
            else:
                coordsAnteriores = (self.nave.nave.x, self.nave.nave.y)
                self.nave.nave = Sprite("img/nave.png")
                self.nave.nave.set_position(coordsAnteriores[0], coordsAnteriores[1])
        else:
            self.naveLevouDano = False

    def atiraMonstro(self):
        idMonstroAtira = randint(0, len(self.inimigos)-1)
        tiroCriado = Sprite("img/bulletEnemie.png", 1)
        tiroCriado.x = self.inimigos[idMonstroAtira].x + self.inimigos[idMonstroAtira].width / 2 - tiroCriado.width / 2
        tiroCriado.y = self.inimigos[idMonstroAtira].y + self.inimigos[idMonstroAtira].height
        self.tirosMonstros.append(tiroCriado)
        self.cooldownTiro = 0
        self.tempoTiro = randint(3+(6/dados.DIFICULDADE),20)/10

    def movimentaTiros(self):
        for tiro in self.tirosMonstros:
            if tiro.y + tiro.height >= self.janela.height:
                self.tirosMonstros.remove(tiro)
            tiro.y += self.velTiroInimigo*self.janela.delta_time()

    def run(self):
        for i in self.inimigos:
            i.draw()
        for t in self.tirosMonstros:
            t.draw()

        self.cooldownTiro += self.janela.delta_time()

        self.detectaMorteMonstro()
        self.detectaDanoNave()
        if self.naveLevouDano:
            self.piscaNave()

        if self.cooldownTiro >= self.tempoTiro:
            #print("hora de atirar!")
            self.atiraMonstro()

        self.movimentaTiros()
        self.movimentaInimigos()
