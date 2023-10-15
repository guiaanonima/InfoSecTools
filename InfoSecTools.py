#!/usr/bin/python3

import os, distro, subprocess

# Define a função para instalar ferramentas em uma categoria
def instalar_categoria(nome_categoria):
    ferramentas = categorias[nome_categoria][1]
    print(f"Instalando ferramentas na categoria {nome_categoria}:")
    for ferramenta in ferramentas:
        subprocess.run([instalador, 'install', ferramenta, argumento_do_instalador])

def verificar_root():
    if os.geteuid() != 0:
        print("Este script requer privilégios de superusuário (root) para instalar ferramentas.")
        exit(1)

verificar_root()

# Define as categorias e as ferramentas associadas
categorias = {
    1: ['Coleta de Informações', ['acccheck', 'ace-voip', 'amap', 'automater', 'braa', 'casefile', 'cdpsnarf', 'cisco-torch', 'cookie-cadger', 'copy-router-config', 'dmitry', 'dnmap', 'dnsenum', 'dnsmap', 'dnsrecon', 'dnstracer', 'dnswalk', 'dotdotpwn', 'enum4linux', 'enumiax', 'fierce', 'firewalk', 'fragroute', 'fragrouter', 'ghost-phisher', 'golismero', 'goofile', 'xplico', 'hping3', 'intrace', 'ismtp', 'lbd', 'maltego-teeth', 'masscan', 'metagoofil', 'miranda', 'nbtscan-unixwiz', 'nmap', 'p0f', 'parsero', 'recon-ng', 'set', 'smtp-user-enum', 'snmpcheck', 'sslcaudit', 'sslsplit', 'sslstrip', 'sslyze', 'thc-ipv6', 'theharvester', 'tlssled', 'twofi', 'urlcrazy','wireshark', 'wol-e']],
    2: ['Análise de Vulnerabilidade', ['bbqsql', 'bed', 'cisco-auditing-tool', 'cisco-global-exploiter', 'cisco-ocs', 'cisco-torch', 'copy-router-config', 'doona', 'dotdotpwn', 'greenbone-security-assistant', 'hexorbase', 'jsql', 'lynis', 'nmap', 'ohrwurm', 'openvas-administrator', 'openvas-cli', 'openvas-manager', 'openvas-scanner', 'oscanner', 'powerfuzzer', 'sfuzz', 'sidguesser', 'siparmyknife', 'sqlmap', 'sqlninja', 'sqlsus', 'thc-ipv6', 'tnscmd10g', 'unix-privesc-check', 'yersinia']],
    3: ['Ataques Wireless', ['aircrack-ng', 'asleap', 'bluelog', 'blueranger', 'bluesnarfer', 'bully', 'cowpatty', 'crackle', 'eapmd5pass', 'fern-wifi-cracker', 'ghost-phisher', 'giskismet', 'gqrx', 'hostapd-wpe', 'kalibrate-rtl', 'killerbee', 'kismet', 'mdk3', 'mfcuk', 'mfoc', 'mfterm', 'multimon-ng', 'pixiewps', 'reaver', 'redfang', 'rtlsdr-scanner', 'spooftooph', 'wifi-honey', 'wifiphisher', 'wifitap', 'wifite']],
    4: ['Aplicações Web', ['apache-users', 'arachni', 'bbqsql', 'blindelephant', 'burpsuite', 'cutycapt', 'davtest', 'deblaze', 'dirb', 'dirbuster', 'fimap', 'funkload', 'gobuster', 'grabber', 'jboss-autopwn', 'joomscan', 'jsql', 'maltego-teeth', 'padbuster', 'paros', 'parsero', 'plecost', 'powerfuzzer', 'proxystrike', 'recon-ng', 'skipfish', 'sqlmap', 'sqlninja', 'sqlsus', 'ua-tester', 'uniscan', 'vega', 'w3af', 'webscarab', 'websploit', 'wfuzz', 'wpscan', 'xsser', 'zaproxy']],
    5: ['Sniffing e Spoofing', ['burpsuite', 'dnschef', 'fiked', 'hamster-sidejack', 'hexinject', 'iaxflood', 'inviteflood', 'ismtp', 'isr-evilgrade', 'mitmproxy', 'ohrwurm', 'protos-sip', 'rebind', 'responder', 'rtpbreak', 'rtpinsertsound', 'rtpmixsound', 'sctpscan', 'siparmyknife', 'sipp', 'sipvicious', 'sniffjoke', 'sslsplit', 'sslstrip', 'thc-ipv6', 'voiphopper', 'webscarab', 'wifi-honey', 'wireshark', 'xspy', 'yersinia', 'zaproxy']],
    6: ['Manutenção de Acesso', ['cryptcat', 'cymothoa', 'dbd', 'dns2tcp', 'http-tunnel', 'httptunnel', 'intersect', 'nishang', 'polenum', 'powersploit', 'pwnat', 'ridenum', 'sbd', 'u3-pwn', 'webshells', 'weevely', 'winexe']],
    7: ['Ferramentas de Relatório', ['casefile', 'cutycapt', 'dos2unix', 'dradis', 'keepnote', 'magictree', 'metagoofil', 'nipper-ng', 'pipal']],
    8: ['Ferramentas de Exploração', ['armitage', 'backdoor-factory', 'beef-xss', 'cisco-auditing-tool', 'cisco-global-exploiter', 'cisco-ocs', 'cisco-torch', 'crackle', 'exploitdb', 'jboss-autopwn', 'linux-exploit-suggester', 'maltego-teeth', 'set', 'shellnoob', 'sqlmap', 'thc-ipv6', 'yersinia']],
    9: ['Ferramentas Forenses', ['binwalk', 'bulk-extractor', 'chntpw', 'cuckoo', 'dc3dd', 'ddrescue', 'python-distorm3', 'dumpzilla', 'volatility', 'xplico', 'foremost', 'galleta', 'guymager', 'iphone-backup-analyzer', 'p0f', 'pdf-parser', 'pdfid', 'pdgmail', 'peepdf', 'extundelete']],
    10: ['Teste de Estresse', ['dhcpig', 'funkload', 'iaxflood', 'inviteflood', 'ipv6-toolkit', 'mdk3', 'reaver', 'rtpflood', 'slowhttptest', 't50', 'termineter', 'thc-ipv6', 'thc-ssl-dos']],
    11: ['Ataques de Senha', ['acccheck', 'burpsuite', 'cewl', 'chntpw', 'cisco-auditing-tool', 'cmospwd', 'creddump', 'crunch', 'findmyhash', 'gpp-decrypt', 'hash-identifier', 'hexorbase', 'hydra', 'john', 'johnny', 'keimpx', 'maltego-teeth', 'maskprocessor', 'multiforcer', 'ncrack', 'oclgausscrack', 'pack', 'patator', 'polenum', 'rainbowcrack', 'rcracki-mt', 'rsmangler', 'statsprocessor', 'thc-pptp-bruter', 'truecrack', 'webscarab', 'wordlists', 'zaproxy']],
    12: ['Engenharia Reversa', ['apktool', 'dex2jar', 'python-distorm3', 'edb-debugger', 'jad', 'javasnoop', 'smali', 'valgrind', 'yara']],
    13: ['Hacking de Hardware', ['android-sdk', 'apktool', 'arduino', 'dex2jar', 'sakis3g', 'smali']],
    14: ['Extras', ['kali-linux', 'kali-linux-full', 'kali-linux-all', 'kali-linux-top10', 'kali-linux-forensic', 'kali-linux-gpu', 'kali-linux-pwtools', 'kali-linux-rfid', 'kali-linux-sdr', 'kali-linux-voip', 'kali-linux-web', 'kali-linux-wireless', 'squid3']]
}

# Adiciona uma categoria que instala todas as ferramentas de todas as categorias
categorias[15] = ['Todas as Ferramentas', [ferramenta for ferramentas in categorias.values() for ferramenta in ferramentas[1]]]

# Identifica a distribuição Linux atual
distro_info = distro.name().lower().split()

# Configura o instalador com base na distribuição Linux
if distro_info[0] in ['debian', 'ubuntu', 'kali']:
    instalador = 'apt'
    argumento_do_instalador = '-y'
elif distro_info[0] in 'arch':
    instalador = 'pacman'
    argumento_do_instalador = '-Syyu'
else:
    print(f"Desculpe, este script suporta apenas Debian, Ubuntu e Arch Linux. Sua distribuição ({distro_info}) não é suportada.")
    exit(1)

# Menu principal
while True:
    print("Categorias:")
    for categoria_id, (nome_categoria, _) in categorias.items():
        print(f"{categoria_id}) {nome_categoria}")
    print("0) Sair")
  
    escolha = input("Selecione uma categoria ou digite '0' para sair: ")
  
    if escolha == "0":
        break
  
    if int(escolha) in categorias:
        os.system('clear')
        print('Atualizando lista de pacotes...')
        os.system('apt update -y')
        os.system('clear')
        print('Instalando pacotes...')
        instalar_categoria(int(escolha))
    else:
        print("Escolha de categoria inválida. Por favor, tente novamente.")
