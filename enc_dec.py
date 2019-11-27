from sys import exit
from os import system
from time import sleep

def encode_decode():

	#menu do progaram
	menu_ = """\033[1;92m[1] - CRIPTOGRAFAR ARQUIVO
[2] - DESCRIPTOGRAFAR ARQUIVO
[0] - SAIR DO PROGRAMA\033[0m"""
	print(menu_, '\n')

	opc = int(input('\033[1;93m[+]Opção desejada: \033[0m'))
	
	#faz o encode do arquivo
	if opc == 1:
		print('\033[1;94m==========[CRIPTOGRAFAR ARQUIVO]==========\033[0m')
		nome_do_arquivo = input('\033[1;93m[+]Informe o nome do arquivo: \033[0m')
		if nome_do_arquivo == '':
			print('\033[1;91mNome do arquivo invalido!!\033[0m')
			exit()
		elif nome_do_arquivo:
			cripto = system(f'ccrypt {nome_do_arquivo}')
			if cripto == 0:
				print(f'\033[1;92mO arquivo {nome_do_arquivo} foi criptografado com sucesso\033[0m')
			elif cripto != 0:
				print('\033[1;91mAlgo deu bastante errado meu chapa\033[0m')
	
	#faz o decode do arquivo
	elif opc == 2:
		print('\033[1;94m==========[DESCRIPTOGRAFAR ARQUIVO]==========\033[0m')
		nome_do_arquivo = input('\033[1;93m[+]Informe o nome do arquivo: \033[0m')
		if nome_do_arquivo == '':
			print('\033[1;91mNome do arquivo invalido!!\033[0m')
			exit()
		elif nome_do_arquivo:
			
			decript = system(f'ccrypt -d {nome_do_arquivo}')
			if decript == 0:
				print(f'\033[1;92mO arquivo {nome_do_arquivo} foi descriptografado com sucesso\033[0m')
			elif decript != 0:
				print('\033[1;91mAlgo deu bastante errado meu chapa\033[0m')

	#verifica se o usuario quer sair do programa
	elif opc == 0:
		print('\033[1;91mFinalizando o programa...\033[0m')
		sleep(3)
		exit()
	elif opc > 2:
		print('\033[1;92mOpção invalida\033[0m')
