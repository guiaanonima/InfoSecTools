from os import system, remove, path
from categorias import categorias
from Instalacao import instalacao_de_pacotes
import distro

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
                                                                                                 
				Guia Anonima: guiaanonima.com                                                                                                                              
	   ''')


# configuração do gerenciador de pacotes referente a distribuição linux
def exibicao_de_categorias():
	distro_info = distro.name().lower().split()

	if distro_info[0] in ['debian', 'ubuntu', 'kali']:
		instalador = 'apt'
		argumento_do_instalador = '-y'
	elif distro_info[0] in 'arch':
		instalador = 'pacman'
		argumento_do_instalador = '-Syyu'
	else:
		print(f"Desculpe, este script suporta apenas Debian, Ubuntu e Arch Linux. Sua distribuição ({distro_info}) não é suportada.")
		exit(1)

	while True:
		print("Categorias:")
		for categoria_id, (numero_da_categoria, _) in categorias.items():
			print(f"{categoria_id} - {numero_da_categoria}")
		print("0) Sair")
		
		try:
			escolha = int(input("Selecione uma categoria ou digite '0' para sair: "))

			if escolha == 'clear':
				system('clear')
			elif escolha == 'exit':
				exit(1)
			elif escolha == 0:
				break
			else:
				instalacao_de_pacotes(escolha, categorias, instalador, argumento_do_instalador)

		except KeyboardInterrupt:
			print('')
			exit(1)
		except ValueError:
			print("Escolha inválida. Tente novamente.")

def menu():
	while True:
		print('''
1) Adicionar repositórios Kali e Atualizar
2) Visualizar Categorias
0) Sair

		''')
		opcao_escolhida = str(input("\033[1;36mGA > \033[1;m"))

		while opcao_escolhida == '1':
			print('''
1) Adicionar repositórios Kali
2) Atualizar
3) Remover lista de repositório infosectools.list
4) Visualizar o conteúdo do arquivo infosectools.list
5) Voltar

			''')
			escolha_repositorios = str(input("\033[1;32mO que você deseja fazer? > \033[1;m"))
			if escolha_repositorios == "1":
				chave_apt = system("apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6")
				repositorio_adicionado = system("echo '# Repositórios Kali Linux\ndeb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware' >> /etc/apt/sources.list.d/infosectools.list")
			elif escolha_repositorios == "2":
				atualizacao_de_sistema = system("apt-get update -m")
			elif escolha_repositorios == "3":
				source_list = "/etc/apt/sources.list.d/infosectools.list"
				if path.exists(source_list):
				    remove(source_list)
				    print("\033[1;31m\nRepositório infosectools.list removido!\n\033[1;m")
				else:
				    print("\033[1;31m\nRepositório infosectools.list já foi removido!\n\033[1;m")
				    				
			elif escolha_repositorios == "4":
				arquivo = open('/etc/apt/sources.list.d/infosectools.list', 'r')
				print(arquivo.read())
			elif escolha_repositorios == "5":
				break
			else:
				print("\033[1;31mDesculpe, esse foi um comando inválido!\033[1;m")
		if opcao_escolhida == '2':
			exibicao_de_categorias()
		elif opcao_escolhida == '0':
			exit(1)
		elif opcao_escolhida == 'clear':
			system('clear')
		elif opcao_escolhida == 'exit':
				exit(1)
