import inquirer
from categorias import categorias
from instalacao import instalacao_de_pacotes
from menu_subfunctions import *
from utils import check_distro

def banner():
	print('''
8888888           .d888          .d8888b.                88888888888                888          
  888            d88P"          d88P  Y88b                   888                    888          
  888            888            Y88b.                        888                    888          
  888   88888b.  888888 .d88b.   "Y888b.    .d88b.   .d8888b 888   .d88b.   .d88b.  888 .d8888b  
  888   888 "88b 888   d88""88b     "Y88b. d8P  Y8b d88P"    888  d88""88b d88""88b 888 88K      
  888   888  888 888   888  888       "888 88888888 888      888  888  888 888  888 888 "Y8888b. 
  888   888  888 888   Y88..88P Y88b  d88P Y8b.     Y88b.    888  Y88..88P Y88..88P 888      X88 
8888888 888  888 888    "Y88P"   "Y8888P"   "Y8888   "Y8888P 888   "Y88P"   "Y88P"  888  88888P' 
                                                                                                 
				 Guia Anônima: guiaanonima.com                                                                                                                              
	   ''')



# configuração do gerenciador de pacotes referente a distribuição linux
def exibicao_de_categorias():
	
	distro = check_distro()

	while True:
		banner()
		try:
			options = [
				inquirer.Checkbox(
					'selecao_categorias',
					message = 'Qual categoria deseja instalar? (Pressione <space> para selecionar, Enter para finalizar)',
					choices = [
						('Coleta de Informações', 1),
						('Análise de Vulnerabilidade', 2),
						('Ataques Wireless', 3),
						('Aplicações Web', 4),
						('Sniffing e Spoofing', 5),
						('Relatório', 6),
						('Exploração', 7),
						('Forense', 8),
						('Teste de Estresse', 9),
						('Ataques de Senha', 10),
						('Engenharia Reversa', 11),
						('Hacking de Hardware', 12),
						('Pós Exploração', 13),
						('OSINT', 14),
						('Todas as Ferramentas', 16)
					],
				),
			]

			respostas = inquirer.prompt(options)['selecao_categorias']
			for i in respostas:
				instalacao_de_pacotes(i, categorias, distro['instalador'], distro['argumento_do_instalador'])

		except KeyboardInterrupt:
			raise Exception("Interrupção via teclado (Ctrl + C)")
		except ValueError:
			print("Escolha inválida. Tente novamente.")

def menu():
	while True:
		banner()
		inquirer_lista_incial = [
			inquirer.List(
				"lista_inicial",
				message="\033[1;36mEscolher \033[1;m",
				choices=[
					('Adicionar repositórios Kali e Atualizar', 1),
					('Visualizar Categorias', 2),
					('Sair', 0)
				],
			),
		]	

		opcao_escolhida = inquirer.prompt(inquirer_lista_incial)['lista_inicial']
		clear()

		escolha_repositorios = 0
		while opcao_escolhida == 1 and escolha_repositorios != 5:
			banner()
			inquirer_lista_repositorio = [
				inquirer.List(
					"lista_repositorio",
					message="\033[1;32mO que deseja fazer? \033[1;m",
					choices=[
						('Adicionar repositórios no infosectools.list', 1),
						('Atualizar', 2),
						('Remover lista de repositório infosectools.list', 3),
						('Visualizar o conteúdo do arquivo infosectools.list', 4),
						('Voltar', 5),

					],
				),
			]
			escolha_repositorios = inquirer.prompt(inquirer_lista_repositorio)['lista_repositorio']

			if escolha_repositorios in dict_choices_infosectools_list:
				dict_choices_infosectools_list[escolha_repositorios]()
			else:
				print("\033[1;31mDesculpe, esse foi um comando inválido!\033[1;m")

		if opcao_escolhida == 2:
			clear()
			exibicao_de_categorias()
		elif opcao_escolhida == 0:
			clear()
			exit()
