importError = False

from os import system
from time import sleep

try:
    import mouse
except ModuleNotFoundError:
    system('pip install mouse')
except ImportError:
    print("ERRO DE IMPORTAÇÃO DA BIBLIOTECA MOUSE")
    importError = True

try:
    import keyboard
except ModuleNotFoundError:
    system('pip install keyboard')
except ImportError:
    print("ERRO DE IMPORTAÇÃO DA BIBLIOTECA KEYBOARD")
    importError = True

try:
    import PySimpleGUI as pg
except ModuleNotFoundError:
    system('pip install pysimplegui')
except ImportError:
    print("ERRO DE IMPORTAÇÃO DA BIBLIOTECA PYSIMPLEGUI")
    importError = True

#FUNÇÃO DE REPETIÇÃO DO CLIQUE
def clicar(time):
    while not(keyboard.is_pressed('-')):
        mouse.click('left')
        sleep(time)
    pg.popup_no_titlebar(f"PRESSIONE (=) PARA CLICAR NOVAMENTE\nPRESSIONER ESC PARA RECONFIGURAR",
                         background_color='white',
                         text_color='black',
                         font=("Open Sans",12,"bold underline"))
    while True:
        if keyboard.is_pressed("="):
            clicar(time)
        elif keyboard.is_pressed("ESC"):
            return 

if not importError:

    #EXECUÇÃO CASO NENHUM ERRO DE IMPORTAÇÃO TENHA OCORRIDO
    try:

        #LAYOUT DA APLICAÇÃO
        layout = [[pg.Text("CLICADOR 3.0",
                           expand_x=True,justification='center',font=("Open Sans", 12,"bold italic"),background_color='darkblue')],
                  [pg.HorizontalSeparator()],
                  [pg.Text("INTERVALO PARA COMEÇAR A CLICAR (MIN 5)",size=(40,1),justification='right',font=("Open Sans", 10,'bold'), background_color='darkblue'), 
                   pg.Input('',key='timeToStart',size=(6,1),font=("Open Sans", 10)), 
                   pg.Text(' SEGUNDOS',font=("Open Sans", 10),background_color='darkblue')],
                  [pg.Text("INTERVALO DE CLIQUE (MIN 0,005)",size=(40,1),justification='right',font=("Open Sans", 10,'bold'),background_color='darkblue'), 
                   pg.Input('',key='clickInterval',size=(6,1),font=("Open Sans", 10)),
                   pg.Text(' SEGUNDOS',font=("Open Sans", 10),background_color='darkblue')],
                  [pg.HorizontalSeparator()],
                  [pg.Text("TECLA (-) -> PARA O CLIQUE\n\nDEPOIS DE PARAR O CLIQUE:\nTECLA (=) -> RETOMA O CLIQUE\nTECLA (ESC) -> ALTERAR OS PARÂMETROS",
                           font=("Open Sans", 10),background_color='darkblue')],
                  [pg.HorizontalSeparator()],
                  [pg.Button('COMEÇAR A CLICAR',
                             key='start',expand_x=True, border_width=5,button_color='green',mouseover_colors='darkgreen')],
                  [pg.Button('SAIR',key='exit',expand_x=True,border_width=5,button_color='red')],
                  [pg.HorizontalSeparator()],
                  [pg.Text("DESENVOLVIDO POR MATHEUS QUELUCCI - VERSÃO 3.0 (08/2023)",
                           expand_x=True,justification='left',font=("Open Sans", 10,"italic"),background_color='darkblue')]]
        
        #ESQUEMA DE FONTES
        pg.set_options(font=("Open Sans", 12),background_color='darkblue')

        #CRIA O OBJETO JANELA
        janela  = pg.Window('CLICADOR 3.0',layout=layout,finalize=True)

        #ÍCONE DA APLICAÇÃO
        janela.set_icon('clicador3.0.ico')
        
        #CENTRALIZA A JANELA
        screen_width, screen_height = pg.Window.get_screen_size()
        window_width, window_height = janela.size
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        janela.move(x_position, y_position)

        while True:

            checkTimeToStart = False #Checagem se o valor de inserido no intervalo de início é válido
            checkClickInterval = False #Checagem se o valor de inserido no intervalo de clique é válido

            events, values = janela.read()

            if events == pg.WINDOW_CLOSED or events == 'exit':
                break

            if events == 'start':

                timeToStart = str(values['timeToStart']).replace(',','.')
                clickInterval = str(values['clickInterval']).replace(',','.')

                #VERIFICA SE O VALOR INSERIDO NO CAMPO DE INTERVALO DE INÍCIO É DECIMAL
                try:
                    timeToStart = float(timeToStart)
                    if timeToStart < 5:
                        pg.popup_no_titlebar('O INTERVALO DE INÍCIO ESTÁ MUITO BAIXO',background_color='yellow',text_color='red',font=("Open Sans",12,"bold underline"))
                    else:
                        checkTimeToStart = True
                except ValueError:
                    pg.popup_no_titlebar('O INTERVALO DE INÍCIO NÃO É UM NÚMERO VÁLIDO',background_color='yellow',text_color='red',font=("Open Sans",12,"bold underline"))

                #VERIFICA SE O VALOR INSERIDO NO CAMPO DE INTERVALO DE CLIQUE É NUMÉRICO
                try:
                    clickInterval = float(clickInterval)
                    if clickInterval < 0.005:
                        pg.popup_no_titlebar('O INTERVALO DE CLIQUE ESTÁ MUITO BAIXO',background_color='yellow',text_color='red',font=("Open Sans",12,"bold underline"))
                    else:
                        checkClickInterval = True
                except ValueError:
                    pg.popup_no_titlebar('O INTERVALO DE CLIQUE NÃO É UM NÚMERO VÁLIDO',background_color='yellow',text_color='red',font=("Open Sans",12,"bold underline"))

                if checkClickInterval and checkTimeToStart:
                    pg.popup_no_titlebar(f"ESSA TELA SERÁ FECHADA EM {timeToStart} SEGUNDOS!\nTECLA (-) -> PARA O CLIQUE\nTECLA (=) -> RETOMA O CLIQUE\nTECLA (ESC) -> ALTERAR OS PARÂMETROS (SOMENTE DEPOIS DE PARAR O CLIQUE)",
                                         background_color='white',
                                         text_color='black',
                                         font=("Open Sans",12,"bold underline"),
                                         auto_close=True,
                                         auto_close_duration=timeToStart)
                    janela.disable()
                    janela.minimize()
                    sleep(timeToStart)
                    clicar(clickInterval)
                    janela.enable()
                    janela.normal()
                
        janela.close()

    #ERRO DE EXECUÇÃO
    except Exception as error:
        pg.popup(f"ERRO DE EXECUÇÃO\n{error}",background_color='yellow',text_color='red',font=("Open Sans",12,"bold underline"))