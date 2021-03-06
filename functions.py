from time import sleep
import paramiko,os

class service():
    def optionMenu(): #Essa função mostra um menu interativo no arquivo main.py
        while True:
            service.cls()
            service.banner()
            print('\033[35m\Main\Fortigate\Menu\033[m')
            try:
                print('\033[33mOptions Fortigate\033\n')
                sleep(1)
                option = int(input("""\033[32m[1]\033[0;0m - Criação de VPN
\033[32m[2]\033[0;0m - Desautenticar User
\033[32m[3]\033[0;0m - Criar User Admin
\033[31m[4]\033[0;0m - Voltar ao Menu
 └> """))
                if option == 1:
                    print('\033[31mEm desenvolvimento\033[m')
                    sleep(1)
                    continue
                elif option == 2:
                    print('\033[31mEm desenvolvimento\033[m')
                    sleep(1)
                    continue
                elif option == 3:
                    sleep(1)
                    print('\033[33mTipo de Conexão\033\n')
                    sleep(1)
                    try:
                        op = int(input('''\033[32m[1]\033[0;0m - SSH
\033[32m[2]\033[0;0m - Cabo Console
 └> '''))
                        if op == 1:
                            fortigateFunctions.create_user_ssh()
                        elif op == 2:
                            fortigateFunctions.create_user_console()
                    except ValueError as error:
                        print('\033[33mValor inválido!\033[m Tente novamente...\n {}'.format(error))
                        sleep(2)
                        continue

            except ValueError as error:
                print('\033[33mValor inválido!\033[m Tente novamente...\n {}'.format(error))
                sleep(2)
                continue
    def cls():
        os.system('cd C:\\Windows|cls' if os.name == 'nt' else 'clear')

    #banner
    def banner():
        print("""
        ██████╗ ██╗  ██╗██╗   ██╗██████╗ ███████╗██╗    ██╗ █████╗ ██╗     ██╗
        ██╔══██╗██║  ██║╚██╗ ██╔╝██╔══██╗██╔════╝██║    ██║██╔══██╗██║     ██║
        ██████╔╝███████║ ╚████╔╝ ██████╔╝█████╗  ██║ █╗ ██║███████║██║     ██║
        ██╔═══╝ ██╔══██║  ╚██╔╝  ██╔══██╗██╔══╝  ██║███╗██║██╔══██║██║     ██║
        ██║     ██║  ██║   ██║   ██║  ██║███████╗╚███╔███╔╝██║  ██║███████╗███████╗
        ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝ \033[1m\033[1;31m0.1\033[0;0m
                                                    \033[1m\033[32mby: Raphael Fiorin & Marcus Castilho\033[0;0m""")

#===============================|
#============================== |
#============================   |

class fortigateFunctions():
    #Aqui está instanciado TODAS as funções pertencentes ao Fortigate(FireWall)
    
    def create_user_ssh(): #Essa função faz a conexão via ssh com o FireWall e mostra um menu de opções
        import getpass
        service.cls()
        service.banner()
        print('\033[34mMain\Fortigate\Menu\Conectar Via SSH\033[m')
        sleep(1)
        print('\n\033[32m[SSH]\033[0;0m - Estabelecendo conexão SSH ')

        while True:
            try:
                sleep(1)
                host = input('└> IP do Host: ')
                port = int(input('└> Porta de acesso: '))
                user = input('└> Usuário de acesso: ')
                password = getpass.getpass('└> Senha de acesso: ', stream=None)
                print('\033[32mConectando via SSH...\033[m')
                
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
                ssh.connect(host, port, user, password)
                print('\n\033[34m[SSH Conectado]\033[m')
                sleep(1)
                break
            except ValueError as error:
                print('\033[33mValor inválido!\033[m Tente novamente...\n {}'.format(error))
                sleep(2)
                continue

            except paramiko.AuthenticationException as error:
                print("\033[31mErro de login: \033[0;0m")
                sleep(1)
                print('Tente novente...\n {}'.format(error))
                sleep(1)
                continue
        
        while True:
            print('\n\033[32m','='*10,'Criação de Usuário','='*10,'\033[0;0m')
            try:
                nome = input('└> Escolha um nome de usuário: ')
                senha = input('└> Digite a senha: ')
                usertype = int(input("""
        \033[36mTipo de usuário\033[0;0m
        \033[32m[1]\033[0;0m - Admin_no_access
        \033[32m[2]\033[0;0m - Prof_admin
        \033[32m[3]\033[0;0m - Super_admin
        \033[32m[4]\033[0;0m - Super_admin_readonly
        \033[31m[5]\033[0;0m - Voltar ao Menu
            └> """))
            except ValueError:
                print('\033[33mValor inválido!\033[m Tente novamente...\n {}'.format(error))

            if usertype == 1:
                usertype = 'admin_no_acess'
                break
            elif usertype == 2:
                usertype = 'prof_admin'
                break
            elif usertype == 3:
                usertype = 'super_admin'
                break
            elif usertype == 4:
                usertype = 'super_admin_readonly'
                break
            elif usertype == 5:
                print('Voltando ao menu!')
            else:
                print(' \033[31mEscolha os itens do menu!\033[0;0m')
                continue

        stdin, stdout, stderr = ssh.exec_command("config system admin \n" + "edit {} \n".format(nome) + " set accprofile {} \n".format(usertype) + "set vdom root \n" + "set password {} \n".format(senha) + "end \n")
        # lines = stdout.readlines()
        # print(lines)
        print('\n\033[34mUsuario criado com sucesso\033[m')
        print(f'''
        └> User: {nome}
        └> Tipo de user: {usertype}''')
        sleep(3)

    def create_user_console():
        while True:
            print('\n\033[32m[CABO CONSOLE]\033[0;0m - Criação de user')
            try:
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

            except ValueError as error:
                print('\033[33mValor inválido!\033[m Tente novamente...\n {}'.format(error))
                sleep(2)
                continue