import dados
from menu import Menu
from game import Jogar
from telaDificuldades import TelaDificuldades

def main():
    def setup():
        menu = Menu(dados.janela, dados.fundo)
        game = Jogar(dados.janela, dados.fundo)
        telaDificuldades = TelaDificuldades(dados.janela, dados.fundo)
        return menu, game, telaDificuldades

    while True:
        if dados.GAME_STATE == 0:
            menu, game, telaDificuldades = setup()
            dados.DIFICULDADE = 1
            dados.FASE = 1
            dados.GAME_STATE = 1

        elif dados.GAME_STATE == 1:
            menu.run()
        elif dados.GAME_STATE == 2:
            game.run()
        elif dados.GAME_STATE == 3:
            telaDificuldades.run()

        # estado de mudança de fase
        elif dados.GAME_STATE == 4:
            menu, game, telaDificuldades = setup()
            dados.GAME_STATE = 2

        elif dados.GAME_STATE == 5:
            dados.janela.close()

        dados.cdTempo += dados.janela.delta_time()
        dados.janela.update()

main()