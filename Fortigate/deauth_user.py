from libAll import *

# Conexão ssh
def deauth_user_ssh():
    print('\n\033[32m[SSH]\033[0;0m - Estabelecendo conexão SSH ')
    host = input('└> Digite o host: ')
    port = input('└> Digite a porta: ')
    user = input('└> Digite o user: ')
    password = input('└> Digite a senha: ')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port, user, password)
    except paramiko.AuthenticationException as err:
        print("\033[31mErro de login: \033[0;0m" + str(err))
    print('\n\033[32m[SSH Conectado]\033[0;0m')
    sleep(1)

# Desautenticando user
    usertype = int(input("""
\033[32m[SSH]\033[0;0m - Tipo de user:
\033[32m[1]\033[0;0m - Fsso
\033[32m[2]\033[0;0m - Kerberos
\033[32m[3]\033[0;0m - Outros
\033[31m[4]\033[0;0m - Voltar ao Menu
└> """))
    if usertype == 1:
        fsso()
    elif usertype == 2:
        kerberos()
    elif usertype == 3:
        outro()
    elif usertype == 4:
        print('Voltando ao menu!')
    else:
        print(' \033[31mEscolha os itens do menu!\033[0;0m')


def fsso():
    print('\n\033[32m[SSH]\033[0;0m - Deauth user')
    nome = input('└> Digite o nome do user: ')
    stdin, stdout, stderr = ssh.exec_command(
        "dia deb authd fsso list \n" + "dia deb auth fsso filter  user {} \n".format(
            nome) + " dia deb authd fsso  clear-logon \n" + "dia deb auth fsso filter clear \n")
    # lines = stdout.readlines()
    # print(lines)
    print('\n\033[32m[SSH]\033[0;0m - Usuario desautenticado com sucesso')
    print(f'''└> User: {nome}
    └> Tipo de user: {usertype}''')
    sleep(3)

def kerberos():
    print('\n\033[32m[SSH]\033[0;0m - Deauth user')
    nome = input('└> Digite o nome do user: ')
    ip = input('└> Digite o IP do user: ')
    vdom = input('└> Digite o VDOM do user: ')
    stdin, stdout, stderr = ssh.exec_command(
        "dia deb authd fsso list \n" + "dia deb auth fsso filter  user {} \n".format(
            nome) + " dia deb authd fsso  clear-logon \n" + "dia deb auth fsso filter clear \n")
    # lines = stdout.readlines()
    # print(lines)
    print('\n\033[32m[SSH]\033[0;0m - Usuario desautenticado com sucesso')
    print(f'''└> User: {nome}
    └> Tipo de user: {usertype}''')
    sleep(3)