from os import system, path
from subprocess import run
from categorias import categorias

def instalar_categoria(numero_da_categoria, instalador, argumento_do_instalador):
	categoria = categorias[numero_da_categoria][1]
	print(f"Instalando ferramentas na categoria {categorias[numero_da_categoria][0]}:")
	for ferramenta in categoria:
		try:
			run([instalador, 'install', ferramenta, argumento_do_instalador, '-o', 'APT::Keep-Downloaded-Packages="false"'])
		except Exception as erro:
			print(f'Error: {erro}')

def instalacao_de_pacotes(escolha, categorias, instalador, argumento_do_instalador):
	try:

		if path.exists('/etc/apt/sources.list.d/infosectools.list'):

			if escolha in categorias:
				system('clear')
				print('Atualizando lista de pacotes...')
				system('apt update -y')
				system('clear')
				print('Instalando pacotes...')
				instalar_categoria(int(escolha), instalador, argumento_do_instalador)
			else:
				print("Escolha inválida. Tente novamente.")
		
		else:
			system('clear')
		print('''> Arquivo infosectools.list não foi adicionado para instalação das ferramentas.
> Para adicioná-lo siga as opções: Voltar > Adicionar repositórios Kali e Atualizar > Adicionar repositórios no infosectools.list''')

	except Exception as erro:
		print(f'O seguinte erro foi gerado: {erro}')
