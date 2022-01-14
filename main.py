import dados
from menu import Menu
from game import Jogar
from telaDificuldades import TelaDificuldades

menu = Menu(dados.janela, dados.fundo)
game = Jogar(dados.janela, dados.fundo)
telaDificuldades = TelaDificuldades(dados.janela, dados.fundo)

while True:
    if dados.GAME_STATE == 1:
        menu.run()
    elif dados.GAME_STATE == 2:
        game.run()
    elif dados.GAME_STATE == 3:
        telaDificuldades.run()
    elif dados.GAME_STATE == 4:
        dados.janela.close()

    dados.cdTempo += dados.janela.delta_time()
    dados.janela.update()