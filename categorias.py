categorias = {
	1: ['Coleta de Informações', ['kali-tools-information-gathering']],
	2: ['Análise de Vulnerabilidade', ['kali-tools-vulnerability']],
	3: ['Ataques Wireless', ['kali-tools-wireless']],
	4: ['Aplicações Web', ['kali-tools-web']],
	5: ['Sniffing e Spoofing', ['kali-tools-sniffing-spoofing']],
	6: ['Ferramentas de Relatório', ['kali-tools-reporting']],
	7: ['Ferramentas de Exploração', ['kali-tools-exploitation']],
	8: ['Ferramentas Forenses', ['kali-tools-forensics']],
	9: ['Teste de Estresse', ['dhcpig', 'funkload', 'iaxflood', 'inviteflood', 'ipv6-toolkit', 'mdk3', 'reaver', 'rtpflood', 'slowhttptest', 't50', 'termineter', 'thc-ipv6', 'thc-ssl-dos']],
	10: ['Ataques de Senha', ['kali-tools-passwords']],
	11: ['Engenharia Reversa', ['kali-tools-reverse-engineering']],
	12: ['Hacking de Hardware', ['kali-tools-hardware']],
    13: ['Ferramentas de Pós Exploração', ['kali-tools-post-exploitation']],
    14: ['Ferramentas de Bug Bounty', ['FFF,airixss,Freq,Goop,Hakrawler,Httprobe,Meg,Haklistgen,Haktldextract,Hakcheckurl,tojson,gowitness,rush,hakcheckurl,shuffledns,rescope,gron,html-tool,gf,qsreplace,Amass,ffuf,assetfinder,github-subdomains,cf-check,waybackurls,nuclei,anew,notify,mildew,dirdar,unfurl,shuffledns,httpx,github-endpoints,dnsx,subfinder,gauplus,subjs,subjs,Gxss,crobat,dalfox,puredns,cariddi,interactsh-client,kxss,GetJs,hakrevdns,dnsgen']]
}

categorias[15] = ['Todas as Ferramentas', [ferramenta for ferramentas in categorias.values() for ferramenta in ferramentas[1]]] # Adicição de todas as ferramentas para opção de instalação
