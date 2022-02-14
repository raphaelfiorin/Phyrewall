from libAll import *
from Fortigate import create_user

def connection ():
    while True:
        escolha = int(input("""
            \033[33mOptions Fortigate\033
    \033[32m[1]\033[0;0m - Criação de VPN
    \033[32m[2]\033[0;0m - Desautenticar User
    \033[32m[3]\033[0;0m - Criar User Admin
    \033[31m[4]\033[0;0m - Voltar ao Menu
    └> """))
        if escolha == 1:
            pass
        elif escolha == 2:
            pass
        elif escolha == 3:
            typeConnection = int(input("""
\033[32m[1]\033[0;0m - Conexão SSH
\033[32m[2]\033[0;0m - Conexão CABO CONSOLE
\033[31m[3]\033[0;0m - Voltar ao Menu
└> """))
            if typeConnection == 1:
                create_user.create_user_ssh()
            elif typeConnection == 2:
                create_user.create_user_console()
            else:
                cls()
                connection()
        else:
            continue