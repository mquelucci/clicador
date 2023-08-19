importError = False
from os import system

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
    from time import sleep
except ImportError:
    print("ERRO DE IMPORTAÇÃO DE SLEEP BIBLIOTECA TIME")
    importError = True

def clicar():
    while not(keyboard.is_pressed('-')):
        sleep(0.01)
        mouse.click('left')
    print("!!!PRESSIONE 'ESC' PARA SAIR DO CLICADOR!!!")
    print("!!!PRESSIONE '=' (IGUAL) PARA VOLTAR A CLICAR!!!")
    while True:
        if keyboard.is_pressed("="):
            clicar()
        elif keyboard.is_pressed("ESC"):
            return 2

if not importError:
    global opt
    print("CLICADOR 2.0")
    opt = int(input("[INICIAR -> 1]\n[SAIR -> 2]\nOPÇÃO: "))

    while True:
        if opt == 1:
            opt = 0
            tdly = int(input("INTERVALO PARA INICIAR (SEGUNDOS): "))
            print("!!!PRESSIONE '-' (HÍFEN) PARA PARAR DE CLICAR!!!")
            print()
            sleep(tdly)
            opt = clicar()
            system('cls')
        elif opt == 2:
            print("ENCERRANDO O CLICADOR")
            sleep(2)
            break
        else:
            system('cls')
            print("CLICADOR 2.0")
            opt = int(input("[INICIAR -> 1]\n[SAIR -> 2]\nOPÇÃO: "))
