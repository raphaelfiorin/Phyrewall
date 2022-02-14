from lib import libAll

# Conexão ssh
def create_user_ssh():
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

# criando o usuario admin
    print('\n\033[32m[SSH]\033[0;0m - Criação de user')
    nome = input('└> Digite o nome do user: ')
    senha = input('└> Digite a senha: ')
    usertype = int(input("""
\033[32m[SSH]\033[0;0m - Tipo de user:
\033[32m[1]\033[0;0m - Admin_no_access
\033[32m[2]\033[0;0m - Prof_admin
\033[32m[3]\033[0;0m - Super_admin
\033[32m[4]\033[0;0m - Super_admin_readonly
\033[31m[5]\033[0;0m - Voltar ao Menu
└> """))
    if usertype == 1:
        usertype = 'admin_no_acess'
    elif usertype == 2:
        usertype = 'prof_admin'
    elif usertype == 3:
        usertype = 'super_admin'
    elif usertype == 4:
        usertype = 'super_admin_readonly'
    elif usertype == 5:
        print('Voltando ao menu!')
    else:
        print(' \033[31mEscolha os itens do menu!\033[0;0m')

    stdin, stdout, stderr = ssh.exec_command("config system admin \n" + "edit {} \n".format(nome) + " set accprofile {} \n".format(usertype) + "set vdom root \n" + "set password {} \n".format(senha) + "end \n")
    # lines = stdout.readlines()
    # print(lines)
    print('\n\033[32m[SSH]\033[0;0m - Usuario criado com sucesso')
    print(f'''└> User: {nome}
└> Tipo de user: {usertype}''')
    sleep(3)

# Conexão CABO CONSOLE
def create_user_console():
    print('\n\033[32m[CABO CONSOLE]\033[0;0m - Criação de user')
    portConsole = input('└> Número da porta: ')
    user = input('└> Digite o user: ')
    password = input('└> Digite a senha: ')

# criando o usuario admin
    nome = input('└> Digite o nome do user: ')
    senha = input('└> Digite a senha: ')
    usertype = int(input("""
\033[32m[CABO CONSOLE]\033[0;0m - Tipo de user:
\033[32m[1]\033[0;0m - Admin_no_access
\033[32m[2]\033[0;0m - Prof_admin
\033[32m[3]\033[0;0m - Super_admin
\033[32m[4]\033[0;0m - Super_admin_readonly
\033[31m[5]\033[0;0m - Voltar ao Menu
└> """))
    if usertype == 1:
        usertype = 'admin_no_acess'
    elif usertype == 2:
        usertype = 'prof_admin'
    elif usertype == 3:
        usertype = 'super_admin'
    elif usertype == 4:
        usertype = 'super_admin_readonly'
    elif usertype == 5:
        print('Voltando ao menu!')
    else:
        print(' \033[31mEscolha os itens do menu!\033[0;0m')

    ser = serial.Serial(portConsole, 9600)
    ser.write(str.encode('{}\n'.format(user) + '{}\n'.format(password) + "config system admin \n" + "edit {} \n".format(nome) + " set accprofile {} \n".format(usertype) + "set vdom root \n" + "set password {} \n".format(senha) + "end \n"))
	# resposta = ser.read(99999).decode('utf-8')
    print('\n\033[32m[CABO CONSOLE]\033[0;0m - Usuario criado com sucesso')
    print(f'''└> User: {nome}
    └> Tipo de user: {usertype}''')
    sleep(3)