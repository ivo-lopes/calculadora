import PySimpleGUI as sg

sg.theme('GrayGrayGray')

layout = [  [sg.Text('')],
            [sg.Input(key="visor")],
            [sg.Text('')],
            [sg.Button('C'), sg.Button('CE'), sg.Button('%'), sg.Button('/')],
            [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('*')],
            [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')],
            [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
            [sg.Button('0'), sg.Button('.'), sg.Button('=', key='calcular')]
        ]

#Criação da Janela
janela = sg.Window('Calculadora', layout)

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
        janela['visor'].update(expressao_atual)
    elif eventos in '/*-+':
        expressao_atual += eventos
        janela['visor'].update(expressao_atual)
    elif eventos == '\r' or eventos == 'calcular':
        try:
            if not expressao_anterior:
                resultado = str(eval(expressao_atual))
            else:
                resultado = str(eval(resultado + expressao_atual))
            janela['visor'].update(resultado)
        except Exception as e:
            resultado = 'Erro.'
            janela['visor'].update(resultado)
            print(f"Erro: {e}")
        expressao_atual = ''
    elif eventos == 'C':
        expressao_atual = ''
        resultado = ''
        janela['visor'].update('')
    elif eventos == 'CE':
        expressao_atual = ''
        resultado = ''
        expressao_anterior = ''
        janela['visor'].update('')

# Fechar a janela logo após o break do loop while
janela.close()