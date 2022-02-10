from libAll import *

banner()
menu = int(input('''
\033[32m[1]\033[0;0m - Fortigate - Tarefas Automatizadas
\033[31m[2]\033[0;0m - Palo alto - Cooming soon...
└> '''))

if menu == 1:
    libFg.connection()
elif menu == 2:
    pass