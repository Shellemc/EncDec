from os import system
from sys import exit
from time import sleep
from os import popen

def instalar():

    #faz a verificação se a dependencia estar instalada no sistema
    print('\033[1;92mVerificando as dependencias...\033[0m')
    sleep(3)
    procura = popen('which ccrypt').read()
    if procura:
        system('clear')
        print('\033[1;92mDependencias já instalada\033[0m')
        sleep(2)
        system('clear')
        sleep(2)
    
    #caso a dependencia não esteja instalada. exibe a mensagem e começa a instalação automatica
    else:
        system('clear')
        print('\033[1;91mDependencias não instaladas\033[0m')
        sleep(3)
        system('clear')
        print('\033[1;92mInstalando as dependencias...\033[0m')
        sleep(2)
        install = popen('apt-get install ccrypt -y').read()
        if install:
            system('clear')
            print('\033[1;92mDependencias instalada com sucesso!\033[0m')
        else:
            system('clear')
            print('\033[1;91mAlgo deu errado!!!\033[0m')
            exit()
