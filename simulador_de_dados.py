import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.janela = None
        self.eventos = None
        self.valores = None
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com esses valores
        try:
            if self.eventos == 'Sim':
                self.gerar_valor_do_dado()
            elif self.eventos == 'Não':
                print('Agradecemos sua participação!')
            else:
                print('Favor digitar sim ou não.')
        except:
            print('Ocorreu um erro ao receber sua resposta.')

    def gerar_valor_do_dado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.iniciar()