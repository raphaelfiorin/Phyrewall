from libAll import *



def connection ():
    while True:
        cls()
        banner()
        ft = 'Fortigate'
        print(f'\033[34m{ft:^70}\033[m')
        escolha = int(input("""
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

                    #Conexão ssh

                    print('\033[0;34m\033[3m    Vamos conectar via SSH...\033[0;0m')
                    host = input('    Digite o host: ')
                    port = input('    Digite a porta: ')
                    user = input('    Digite o user: ')
                    password = input('    Digite a senha: ')
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    try:
                        ssh.connect(host, port, user, password)
                    except paramiko.AuthenticationException as err:
                        print("\033[31mErro de login: \033[0;0m" + str(err))
                    print('\033[33mConectado\033[m')
                    sleep(1)
                    cls()
                    banner()

                    #criando o usuraio admin
                    print('\033[0;34m\033[3m    Vamos criar o novo user ...\033[0;0m')
                    nome = input('    Digite o nome do user: ')
                    senha = input('    Digite a senha: ')
                    usertype = int(input("""
                    \n\033[0;34m\033[3m    Tipo de usuário...
                    \033[32m[1]\033[0;0m - Admin_no_access
                    \033[32m[2]\033[0;0m - Prof_admin
                    \033[32m[3]\033[0;0m - Super_admin
                    \033[32m[4]\033[0;0m - Super_admin_readonly
                    \033[31m[5]\033[0;0m - Voltar ao Menu
                    
                    └> """))
                    if usertype == 1:
                        usertype='admin_no_acess'
                    elif usertype == 2:
                        usertype='prof_admin'
                    elif usertype == 3:
                        usertype='super_admin'
                    elif usertype == 4:
                        usertype='super_admin_readonly'
                    elif usertype == 5:
                        print('Voltando ao menu!')
                    else:
                        print(' \033[31mEscolha os itens do menu!\033[0;0m')

                    stdin, stdout, stderr = ssh.exec_command("config system admin \n" + "edit {} \n".format(nome) + " set accprofile {} \n".format(usertype) + "set vdom root \n" + "set password {} \n".format(senha) + "end \n")
                    #lines = stdout.readlines()
                    #print(lines)
                    print('='*30, '\033[32mSucesso\033[m', '='*30)
                    print(f'''\033[32m
                \033[32mUsuário:\033[m {nome}
                \033[32mTipo de Usuraio:\033[m {usertype}''')
                    sleep(3)


            elif typeConnection == 2:
                portConsole = int(input('Número da porta: '))
                user = input('    Digite o user: ')
                password = input('    Digite a senha: ')

                                #criando o usuraio admin
                nome = input('Digite o nome do user: ')
                senha = input('Digite a senha: ')
                usertype = int(input("""
                \n\033[0;34m\033[3m    Tipo de usuário...
                \033[32m[1]\033[0;0m - Admin_no_access
                \033[32m[2]\033[0;0m - Prof_admin
                \033[32m[3]\033[0;0m - Super_admin
                \033[32m[4]\033[0;0m - Super_admin_readonly
                \033[31m[5]\033[0;0m - Voltar ao Menu
                
                └> """))
                if usertype == 1:
                    usertype='admin_no_acess'
                elif usertype == 2:
                    usertype='prof_admin'
                elif usertype == 3:
                    usertype='super_admin'
                elif usertype == 4:
                    usertype='super_admin_readonly'
                elif usertype == 5:
                    print('Voltando ao menu!')
                else:
                    print(' \033[31mEscolha os itens do menu!\033[0;0m')
                ser = serial.Serial(portConsole, 9600)
                ser.write(str.encode('{}\n'.format(user) + '{}\n'.format(password) + "config system admin \n" + "edit {} \n".format(nome) + " set accprofile {} \n".format(usertype) + "set vdom root \n" + "set password {} \n".format(senha) + "end \n"))
                #resposta = ser.read(99999).decode('utf-8')
                print('='*30, '\033[32mSucesso\033[m', '='*30)
                print(f'''\033[32m
\033[32mUsuário:\033[m {nome}
\033[32mTipo de Usuraio:\033[m {usertype}''')
            else:
                cls()
                connection()
        else:
            continue
connection()