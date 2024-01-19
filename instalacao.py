from os import system, geteuid
from subprocess import run

def instalar_categoria(numero_da_categoria, categorias, instalador, argumento_do_instalador):
	categoria = categorias[numero_da_categoria][1]
	print(f"Instalando ferramentas na categoria {categorias[numero_da_categoria][0]}:")
	for ferramenta in categoria:
		try:
			run([instalador, 'install', ferramenta, argumento_do_instalador])
		except Exception as erro:
			print(f'Error: {erro}')

def instalacao_de_pacotes(escolha, categorias, instalador, argumento_do_instalador):
	try:
		if escolha in categorias:
			system('clear')
			print(f"Instalando ferramentas na categoria {categorias[escolha][0]}:")
			print('Atualizando lista de pacotes...')
			system('apt update -y')
			system('clear')
			print('Instalando pacotes...')
			instalar_categoria(int(escolha), categorias, instalador, argumento_do_instalador)
		else:
			print("Escolha inválida. Tente novamente.")
	except Exception as erro:
		print(erro)

def verificar_root():
	if geteuid() != 0:
		print("Este script requer privilégios de superusuário (root) para instalar ferramentas.")
		exit(1)