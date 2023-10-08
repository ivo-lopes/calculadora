import PySimpleGUI as sg

sg.theme('DarkGrey10')

# Estilos dos botões
botao_tipo1: dict = {'size':(7,2)}
botao_tipo2: dict = {'size':(7,2)}
botao_tipo3: dict = {'size':(16,2), 'focus':True}

layout = [  [sg.Input(key="input", size=(25,2), font=('Franklin Gothic Book', 14, 'bold'))],
            [sg.Input(key="visor_resultado", size=(25,2), font=('Franklin Gothic Book', 14, 'bold'))],
            [sg.Button('C', **botao_tipo1), sg.Button('CE', **botao_tipo1), sg.Button('%', **botao_tipo1), sg.Button('/', **botao_tipo1)],
            [sg.Button('7', **botao_tipo1), sg.Button('8', **botao_tipo1), sg.Button('9', **botao_tipo1), sg.Button('*', **botao_tipo1)],
            [sg.Button('4', **botao_tipo1), sg.Button('5', **botao_tipo1), sg.Button('6', **botao_tipo1), sg.Button('-', **botao_tipo1)],
            [sg.Button('1', **botao_tipo1), sg.Button('2', **botao_tipo1), sg.Button('3', **botao_tipo1), sg.Button('+', **botao_tipo1)],
            [sg.Button('0', **botao_tipo1), sg.Button('.', **botao_tipo1), sg.Button('=', **botao_tipo3)]
        ]

#Criação da Janela
janela = sg.Window('Calculadora', layout, return_keyboard_events=True)

#Variáveis para armazenar a expressão e o resultado
expressao_atual = ''
expressao_anterior = ''
resultado = ''

while True:
    eventos, valores = janela.read()

    if eventos == sg.WIN_CLOSED:
        break
    
    if eventos in '0123456789.':
        expressao_atual += eventos
        janela['input'].update(expressao_atual)
    elif eventos in '/*-+%':
        expressao_atual += eventos
        janela['input'].update(expressao_atual)
    elif eventos == '=' or eventos == '\r':
        try:
            if resultado:
                resultado = str(eval(resultado + expressao_atual))
            else: 
                resultado = str(eval(expressao_atual))
            janela['visor_resultado'].update(resultado)
        except Exception as e:
            resultado = 'Erro.'
            janela['visor_resultado'].update(resultado)
            print(f"Erro: {e}")
        expressao_atual = ''
        janela['input'].update('')
    elif eventos == 'C':
        expressao_atual = ''
        janela['input'].update('')
    elif eventos == 'CE':
        expressao_atual = ''
        resultado = ''
        expressao_anterior = ''
        janela['input'].update('')
        janela['visor_resultado'].update('')

# Fechar a janela logo após o break do loop while
janela.close()