#!/usr/bin/python3

from Instalacao import verificar_root
from Menu import menu, banner

# Menu
while True:
	verificar_root()
	banner()
	menu()

