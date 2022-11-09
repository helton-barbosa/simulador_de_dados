import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.janela = None
        self.eventos = None
        self.valores = None
        self.menor_face_do_dado = 1
        self.maior_face_do_dado = 6
        # Layout
        self.caixa = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não'), sg.Button('Sair')]
        ]

    def iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de Dados', layout=self.caixa)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com esses valores
        try:
            if self.eventos == 'Sim':
                self.gerar_valor_do_dado()
            elif self.eventos == 'Não':
                print('Agradecemos sua participação!')
            else:
                print('Saindo do programa!')
        except:
            print('Ocorreu um erro ao receber sua resposta.')

    def gerar_valor_do_dado(self):
        print(f'Foi sorteado a face {random.randint(self.menor_face_do_dado, self.maior_face_do_dado)} do dado.')


simulador = SimuladorDeDado()
simulador.iniciar()