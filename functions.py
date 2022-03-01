from time import sleep
import paramiko,os

class service():
    def optionMenu():
        while True:
            service.cls()
            service.banner()
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
                    service.cls()
                    service.banner()
                    sleep(1)
                    print('\033[33mTipo de Conexão\033\n')
                    sleep(1)
                    try:
                        op = int(input('''
\033[32m[1]\033[0;0m - SSH
\033[32m[2]\033[0;0m - Cabo Console
'''))
                        if op == 1:
                            fortigateFunctions.create_user_ssh()
                        elif op == 2:
                            print('\033[31mEm desenvolvimento\033[m')
                            sleep(1)
                            continue
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

class fortigateFunctions():
    #Aqui está instanciado TODAS as funções pertencentes ao Fortigate(FireWall)
    
    def create_user_ssh():
        service.cls()
        service.banner()
        sleep(1)
        print('\n\033[32m[SSH]\033[0;0m - Estabelecendo conexão SSH ')

        while True:
            try:
                sleep(1)
                host = input('└> IP do Host: ')
                port = int(input('└> Porta de acesso: '))
                user = input('└> Usuário de acesso: ')
                password = input('└> Senha de acesso: ')
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
                print("\033[31mErro de login: \033[0;0m" + str(err))
                sleep(1)
                print('Tente novente...\n {}'.format(error))
                sleep(1)
                continue
        
        while True:
            print('\n\033[32mCriação de Usuário\033[0;0m')
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
