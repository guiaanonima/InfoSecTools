from os import system, remove
from categorias import categorias
from Instalacao import instalacao_de_pacotes
import distro

def exibicao_de_categorias():
	distro_info = distro.name().lower().split() # Descoberta de OS

	# Declaração de argumentos e afins para instalação, de acordo com cada OS
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
			escolha = input("Selecione uma ou mais categorias (1,2,3) ou digite '0' para sair: ")

			itens_escolha = escolha.split(',')

			if escolha == 'clear':
				system('clear')
			elif escolha == 'exit':
				exit(1)
			elif escolha == 0:
				break
			else:
				if len(itens_escolha) > 1:
					for instalacao in itens_escolha:
						instalacao_de_pacotes(instalacao, categorias, instalador, argumento_do_instalador)
				else:
					instalacao_de_pacotes(escolha, categorias, instalador, argumento_do_instalador)

		except KeyboardInterrupt:
			print('')
			exit(1)
		except ValueError:
			pass

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
3) Remover todos os repositórios Kali
4) Visualizar o conteúdo do arquivo sources.list
5) Voltar

			''')
			escolha_repositorios = str(input("\033[1;32mO que você deseja fazer? > \033[1;m"))
			if escolha_repositorios == "1":
				chave_apt = system("apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6")
				repositorio_adicionado = system("echo '# Repositórios Kali Linux | Adicionado pelo Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware' >> /etc/apt/sources.list")
			elif escolha_repositorios == "2":
				atualizacao_de_sistema = system("apt-get update -m")
			elif escolha_repositorios == "3":
				source_list1 = "/etc/apt/sources.list"
				source_list2 = "/etc/apt/sources.list"

				lista_para_deletar = ["# Repositórios Kali Linux | Adicionado pelo Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware\n"]
				source_list_para_remover = open(source_list1)
				remove(source_list1)
				source_list_para_adicionar = open(source_list2, "w+")
				for repositorio in source_list_para_remover:
					for palavra in lista_para_deletar:
						repositorio = repositorio.replace(palavra, "")
					source_list_para_adicionar.write(repositorio)
				source_list_para_remover.close()
				source_list_para_adicionar.close()
				print("\033[1;31m\nTodos os repositórios Kali Linux foram removidos!\n\033[1;m")
			elif escolha_repositorios == "4":
				arquivo = open('/etc/apt/sources.list', 'r')
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
