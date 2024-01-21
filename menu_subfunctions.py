from os import system, remove, path
from utils import clear

def add_repo_to_infosectools_list():
    system("apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6")

    file_path = "/etc/apt/sources.list.d/infosectools.list"
    repository = "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware"

    with open(file_path, "r") as file:
        lines = file.readlines()
    
    if repository not in lines:
        with open(file_path, "w") as file:
            file.write(repository)
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
    clear()
    if not path.exists('/etc/apt/sources.list.d/infosectools.list'):
        print('\033[1;31m\nRepositório infosectools.list não existe!\n\033[1;m')
        return None

    editor_list = ['editor','nano','vi','vim','nvim','emacs']
    for editor in editor_list:
        if system(f'{editor} /etc/apt/sources.list.d/infosectools.list 2> /dev/null') == 0:
            return None
            
    print(f"Nenhum dos seguintes editores foi encontrado: ({' '.join(editor_list)})")
    
def return_menu():
    clear()

dict_choices_infosectools_list = {
    1: add_repo_to_infosectools_list,
	2: update_repo_list,
    3: remove_infosectool_list,
	4: get_infosectool_list,
    5: clear
}