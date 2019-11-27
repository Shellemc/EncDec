from install_dependencia import instalar
from enc_dec import encode_decode
from time import sleep
from sys import exit


def banner():
	banner_ = """

	\033[1;92m
		███████╗███╗   ██╗ ██████╗  ██████╗ ███████╗ ██████╗
		██╔════╝████╗  ██║██╔════╝  ██╔══██╗██╔════╝██╔════╝
		█████╗  ██╔██╗ ██║██║       ██║  ██║█████╗  ██║     
		██╔══╝  ██║╚██╗██║██║       ██║  ██║██╔══╝  ██║     
		███████╗██║ ╚████║╚██████╗  ██████╔╝███████╗╚██████╗
		╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝
		                                                   

		[ 1 ] - Cripto e Decript
		[ 0 ] - Sair
	\033[0m
	"""
	print(banner_)
banner()

def escolha():
	escolha_ = int(input('\033[1;93m[!]Informe o número da opção desejada: \033[0m'))
	if escolha_ == 1:
		instalar()
		encode_decode()
	elif escolha_ == 0:
		print('\033[1;91mSaindo...')
		sleep(2)
		exit()

escolha()