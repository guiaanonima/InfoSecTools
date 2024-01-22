categorias = {
	1: ['Coleta de Informações', ['kali-tools-information-gathering', 'amap', 'casefile', 'dotdotpwn', 'maltego-teeth', 'sslsplit', 'sslstrip', 'wireshark']],
	2: ['Análise de Vulnerabilidade', ['kali-tools-vulnerability', 'doona', 'dotdotpwn', 'greenbone-security-assistant', 'jsql', 'ohrwurm', 'openvas-scanner', 'oscanner', 'sidguesser', 'sqlmap', 'sqlninja', 'sqlsus', 'thc-ipv6', 'tnscmd10g']],
	3: ['Ataques Wireless', ['kali-tools-wireless', 'blueranger', 'bluesnarfer', 'crackle', 'kalibrate-rtl', 'mfcuk', 'mfoc', 'mfterm', 'multimon-ng', 'redfang', 'rtlsdr-scanner', 'spooftooph']],
	4: ['Aplicações Web', ['kali-tools-web', 'gobuster', 'jsql', 'maltego-teeth', 'parsero', 'recon-ng']],
	5: ['Sniffing e Spoofing', ['kali-tools-sniffing-spoofing', 'burpsuite', 'burpsuite',  'iaxflood', 'inviteflood', 'ismtp', 'ohrwurm', 'protos-sip', 'rtpinsertsound', 'rtpmixsound', 'sctpscan', 'siparmyknife', 'sipp', 'sipvicious', 'sslstrip', 'thc-ipv6', 'voiphopper', 'webscarab', 'xspy', 'zaproxy']],
	6: ['Ferramentas de Relatório', ['kali-tools-reporting', 'casefile', 'nipper-ng']],
	7: ['Ferramentas de Exploração', ['kali-tools-exploitation',  'crackle', 'jboss-autopwn', 'linux-exploit-suggester', 'maltego-teeth',  'thc-ipv6', 'yersinia']],
	8: ['Ferramentas de Forense', ['kali-tools-forensics', 'chntpw', 'p0f']],
	9: ['Teste de Estresse', ['dhcpig', 'funkload', 'iaxflood', 'inviteflood', 'ipv6-toolkit', 'mdk3', 'reaver', 'rtpflood', 'slowhttptest', 't50', 'termineter', 'thc-ipv6', 'thc-ssl-dos']],
	10: ['Ataques de Senha', ['kali-tools-passwords', 'burpsuite', 'maltego-teeth', 'multiforcer', 'oclgausscrack', 'webscarab', 'zaproxy']],
	11: ['Engenharia Reversa', ['kali-tools-reverse-engineering', 'smali', 'valgrind', 'yara']],
	12: ['Hacking de Hardware', ['kali-tools-hardware', 'android-sdk', 'apktool', 'dex2jar', 'sakis3g', 'smali']],
    13: ['Ferramentas de Pós Exploração', ['kali-tools-post-exploitation']],
    14: ['OSINT', ['photon','sn0int','metagoofil','sherlock','maltego','theharvester','spiderfoot','osrframework','recon-ng','exiflooter', 'sherlock']],
    15: ['Ferramentas de Bug Bounty', ['FFF','airixss','Freq','Goop','Hakrawler','Httprobe','Meg','Haklistgen','Haktldextract','Hakcheckurl','tojson','gowitness','rush','hakcheckurl','shuffledns','rescope','gron','html-tool','gf','qsreplace','Amass','ffuf','assetfinder','github-subdomains','cf-check','waybackurls','nuclei','anew','notify','mildew','dirdar','unfurl','shuffledns','httpx','github-endpoints','dnsx','subfinder','gauplus','subjs','Gxss','crobat','dalfox','puredns','cariddi','interactsh-client','kxss','GetJs','hakrevdns','dnsgen']]
}

categorias[16] = ['Todas as Ferramentas', [ferramenta for ferramentas in categorias.values() for ferramenta in ferramentas[1]]] # Adicição de todas as ferramentas para opção de instalação
