from time import sleep
import functions


while True:
    functions.service.cls()
    functions.service.banner()
    print('\033[35m\Main\033[m')
    try:
        sleep(1)
        print('\n\033[33mEscolha o tipo de FireWall\033[m')
        sleep(2)
        op = int(input('''
[01] Fortigate
\033[31m[02] Sair\033[m
 └> '''))
        
        if op == 1 or op == str(op):
            sleep(1)
            functions.service.optionMenu()
        elif typeConnection == 2 or typeConnection == str(typeConnection):
            print('\033[31mEm desenvolvimento...\033[m')
            sleep(2)
            continue
        
    except ValueError as error:
        print('\033[33mValor inválido!\033[m Tente novamente...\n {}'.format(error))
        sleep(2)
        continue