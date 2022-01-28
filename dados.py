from PPlay.gameimage import *
from PPlay.window import *

# inicialização
janela = Window(1040, 620)
janela.set_title('Space Invaders')
fundo = GameImage("./img/galaxy.jpg")

cdTempo = 0
GAME_STATE = 0
DIFICULDADE = 1
FASE = 1
pontosNave = 0