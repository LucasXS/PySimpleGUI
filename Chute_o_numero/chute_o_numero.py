from random import randint
import PySimpleGUI as sg


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_min = 1
        self.valor_max = 100
        self.tentar_novamnete = True

    def iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu chute', size=(40, 4))],
            [sg.Input(size=(20, 2), key='ValorChute')],
            [sg.Button('Chutar!', size=(15, 2), button_color=(sg.YELLOWS[0], sg.BLUES[0]))],
            [sg.Output(size=(20, 20))]
        ]
        # Cria uma janela
        self.janela = sg.Window('Chute o numero!', layout=layout)
        self.GerarNumeroAleatorio()
        #self.PedirValorAleatorio()
        try:
            while True:
                # Receber os valores
                self.evento, self.valores = self.janela.Read()
                self.valor_do_chute = self.valores('ValorChute')
                # Fazer algo com os valores
                if self.evento == 'Chutar!':
                    while self.tentar_novamnete == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo')
                            self.PedirValorAleatorio()
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto')
                            self.PedirValorAleatorio()
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamnete = False
                            print('PARABÉNS!! VOCÊ ACERTOU')
        except:
            print('DIGITAR APEMAS NÚMEROS INTEIROS!')
            self.iniciar()


    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = randint(self.valor_min, self.valor_max)

chute = ChuteONumero()
chute.iniciar()