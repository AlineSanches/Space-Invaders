import dados
from PPlay.sprite import *

class Inimigos:
    def __init__(self, janela, nave):
        self.janela = janela
        self.linsInimigos = 2 + (2*dados.DIFICULDADE)
        self.colsInimigos = 2 + (3*dados.DIFICULDADE)

        self.inimigos = []
        self.velMonstroX = 200 * dados.DIFICULDADE
        self.velMonstroY = 300
        self.nave = nave

        self.cooldownDescida = 0

        self.criaInimigos()

    def criaInimigos(self):
        for l in range(self.linsInimigos):
            linha = []
            for c in range(self.colsInimigos):
                monstro = Sprite("img/enemie.png", 1)
                if c == 0:
                    monstro.x = self.janela.width / 2 - (self.colsInimigos / 2 * monstro.width)
                    monstro.y = (l + 1.8) * monstro.height
                else:
                    monstro.x = linha[c - 1].x + monstro.width * 3 / 2
                    monstro.y = (l + 1.8) * monstro.height
                linha.append(monstro)
            self.inimigos.append(linha)

    def movimentaInimigos(self):
        self.cooldownDescida += self.janela.delta_time()

        for lin in self.inimigos:
            for m in lin:
                m.x += self.velMonstroX * self.janela.delta_time()

        if self.cooldownDescida > 0.15:
            if self.inimigos[0][-1].x + self.inimigos[0][-1].width >= self.janela.width or self.inimigos[0][0].x <= 0:
                for linha in self.inimigos:
                    for monstro in linha:
                        monstro.y += 30
                self.velMonstroX *= (-1)
                self.cooldownDescida = 0


    def run(self):
        for lin in self.inimigos:
            for i in lin:
                i.draw()

        colidiu = False
        lin = [True]*self.colsInimigos
        matrizExiste = [lin]*self.linsInimigos

        for tiro in self.nave.tiros:
            if tiro.y<=self.inimigos[-1][-1].y or tiro.x<=self.inimigos[-1][-1].x:
                for linId in range(self.linsInimigos):
                    for monId in range(self.colsInimigos):
                        print("analisando monstros")
                        try:
                            if matrizExiste[linId][monId]:
                                if tiro.collided(self.inimigos[linId][monId]):
                                    print("colidiu!")
                                    self.nave.tiros.remove(tiro)
                                    self.inimigos[linId].remove(self.inimigos[linId][monId])
                                    matrizExiste[linId][monId] = False
                                    self.nave.pontosNave += 1
                                    colidiu = True
                                    break
                        except:
                            print("não foi")
                    if colidiu:
                        break
        self.movimentaInimigos()
