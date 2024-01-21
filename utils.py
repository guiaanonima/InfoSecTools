from os import geteuid, system
import distro

def verificar_root():
	if geteuid() != 0:
		raise Exception("Este script requer privilégios de superusuário (root) para instalar ferramentas.")
	
def clear():
	system('clear')

def check_distro():
	distro_info = distro.name().lower().split()

	if distro_info[0] in ['debian', 'ubuntu', 'kali']:
		
		return {
			'instalador': 'apt', 
			'argumento_do_instalador': '-y'
		}
	
	else:
		raise Exception(f"Desculpe, este script suporta apenas instaladores de Debian, Ubuntu e Kali. Sua distribuição ({distro_info}) não é suportada.")
