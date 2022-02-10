import os, paramiko, serial, sys
from time import sleep
from Fortigate import libFg

#Limpar terminal
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