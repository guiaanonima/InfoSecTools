from os import system, remove, path

def clear():
	system('clear')

def add_repo_to_infosectools_list():
    system("apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6")
    system("echo '# Repositórios Kali Linux\ndeb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware' >> /etc/apt/sources.list.d/infosectools.list")
    clear()

def update_repo_list():
    system("apt-get update -m")
    clear()

def remove_infosectool_list():
    source_list = "/etc/apt/sources.list.d/infosectools.list"
    if path.exists(source_list):
        clear()
        remove(source_list)
        print("\033[1;31m\nRepositório infosectools.list removido!\n\033[1;m")
    else:
        clear()
        print("\033[1;31m\nRepositório infosectools.list já foi removido!\n\033[1;m")

def get_infosectool_list():
    try:
        clear()
        with open('/etc/apt/sources.list.d/infosectools.list', mode='r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError as error:
        print('\033[1;31m\nRepositório infosectools.list não existe!\n\033[1;m')

def return_menu():
    clear()

dict_choices_infosectools_list = {1:add_repo_to_infosectools_list,
			    2:update_repo_list,
                3:remove_infosectool_list,
				4:get_infosectool_list,
                5: clear}
