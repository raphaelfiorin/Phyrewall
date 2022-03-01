from time import sleep
import functions


while True:
    functions.service.cls()
    functions.service.banner()
    try:
        sleep(1)
        print('\n\033[34mEscolha o tipo de FireWall\033[m')
        sleep(2)
        op = int(input('''
[01] Fortigate
\033[31m[02] Sair\033[m
 └> '''))

        if op == 1 or op == str(op):
            print('\n\033[34mEscolha o tipo de conexão\033[m')
            sleep(1)
        typeConnection = int(input('''
    [01] SSH
    [02] Cabo Console
    └> '''))
        if typeConnection == 1 or typeConnection == str(typeConnection):
            functions.fortigateFunctions.create_user_ssh()
        elif typeConnection == 2 or typeConnection == str(typeConnection):
            print('\033[31mEm desenvolvimento...\033[m')
            sleep(2)
            continue
        
    except ValueError:
        print('\033[33mValor inválido!\033[m Tente novamente...\n {}'.format(error))
        sleep(2)
        continue