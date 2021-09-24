
'''VERSÃO 1'''

# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        sg.theme('Reddit')
        self.layout = [
            [sg.Text('Jogar o dado?', size=(30, 4))],
            [sg.Button('Sim', size=(15, 2), button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
             sg.Button('Não', size=(15, 2), button_color=(sg.YELLOWS[0], sg.GREENS[0]), bind_return_key=True)]
        ]

    def Iniciar(self):
        # criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agrecemos a sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()